from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "👋 Hello from Flask SRE App!"

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/health')
def health():
    return "✅ App is healthy!", 200

if __name__ == '__main__':
    app.run(debug=True)
