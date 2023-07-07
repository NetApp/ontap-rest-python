import logging
from netapp_ontap import NetAppRestError
from netapp_ontap.resources import Volume
from netapp_ontap.resources import FileInfo
from utils import Argument, parse_args, setup_connection

# REFERENCES
# https://devnet.netapp.com/restapi.php
# https://pypi.org/project/netapp-ontap/
# https://library.netapp.com/ecmdocs/ECMLP2858435/html/resources/volume.html
# https://library.netapp.com/ecmdocs/ECMLP2885777/html/resources/file_info.html
# https://community.netapp.com/t5/ONTAP-Rest-API-Discussions/FileInfo-Received-list-directory-more-than-one-record/m-p/440962


def list_files(volume, path):
    """Recursively list files on a volume"""
    files = FileInfo.get_collection(volume.uuid, path)
    for f in files:
        if f.name != "." and f.name != "..":
            if f.type == "file":
                print(f"{path}{f.name}")
            elif f.type == "directory" and f.name != ".snapshot":
                print(f"{path}{f.name}/")
                list_files(volume, f"{path}{f.name}/")


def delete(volume, pathname, recursive=False):
    """Delete a file or directory on a volume"""
    try:
        resource = FileInfo(volume.uuid, path=pathname)
        resource.delete(recurse=recursive)
    except NetAppRestError as error:
        if recursive:
            extra = "(recursively) "
        else:
            extra = ""
        logging.critical(
            f"delete: File or directory {pathname} was not deleted {extra}on {volume.name} ({error})")


def create_directory(volume, pathname):
    """Create a directory on a volume"""
    resource = FileInfo(volume.uuid, pathname)
    resource.type = "directory"
    resource.unix_permissions = "644"
    try:
        resource.post()
    except NetAppRestError as error:
        logging.critical(
            f"create_directory: Directory {pathname} was not created on {volume.name} ({error})")


def create_file(volume, pathname, contents):
    try:
        resource = FileInfo(volume.uuid, pathname)
        resource.post(
            hydrate=True, data="the data to be written to the new file")
        resource.patch()
    except NetAppRestError as error:
        logging.critical(
            f"create_file: File {pathname} was not created on {volume.name} ({error})")


def file_handling(volume_name):
    try:
        all_volumes = list(Volume.get_collection())
        for vol in all_volumes:
            if vol.name == volume_name:
                print(f"Volume: {vol.name} ({vol.uuid})")
                create_file(vol, "alice", "lorem ipsum")

                create_directory(vol, "bobsfiles")
                create_file(vol, "bobsfiles/bob", "lorem ipsum")

                create_directory(vol, "bobsfiles/charliesfiles")
                create_file(
                    vol, "bobsfiles/charliesfiles/charlie1", "lorem ipsum")
                create_file(
                    vol, "bobsfiles/charliesfiles/charlie2", "lorem ipsum")
                create_file(
                    vol, "bobsfiles/charliesfiles/charlie3", "lorem ipsum")

                list_files(vol, "/")

                print("Cleaning up...")
                delete(vol, "/alice", False)
                delete(vol, "/bobsfiles", True)
                print("Done.")
    except NetAppRestError as error:
        print("Exception :" + str(error))


def main() -> None:
    """Main function"""

    arguments = [
        Argument("-c", "--cluster", "API server IP:port details"),
        Argument("-v", "--volume_name", "Volume Name")]
    args = parse_args(
        "This script will demo          nstrate enumerating volumes, file and directory creation, file and directory creation deletion",
        arguments,
    )

    setup_connection(args.cluster, args.api_user, args.api_pass)
    file_handling(args.volume_name)


if __name__ == "__main__":
    main()