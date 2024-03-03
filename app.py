from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id': 1,
  'position': 'Data Analyst',
  'location': 'Bangalore',
  'salary': '2000000'
},

{
  'id': 2,
  'position': 'Data scientist',
  'location': 'Bangalore',
  'salary': '9000000'
},


{
  'id': 3,
  'position': 'Backend Engineer',
  'location': 'Delhi',
  'salary': '1230000'
}


]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host = '0.0.0.0' , debug = True)


