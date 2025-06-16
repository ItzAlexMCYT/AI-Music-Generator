from flask import render_template, request
from app import app
from app.musica import generar_melodia
import os

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        nombre_archivo = generar_melodia(prompt)
        return render_template("index.html", archivo=nombre_archivo)
    return render_template("index.html", archivo=None)
