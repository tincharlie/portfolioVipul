from flask import Flask, render_template, request
from pickle import load, dump
import pandas as pd

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """
    CreatedBy: Tincharlie
    :return: Render the templates which we have created to show the home.
    """
    # return render_template('index.html', title='index')
    return render_template('/index.html', title='index')


@app.route("/contact")
def contact():
    """
    CreatedBy: Tincharlie
    :return: Render templates which we have created to show the contact html.
    """
    return render_template('/cont.html', title='contact')


model = load(open("model.pkl", "rb"))


# Load template on opening app home page
@app.route("/projects", methods=["POST", "GET"])
def projects():
    return render_template("/projectsover.html")


# Create predictions and show it on page
@app.route("/50Startup", methods=["POST", "GET"])
def predict1():
    try:
        predicted_profit = None

        if request.method == 'POST':
            A = [int(i) for i in request.form.values()]
            # Assuming 'model' is your machine learning model
            predicted_profit = round(model.predict(pd.DataFrame([[A[0], A[1]]]))[0][0], 2)
        if predicted_profit == None:
            return render_template("/50Startup.html", pred="Please Pass the input...")
        return render_template("/50Startup.html", pred=predicted_profit)
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template("/50Startup.html", error=error_message)


bostmodel = load(open("bostMdl.pkl", "rb"))


# Load template on opening app home page

# @app.route("/bostproj", methods=['POST', 'GET'])
# def bostproj():
#     return render_template("/bostindex.html")


# Create predictions and show it on page
# @app.route("/bost2predict", methods=["POST"])
# @app.route("/BostonHousePrice", methods=['POST', 'GET'])
# def predict2():
#     try:
#         features = []
#         for i in request.form.values():
#             features.append(float(i))
#         # [[features[0],features[1], features[2], features[3], features[4], features[5]]]
#         # predict_price = round(model.predict([features])[0], 2)
#         # predict_price = round(model.predict(features)[0], 2)
#         print(features)

#         predict_price = round(
#             bostmodel.predict([[features[0], features[1], features[2], features[3], features[4], features[5]]])[0], 2)
#     except Exception as e:
#         predict_price = f"Error: {e}"

#     # return render_template("/BostonHousePrice.html", predi = predict_price)
#     return render_template("/bostresult.html", predi = predict_price)
    # from flask import Flask, render_template, request



# Assuming 'bostmodel' is your machine learning model for Boston House Price prediction,
# make sure it's loaded or defined properly

# Create predictions and show it on page
@app.route("/BostonHousePrice", methods=['POST', 'GET'])
def predict2():
    prediction_result = None
    try:
        if request.method == 'POST':
            features = [float(i) for i in request.form.values()]

            # Assuming 'bostmodel' is your machine learning model
            prediction_result = round(bostmodel.predict([features])[0], 2)
        if prediction_result == None:
            return render_template("/BostonHousePrice.html", predi="Please Pass the input...")
        return render_template("/BostonHousePrice.html", predi=prediction_result)
    except Exception as e:
        error_message = f"Error: {e}"
        # return render_template("/BostonHousePrice.html", error=error_message)

        return render_template("/BostonHousePrice.html", predi = error_message)

if __name__ == "__main__":
    app.run()
