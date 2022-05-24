import os
import subprocess
from urllib.parse import urlparse


def processurl(url):
    domain = urlparse(url).netloc
    if domain == "":
        print("Please input a valid URL!")
    elif domain == "github.com" or domain == "gitlab.com":
        shortlink = (
            str(
                subprocess.check_output(
                    "basename " + url.rsplit(".git", 1)[0], shell=True
                )
            )
            .rstrip("\\n'")
            .lstrip("b'")
        )
        if len(shortlink) <= 100:
            print("https://g.neb.cx/" + shortlink)
        else:
            print("Your repo is over 100chars!")
    else:
        print("Please input a github/lab domain!")
