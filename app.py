from flask import Flask, render_template

# Create the Flask Application
app = Flask(__name__)
# Tell it what to do when someone visits the homepage
@app.route("/")
def home():
    # Send text back to the browser
    return render_template("index.html")




if __name__ == "__main__":
    # Start a local development server
    app.run(debug=True)