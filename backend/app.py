from flask import Flask, request, jsonify
from similarity import find_similar_threads
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin support (useful if frontend is separate)

@app.route('/search', methods=['POST'])
def search_threads():
    data = request.get_json()
    query = data.get("query", "")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        results = find_similar_threads(query)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

