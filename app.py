from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]["summary_text"]
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
