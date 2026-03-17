from flask import Flask, request, jsonify, render_template
from analyzer import analyze_resume, compare_resume_with_job

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    resume_text = data.get("resume_text")

    if not resume_text:
        return jsonify({"error": "resume_text is required"}), 400

    result = analyze_resume(resume_text)
    return jsonify(result), 200


@app.route("/match", methods=["POST"])
def match():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    resume_text = data.get("resume_text")
    job_description = data.get("job_description")

    if not resume_text:
        return jsonify({"error": "resume_text is required"}), 400

    if not job_description:
        return jsonify({"error": "job_description is required"}), 400

    result = compare_resume_with_job(resume_text, job_description)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)