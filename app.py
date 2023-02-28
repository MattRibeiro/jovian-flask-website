from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db
app = Flask(__name__)

# Stopped at 38 minutes, Lesson 4
# JOBS = [{
#   "id": 1,
#   "title": "Data Scientist",
#   "salary": 100000,
#   "location": "New York City"
# }, {
#   "id": 2,
#   "title": "Machine Learning Engineer",
#   "salary": 120000,
#   "location": "San Francisco"
# }, {
#   "id": 3,
#   "title": "Artificial Intelligence Researcher",
#   "salary": 150000,
#   "location": "Seattle"
# }, {
#   "id": 4,
#   "title": "Computer Vision Engineer",
#   "salary": 110000,
#   "location": "Boston"
# }, {
#   "id": 5,
#   "title": "Natural Language Processing Scientist",
#   "salary": 130000,
#   "location": "Chicago"
# }]
  
@app.route('/')
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  print(type(jobs))
  print(type(jobs[0]))
  return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Job Not Found", 404
  return render_template('jobpage.html', job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
