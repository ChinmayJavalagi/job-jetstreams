from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title": "Flutter Developer",
        "location": "Remote",
        "salary": "Rs. 33,00,000"
    },
    {
        "id":2,
        "title": "Intern Software Engineer",
        "location": "Bengaluru, India",
        "salary": "Rs. 10,00,000"
    },
    {
        "id":3,
        "title": "Application Developer",
        "location": "Chennai, India",
        "salary": "Rs. 21,00,000"
    },
    {
        "id":4,
        "title": "Product Manager",
        "location": "Noida, India",
    }
]


@app.route("/")
def home():
    return render_template("home.html", jobs = JOBS)

@app.route("/api/jobs")
def jobsapi():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)