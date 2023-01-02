import os

import openai
from flask import Flask, redirect, render_template, request, url_for, send_file


app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        image = request.form["image"]
        try:
            response = openai.Image.create(
                prompt=image,
                n=1,
                size="512x512"
            )
        except:
            return render_template("index.html", err = "Vulgar terminology is not allowed.")
        url = response['data'][0]['url']
        
        return redirect(url_for("index", result=url))

    result = request.args.get("result")
    return render_template("index.html", result=result)



