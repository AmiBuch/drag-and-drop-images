# app.py
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)

@app.route('/')
def index():
    db.create_all()
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('files[]')
    for file in files:
        image = Image(data=file.read())
        db.session.add(image)
    db.session.commit()
    return jsonify({'message': 'Images uploaded successfully'})

if __name__ == '__main__':
    
    app.run(debug=True)
