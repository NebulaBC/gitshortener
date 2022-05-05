import sqlite3
from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/')
def index():
   return render_template('/index.html')
if __name__ == '__main__':
   app.run()

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template('/404.html')