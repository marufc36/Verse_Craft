from flask import Flask, render_template, request
from gradio_client import Client

# Initialize Flask app
app = Flask(__name__)

# Define route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Define route for the prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get user input from the form
    user_input = request.form["user_input"]

    # Initialize Gradio client and make prediction
    client = Client("mmchowdhury/VerseCraft")
    result = client.predict(user_input, api_name="/predict")

    # Render the prediction result
    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
