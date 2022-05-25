import sqlite3
import uuid
from waitress import serve
from flask import Flask, render_template, redirect, request, abort
import config
from connectionmanager import executedb

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)


@app.route("/")
def index():
    return render_template("/index.html", themecss=config.themecss, servicename=config.servicename)

@app.route("/about")
def about():
    return render_template("/about.html", themecss=config.themecss, about=config.about)

@app.route("/privacy")
def privacy():
    if config.privacyredirect.lower() != "true":
        return render_template("/privacy.html", themecss=config.themecss, privacypolicy=config.privacypolicy)
    else:
        return redirect(config.privacypolicylink)
    


@app.route("/report")
def report():
    return render_template(
        "/report.html", reporturl=config.reporturl, themecss=config.themecss
    )


@app.route("/", methods=["POST"])
def linkcreate():
    text = request.form["text"]
    processed_text = text.upper()
    executedb(
        'INSERT INTO "main"."links"("url","originalurl","deleteuuid","creationstamp") VALUES (NULL,NULL,NULL,NULL);'
    )
    return processed_text

@app.route('/<shortlink>')
def url_redirect(shortlink):
    if shortlink == "a":
        return redirect("google.com")
    else:
        abort(404)



@app.errorhandler(404)
def invalid_route(e):
    return render_template("/404.html", themecss=config.themecss)


# @app.route("/git/<url>")
# def reroute(url):
#     return render_template("/index.html")

if __name__ == "__main__":
    app.run()
    # serve(app, host='0.0.0.0', port=8080)
