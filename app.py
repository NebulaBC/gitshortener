import sqlite3
import uuid
from waitress import serve
from flask import Flask, render_template, redirect, request

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)

# print(uuid.uuid4())'


@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/", methods=["POST"])
def my_form_post():
    text = request.form["text"]
    processed_text = text.upper()
    try:
        sqLiteConnection = sqlite3.connect("links.sqlite")
        cursor = sqLiteConnection.cursor()
        sqliteCommand = 'INSERT INTO "main"."links"("url","originalurl","deleteuuid","creationstamp") VALUES (NULL,NULL,NULL,NULL);'
        cursor.execute(sqliteCommand)
        sqLiteConnection.commit()
        record = cursor.fetchall()
        print(record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqLiteConnection:
            sqLiteConnection.close()
            print("sqLiteConnection closed")
    return processed_text


@app.errorhandler(404)
def invalid_route(e):
    return render_template("/404.html")


# @app.route("/git/<url>")
# def reroute(url):
#     return render_template("/index.html")

if __name__ == "__main__":
    app.run()
    # serve(app, host='0.0.0.0', port=8080)
