#!/usr/bin/python3
from fabric.api import local
from time import strftime as tm
from datetime import date


def do_pack():
    """ A script which generates archive the contents of web_static folder"""

    filename = tm("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
