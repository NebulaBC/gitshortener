import os
from urllib.parse import urlparse
from urllib.parse import quote
import config
from connectionmanager import executedb


def processurl(url, deleteid):
    domain = quote(urlparse(url).netloc, safe="/.?&#,!:")
    safeurl = quote(url, safe="/.?&#,!:")
    if (
        domain == ""
        or getshortlink(url) == "about"
        or getshortlink(safeurl) == "privacy"
        or getshortlink(safeurl) == "report"
    ):
        return "Please input a valid URL!"
    elif (
        executedb(
            'SELECT COUNT(*) FROM "main"."links" WHERE "url" LIKE \''
            + getshortlink(safeurl)
            + "';"
        )[0][0]
        > 0
    ):
        return "This URL has already been shortened!"
    elif domain == "github.com" or domain == "gitlab.com":
        shortlink = (
            str(os.path.basename(url.rsplit(".git", 1)[0])).rstrip("\\n'").lstrip("b'")
        )
        if len(shortlink) <= 100:
            return (
                config.baseurl
                + shortlink
                + "<br> Your delete uuid is: "
                + deleteid
                + "<br> Keep track of this (or your current ip address) if you would like to delete your link in the future."
            )
        else:
            return "Your repo is over 100chars!"
    else:
        return "Please input a github/lab domain!"


def getshortlink(url):
    domain = quote(urlparse(url).netloc, safe="/.?&#,!:")
    if domain == "github.com" or domain == "gitlab.com":
        shortlink = (
            str(os.path.basename(url.rsplit(".git", 1)[0])).rstrip("\\n'").lstrip("b'")
        )
        if len(shortlink) <= 100:
            return shortlink


def canshortlink(url):
    domain = quote(urlparse(url).netloc, safe="/.?&#,!:")
    safeurl = quote(url, safe="/.?&#,!:")
    if (
        domain == ""
        or getshortlink(safeurl).lower() == "about"
        or getshortlink(safeurl).lower() == "privacy"
        or getshortlink(safeurl).lower() == "report"
        or executedb(
            'SELECT COUNT(*) FROM "main"."links" WHERE "url" LIKE \''
            + getshortlink(safeurl).lower()
            + "';"
        )[0][0]
        != 0
    ):
        return False
    elif domain == "github.com" or domain == "gitlab.com":
        shortlink = (
            str(os.path.basename(url.rsplit(".git", 1)[0])).rstrip("\\n'").lstrip("b'")
        )
        if len(shortlink) <= 100:
            return True
        else:
            return False
    else:
        return False
