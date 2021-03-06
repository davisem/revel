import sqlite3 as sql
import os
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/search', methods=["POST"])
def search():

    chrom = request.form['chrom']
    coord = request.form['coord']
    db = request.form['db']

    if db.lower() != 'revel':
        return "Sorry, only the revel database is supported", 404

    if not chrom:
        return "Must provide a valid Chromosome", 404

    if not coord:
        return "Must provide a valid Coordinate", 404

    return redirect(url_for("result", chrom=chrom, start=coord))


@app.route('/result/<chrom>/<start>', methods=["GET"])
def result(chrom, start):

    conn = sql.connect("REVEL.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()

    rows = cur.execute('SELECT * FROM variants WHERE chrom=? and hg19_pos=?', (chrom, start))

    return render_template("result.html", rows=rows, chrom=chrom, start=start)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)