from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment_result = None
    if request.method == "POST":
        user_text = request.form.get("user_text")
        if user_text:
            analysis = TextBlob(user_text)
            polarity = analysis.polarity
            subjectivity = analysis.subjectivity

            if polarity > 0:
                sentiment = "Positive"
            elif polarity < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            sentiment_result = {
                "text": user_text,
                "polarity": round(polarity, 2),
                "subjectivity": round(subjectivity, 2),
                "sentiment": sentiment,
            }
    return render_template("index.html", result=sentiment_result)

if __name__ == "__main__":
    app.run(debug=True)
