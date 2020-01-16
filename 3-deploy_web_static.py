#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive
    from the contents of the web_static
"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["35.196.228.78", "35.231.75.201"]


def do_pack():
    """
        Compress all files before sending
    """
    time_now = datetime.now()
    files = "web_static_{}{}{}{}{}{}.tgz".format(
            time_now.year, time_now.month, time_now.day,
            time_now.hour, time_now.minute, time_now.second)
    try:
        local("mkdir -p versions")
        local("tar -cavf versions/{} web_static".format(files))
        return "versions/{}".format(files)
    except Exception:
        return None


def do_deploy(archive_path):
    """
        Sends `archive_path` to a web server.
        Args:
            archive_path (str): path of the .tgz file to transfer

        Returns: True on success, False otherwise.
    """
    # if the file at the path archive_path doesn't exist
    if not os.path.exists(archive_path):
        return False

    file_tar = archive_path[9:]
    dir_tar = archive_path[9:-4]
    path = "/data/web_static/releases/"

    try:
        # upload /tmp/ directory of the web server
        put(archive_path, '/tmp')
        # Create directory if doesn't exits
        run("mkdir -p {}{}".format(path, dir_tar))
        # Umcompress the file in /data/web_static/releases/ and remove
        run("tar -zxf /tmp/{} -C {}{}".format(file_tar, path, dir_tar))
        run("rm -rf /tmp/{}".format(file_tar))

        run("mv {0}{1}/web_static/* {0}{1}/".format(path, dir_tar))
        run("rm -rf {}{}/web_static".format(path, dir_tar))
        # Delete symbolic link
        run("rm -rf /data/web_static/current")
        # create new symbolic link
        run("ln -s {}{} /data/web_static/current".format(path, dir_tar))

        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """
        Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
