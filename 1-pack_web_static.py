#!/usr/bin/python3
"""A Fabric script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack.
"""


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo.
    """
    from fabric.api import local
    from datetime import datetime

    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format
                   (datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if result.failed:
        return None
    return result
