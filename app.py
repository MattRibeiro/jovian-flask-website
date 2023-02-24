from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Scientist",
  "salary": 100000,
  "location": "New York City"
}, {
  "id": 2,
  "title": "Machine Learning Engineer",
  "salary": 120000,
  "location": "San Francisco"
}, {
  "id": 3,
  "title": "Artificial Intelligence Researcher",
  "salary": 150000,
  "location": "Seattle"
}, {
  "id": 4,
  "title": "Computer Vision Engineer",
  "salary": 110000,
  "location": "Boston"
}, {
  "id": 5,
  "title": "Natural Language Processing Scientist",
  "salary": 130000,
  "location": "Chicago"
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company='Jovian')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
