import sqlite3 as sql
import os
from flask import Flask, render_template, json, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'You Will Never Guess'
app.config['SESSION_TYPE'] = 'filesystem'

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

    return redirect(url_for("result", chrom=chrom, start=coord))


@app.route('/result/<chrom>/<start>', methods=["GET"])
def result(chrom, start):

    # replace with query
    rows = [{"chrom": "chr{}".format(chrom),
             "hg19_pos": start,
             "ref": "A",
             "alt": "T",
             "aaref": "TT",
             "aaalt": "TT",
             "REVEL": 0.01}]

    return render_template("result.html", rows=rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)