from flask import Flask, render_template, request
from pickle import load, dump

app = Flask(__name__)
import pandas as pd


@app.route("/")
@app.route("/index")
def index():
    """
    CreatedBy: Tincharlie
    :return: Render the templates which we have created to show the home.
    """
    return render_template('index.html', title='index')


@app.route("/contact")
def contact():
    """
    CreatedBy: Tincharlie
    :return: Render templates which we have created to show the contact html.
    """
    return render_template('contact.html', title='contact')


model = load(open("model.pkl", "rb"))


# Load template on opening app home page
@app.route("/projects", methods=["POST", "GET"])
def projects():
    return render_template("projectsover.html")


# Load template on opening app home page
@app.route("/proj", methods=["POST", "GET"])
def proj1():
    return render_template("Proj1.html")


# Create predictions and show it on page
@app.route("/proj1pred", methods=["POST"])
def predict1():
    A = []
    for i in request.form.values():
        A.append(int(i))
    predicted_profit = round(model.predict(pd.DataFrame([[A[0], A[1]]]))[0][0], 2)
    return render_template("Proj1result.html", pred=predicted_profit)


bostmodel = load(open("bostMdl.pkl", "rb"))


# Load template on opening app home page

@app.route("/bostproj", methods=['POST', 'GET'])
def bostproj():
    return render_template("bostindex.html")


# Create predictions and show it on page
@app.route("/bost2predict", methods=["POST"])
def predict2():
    features = []
    for i in request.form.values():
        features.append(float(i))
    # [[features[0],features[1], features[2], features[3], features[4], features[5]]]
    # predict_price = round(model.predict([features])[0], 2)
    # predict_price = round(model.predict(features)[0], 2)
    print(features)

    predict_price = round(
        bostmodel.predict([[features[0], features[1], features[2], features[3], features[4], features[5]]])[0], 2)

    return render_template("bostresult.html", predi = predict_price)


if __name__ == "__main__":
    app.run(debug=True, port = 5002)
