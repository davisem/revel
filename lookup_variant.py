import sqlite3 as sql
import os
from flask.ext.cache import Cache
from flask import Flask, render_template, json, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'You Will Never Guess'
app.config['SESSION_TYPE'] = 'filesystem'

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/search', methods=["POST", "GET"])
def search():
    data = json.dumps(request.json)
    return redirect(url_for("whatever", chrom='1', start='35146'))

@app.route('/whatever/<chrom>/<start>', methods=["POST", "GET"])
def whatever(chrom, start):

    query = "SELECT * FROM variants WHERE chrom={} and hg19_pos={}".format(chrom, start)
    conn = sql.connect("REVEL.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    rows = cur.execute(query)
    return render_template("result.html", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)