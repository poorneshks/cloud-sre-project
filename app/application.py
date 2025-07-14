from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "👋 Hello from Flask SRE App v2!"

if __name__ == "__main__":
    # Use Flask's built-in development server when running locally
    app.run(debug=True, host="0.0.0.0", port=5000)
