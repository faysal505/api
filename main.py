from flask import Flask, render_template
import requests


app = Flask(__name__)


# @app.route('/')
# def hoem():
#     return render_template('link.html')

@app.route("/<string:nid>/<string:dob>")
def vata(nid, dob):
    link = 'https://mis.bhata.gov.bd/beneficiary/verifynidinfo'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    }

    data = {
        "nid": nid,
	    "dob": dob
    }

    print("nid: " + nid)
    print("nid: " + dob)

    r = requests.post(link, json=data, headers=headers)
    if r.status_code == 200:
        res = r.content.decode('unicode_escape')
        return res
    else:
        return "something wrong"


if __name__ == '__main__':
    app.run(debug=True)