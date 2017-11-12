import sqlite3 as sql
import os
from flask.ext.cache import Cache
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/result', methods=["POST", "GET"])
def result():
    return "result.html"

@app.route('/search', methods=["POST", "GET"])
def search():
    data = json.dumps(request.json)
    #TODO parse data
    
    conn = sql.connect("REVEL.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM variants WHERE chrom={} and hg19_pos={}".format('1', '35146'))

    return render_template("result.html", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)