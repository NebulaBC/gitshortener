import os
import subprocess
from urllib.parse import urlparse


def processurl(url):
    domain = urlparse(url).netloc
    if domain == "":
        return "Please input a valid URL!"
    elif domain == "github.com" or domain == "gitlab.com":
        shortlink = (
            str(os.path.basename(url.rsplit(".git", 1)[0])).rstrip("\\n'").lstrip("b'")
        )
        if len(shortlink) <= 100:
            return "https://g.neb.cx/" + shortlink
        else:
            return "Your repo is over 100chars!"
    else:
        return "Please input a github/lab domain!"
