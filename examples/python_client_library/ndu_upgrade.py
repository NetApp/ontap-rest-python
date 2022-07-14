"""
ONTAP REST API Python Client Library Sample Scripts

This script was developed by NetApp to help demonstrate NetApp
technologies. This script is not officially supported as a
standard NetApp product.

NOTE: AUTOBOOT must already be set to true or else ANDU will complain and it
      cannot be set via REST today (not even the CLI passthrough) so this script
      isn't doing it. If you need to, run this on your cluster:

      run * bootargs set AUTOBOOT true

workflow:
    1. Show the current cluster software version and available packages
    2. Download a new software package
    3. PATCH the cluster software to use the new package
    4. Monitor the progress

Copyright (c) 2020 NetApp, Inc. All Rights Reserved.

Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause

"""

import argparse
from http.server import SimpleHTTPRequestHandler
import os
from pprint import pprint
import socket
import socketserver
from threading import Thread
import time

from netapp_ontap.error import NetAppRestError
from netapp_ontap.resources import CLI, Node, Software, SoftwarePackage, SoftwarePackageDownload

from utils import (
    Argument, parse_args, setup_logging, setup_connection, step, substep,
    LiveMultilineOutput
)


def show_current_cluster_image():
    """Verify our current software status"""

    step("Show the packages")
    substep("Show the current cluster image")
    software = Software()
    software.get()
    print("Current software package:", software)

    substep("Show the available software packages")
    print("Available software packages:", list(SoftwarePackage.get_collection()))
    return software


def download_new_cluster_image(parsed_args: argparse.Namespace):
    """Start our HTTP server and tell ONTAP to start downloading the new image"""

    step("Download a new software package")
    substep("Start an HTTP server to serve the file")
    image_server = Thread(target=serve_image_download, args=(parsed_args,))
    image_server.start()

    substep("Have ONTAP download the package")
    local_ip = socket.gethostbyname(socket.gethostname())
    url = "http://%s:%s/%s" % (local_ip, parsed_args.port, parsed_args.image_path)
    download_package = SoftwarePackageDownload(url=url)
    download_package.post(poll_timeout=1200, poll_interval=60)
    image_server.join()

    substep("Show the new package")
    packages = list(SoftwarePackage.get_collection())
    print("Available software packages:", packages)
    return packages[0]


def update_cluster_image(software, new_package):
    """Set the new version of the software on the cluster"""

    step("Update the cluster to the new image")
    software.version = new_package.version
    try:
        if Node.count_collection() > 1:
            # make sure cluster HA is enabled
            cli = CLI()
            cli.execute("cluster ha modify", body={"configured": "true"})
        software.patch(poll_timeout=1200, poll_interval=30, skip_warnings="true")
    except NetAppRestError:
        print("Current cluster software status:")
        software.get()
        pprint(software)


def monitor_progress(software):
    """Until all nodes are complete, monitor and print the status of the upgrade"""

    step("Watch the progress")

    errors = 0
    with LiveMultilineOutput() as output:
        while True:
            try:
                software.get(fields="state,status_details,elapsed_duration,estimated_duration")
                if not software.state == "in_progress":
                    break
                errors = 0
                new_list = []
                for detail in software.status_details:
                    new_list.append(
                        "[%s]: %s - %s"
                        % (detail.node.name, detail.name, detail.issue.message)
                    )
                percent_complete = (
                    software.elapsed_duration / software.estimated_duration
                ) * 100
                new_list.append("%.2f%% complete (estimate)" % percent_complete)
                output.change(new_list)
            except Exception:  # pylint: disable=broad-except
                errors += 1
                if errors > 10:
                    break
            finally:
                time.sleep(30)
    if errors > 10:
        raise RuntimeError("ERROR: No longer could communicate with the server. Is it down?")


def serve_image_download(parsed_args):
    """Start a temporary HTTP server to allow ONTAP to download the image file"""

    if parsed_args.image_path.startswith("/"):
        os.chdir("/")
    port = parsed_args.port
    local_ip = socket.gethostbyname(socket.gethostname())
    httpd = socketserver.TCPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print("serving package download at http://%s:%s" % (local_ip, port))

    # ONTAP does 3 HEAD requests followed by the GET we care about
    httpd.handle_request()
    httpd.handle_request()
    httpd.handle_request()
    httpd.handle_request()


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details", required=True),
        Argument(
            "-p", "--port", "The port to open as an HTTP server to serve the ONTAP image from",
            default=7654, arg_type=int,
        ),
        Argument(
            "-i", "--image-path", "The path to an ONTAP image which will be downloaded by ONTAP",
            required=True,
        )
    ]
    args = parse_args("This script will update the nodes of an ONTAP cluster.", arguments)
    setup_logging()
    setup_connection(args.cluster, args.api_user, args.api_pass)

    software = show_current_cluster_image()
    new_package = download_new_cluster_image(args)
    update_cluster_image(software, new_package)
    monitor_progress(software)

    software.get()
    print("Upgrade complete! Current version: %s" % software.version)


if __name__ == "__main__":
    main()
