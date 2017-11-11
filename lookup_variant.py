import sqlite3 as sql
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')
@app.route('/result', methods=["GET"])
def result():
    conn = sql.connect("REVELmock.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM variants WHERE chrom={} and pos={}".format('1', '100'))
    rows = [{"chrom":"1", "pos":"100", "ref":"A", "alt":"T","REVEL":".89"}]
    return render_template("result.html", rows=rows)

@app.route('/search', methods=["POST"])
def search():
    
    data = json.dumps(request.json)

    return redirect(url_for('result'))

if __name__ == "__main__":
    app.run(port=5002)