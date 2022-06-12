import sqlite3
import uuid
from waitress import serve
from flask import Flask, render_template, redirect, request, abort
import config
from connectionmanager import executedb
from linkprocesser import canshortlink, getshortlink, processurl
import datetime
from urllib.parse import quote
import logging

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)


@app.route("/")
def index():
    return render_template(
        "/index.html", themecss=config.themecss, servicename=config.servicename
    )


@app.route("/about")
def about():
    return render_template("/about.html", themecss=config.themecss, about=config.about)


@app.route("/privacy")
def privacy():
    if config.privacyredirect.lower() != "true":
        return render_template(
            "/privacy.html",
            themecss=config.themecss,
            privacypolicy=config.privacypolicy,
        )
    else:
        return redirect(config.privacypolicylink)


@app.route("/report")
def report():
    return render_template(
        "/report.html", reporturl=config.reporturl, themecss=config.themecss
    )


@app.route("/", methods=["POST"])
def linkcreate():
    timestamp = datetime.datetime.now().strftime("%m%d%y%H%M%S")
    deleteid = str(uuid.uuid4())
    text = request.form["text"]
    processed_text = quote(text.lower(), safe='/.?&#,!:')
    returntext = processurl(processed_text, deleteid)
    if canshortlink(processed_text):
        shorturl = quote(getshortlink(processed_text), safe='/.?&#,!:')
        executedb(
            'INSERT INTO "main"."links"("url","originalurl","deleteuuid","creationstamp","address") VALUES (\"' + shorturl + '\",\"' + processed_text + '\",\"' + deleteid + '\",\"' + timestamp + '\",\"' + request.remote_addr + '\");'
        )
    return returntext


@app.route("/<shortlink>")
def url_redirect(shortlink):
    if shortlink == "url" or shortlink == "about" or shortlink == "privacy" or shortlink == "report":
        abort(404)
    try:
        return redirect(executedb(
            'SELECT "originalurl" FROM "main"."links" WHERE "url" = "{}";'.format(
                quote(shortlink, safe='/.?&#,!:')
            )
        )[0][0])
    except:
        abort(404)


@app.errorhandler(404)
def invalid_route(e):
    return render_template("/404.html", themecss=config.themecss)

if __name__ == "__main__":
    # app.run()
    serve(app, host='0.0.0.0', port=8080)
