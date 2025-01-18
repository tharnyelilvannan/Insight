from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')  # Your main page

@app.route('/debate/<topic_id>')
def debate(topic_id):
    # Fetch the topic by topic_id and assign perspectives
    # For now, a placeholder response
    return f"Debating Topic: {topic_id}"
