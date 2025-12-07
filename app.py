from flask import Flask, render_template, send_file
import json
import os

app = Flask(__name__)

def load_resume_data():
    with open('resume.json', 'r') as f:
        return json.load(f)

@app.context_processor
def inject_resume():
    return dict(resume=load_resume_data())

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
