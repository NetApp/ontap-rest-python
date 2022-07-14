#! /usr/bin/env python3

"""
ONTAP REST API Python Sample Scripts

This script was developed by NetApp to help demonstrate
NetApp technologies. This script is not officially
supported as a standard NetApp product.

Purpose: This script will enable certificate authentication on the provided account (or admin)

usage: cert_auth [-h] -c CLUSTER [-u API_USER] [-p API_PASS] [-a CERT_ACCOUNT] [-o ORGANIZATION]

Workflow:
    1. List the certs currently installed on the system
    2. Generate and install a new root_ca cert on the cluster
    3. Generate a signing request and have the cluster sign it
    4. Use the signed certificate in a verified TLS connection

NOTE: Make sure time is set correctly on the cluster (or NTP is configured) or
      else the newly created certificate may be rejected as not being in the
      valid period, especially if ONTAP is running behind the server this script
      is run from.

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New or Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""

import argparse
import logging
import tempfile
import time

from netapp_ontap import HostConnection, NetAppRestError
from netapp_ontap.resources import Account, AccountApplication, SecurityCertificate, Volume

from utils import Argument, step, substep, parse_args, run_cmd, setup_connection, setup_logging


def install_cert(parsed_args: argparse.Namespace) -> SecurityCertificate:
    """Create and install a new root cert"""

    common_name = "%sCA" % parsed_args.organization
    cert = SecurityCertificate.find(common_name=common_name, type="root_ca")
    if cert is None:
        substep("Create a new root CA in ONTAP for %s" % parsed_args.organization)
        cert = SecurityCertificate(
            type="root_ca", common_name=common_name, expiry_time="3652days",
        )
        cert.post(hydrate=True)
    else:
        substep("Using existing root CA for %s" % parsed_args.organization)

    substep("Show the installed root CA")
    logging.info(cert)
    return cert


def sign_domain(
        my_ca: SecurityCertificate, temp_path: str, parsed_args: argparse.Namespace
    ) -> SecurityCertificate:
    """Generate a signing request and have it signed by the CA we just installed"""

    subject = (
        "/C=US/ST=PA/L=Pittsburgh/O=%s/OU=BestPart/CN=%s" %
        (parsed_args.organization, parsed_args.cert_account)
    )

    substep("Generate the private key")
    run_cmd("openssl genrsa -out %s/cert_user.key 2048" % temp_path)

    substep("Generate the certificate signing request")
    run_cmd(
        "openssl req -sha256 -new -nodes -key %s/cert_user.key"
        ' -subj "%s" -out %s/cert_user.csr' % (temp_path, subject, temp_path)
    )

    substep("Sign the CSR with our root CA")
    with open("%s/cert_user.csr" % temp_path) as signing_request_file:
        response = my_ca.sign(body={"signing_request": signing_request_file.read()})

    substep("Create a cert object from the response")
    cert = SecurityCertificate.from_dict(response.http_response.json())
    logging.info(cert)
    with open("%s/cert_user.cert" % temp_path, "w") as cert_file:
        cert_file.write(cert.public_certificate)
    return cert


def enable_cert_auth(parsed_args: argparse.Namespace) -> Account:
    """Install the client cert as a client-ca and enable cert auth """

    account = Account.find(name=parsed_args.cert_account)
    if account is None:
        substep("Create an account that uses cert auth")
        account = Account(
            name="cert_user",
            applications=[
                AccountApplication(application="http", authentication_methods=["cert"])
            ],
        )
        account.post()
    else:
        http_application = [a for a in account.applications if a.application == "http"]
        if http_application and "cert" in http_application[0].authentication_methods:
            substep("The %s account is already cert-enabled")
        else:
            substep("Modifying the %s account for cert authentication" % account.name)
            if http_application:
                http_application[0].authentication_methods.append("cert")
            else:
                http_application = AccountApplication(
                    application="http", authentication_methods=["cert"],
                )
                account.applications.append(http_application)
            account.patch()
    return account


def test_cert_auth(parsed_args: argparse.Namespace, temp_path: str) -> None:
    """Verify our account can connect with a cert and no user/pass. After uploading
    and creating a user account, it can take some time before authentication works.
    In my testing, I've seen it take about 10 seconds. The while loop here tries
    to paper over that.
    """

    substep("List the volumes using a connection with cert-based auth")
    cert_conn = HostConnection(
        parsed_args.cluster, cert="%s/cert_user.cert" % temp_path,
        key="%s/cert_user.key" % temp_path, verify=False,
    )
    with cert_conn:
        tries = 0
        while True:
            try:
                logging.info([vol.name for vol in Volume.get_collection()])
                logging.debug("Succeeded on try %s", tries)
                break
            except NetAppRestError as err:
                resp = err.http_err_response
                if resp is None or resp.http_response.status_code == 401:
                    tries += 1
                    if tries > 60:
                        logging.error("Not able to authenticate within 60 tries")
                        raise
                    time.sleep(1)
                else:
                    raise


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details", required=True),
        Argument(
            "-a", "--cert_account", "Account which be used for certificate authentication",
            default="admin",
        ),
        Argument(
            "-o", "--organization", "Organization name for the root certificate",
            default="MyCompany",
        )
    ]
    args = parse_args(
        "This script will enable certificate authentication on the provided account (or admin)",
        arguments,
    )
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    # make a temp directory for certs to live in
    dirpath = tempfile.mkdtemp()

    step("Install a root CA for %s" % args.organization)
    my_ca = install_cert(args)

    step("Sign a CSR for cert_user with our root")
    sign_domain(my_ca, dirpath, args)

    step("Install signed cert as client-ca")
    enable_cert_auth(args)

    step("Verify cert auth works for our user")
    test_cert_auth(args, dirpath)


if __name__ == "__main__":
    main()
