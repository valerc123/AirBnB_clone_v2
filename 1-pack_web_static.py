#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    time_now = datetime.now()
    files = "web_static_{}{}{}{}{}{}.tgz".format(time_now.year, time_now.month,
            time_now.day, time_now.hour, time_now.minute, time_now.second)
    try:
        local("mkdir -p versions")
        local("tar -cavf versions/{} web_static".format(files))
        return "versions/{}".format(files)
    except Exception:
        return False
