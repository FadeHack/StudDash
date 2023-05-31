from flask import Flask, render_template, request, redirect, session, jsonify
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

uri = 'mongodb+srv://Temp_User:9BH1EM6p6LWStCxt@mongodatabase.ytbk03l.mongodb.net/?retryWrites=true&w=majority'

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
db = client['stud_dash']
users_collection = db['users']
assessments_collection = db['assessments']
results_collection = db['results']

@app.route('/')
def index():
    if 'username' in session:
        return render_template('dashboard.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']

    # Check user credentials from MongoDB
    user = users_collection.find_one({'username': username, 'password': password, 'role': role})

    if user:
        session['username'] = user['username']
        session['role'] = user['role']
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/create-assessment')
def create_assessment():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        return render_template('create_assessment.html')
    else:
        return redirect('/')

@app.route('/save-assessment', methods=['POST'])
def save_assessment():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        title = request.form['title']
        questions = request.form['questions']
        justification = request.form['justification']

        # Save assessment to MongoDB
        assessment = {
            'title': title,
            'questions': questions,
            'justification': justification
        }
        assessments_collection.insert_one(assessment)

        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/generate-reports')
def generate_reports():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        class_reports = results_collection.find()
        return render_template('class_reports.html', class_reports=class_reports)
    else:
        return redirect('/')



@app.route('/individual-reports')
def individual_reports():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        return render_template('individual_reports.html')
    else:
        return redirect('/')

@app.route('/search-results', methods=['POST'])
def search_results():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        username = request.form['username']
        result = results_collection.find_one({'username': username})

        if result:
            return render_template('view_results.html', results=[result])
        else:
            return render_template('no_results.html', username=username)
    else:
        return redirect('/')



@app.route('/view-assessments')
def view_assessments():
    if 'username' in session and session['role'] in ['admin', 'teacher']:
        assessments = assessments_collection.find()
        return render_template('view_assessments.html', assessments=assessments)
    else:
        return redirect('/')

@app.route('/take-assessment')
def take_assessment():
    if 'username' in session and session['role'] == 'student':
        assessments = assessments_collection.find()
        return render_template('take_assessment.html', assessments=assessments)
    else:
        return redirect('/')
    
@app.route('/get-assessment/<assessment_id>')
def get_assessment(assessment_id):
    assessment = assessments_collection.find_one({'_id': ObjectId(assessment_id)})
    if assessment:
        return jsonify({'assessment': {
            '_id': str(assessment['_id']),
            'title': assessment['title'],
            'questions': assessment['questions'],
            'justification': assessment['justification']
        }})
    else:
        return jsonify({'error': 'Assessment not found'})


@app.route('/submit-assessment', methods=['POST'])
def submit_assessment():
    if 'username' in session and session['role'] == 'student':
        assessment_id = request.form['assessment_id']
        answers = []

        # Collect the answers from the form data
        for key, value in request.form.items():
            if key.startswith('answer_'):
                answer_index = int(key.split('_')[1])
                answers.append(value)

        # Save student's answers to MongoDB
        result = {
            'username': session['username'],
            'assessment_id': assessment_id,
            'answers': answers
        }
        results_collection.insert_one(result)

        return redirect('/dashboard')
    else:
        return redirect('/')



@app.route('/view-results')
def view_results():
    if 'username' in session and session['role'] == 'student':
        results = results_collection.find({'username': session['username']})
        return render_template('view_results.html', results=results)
    else:
        return redirect('/')


@app.route('/add-users', methods=['GET', 'POST'])
def add_users():
    if 'username' in session and session['role'] == 'admin':
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']

            # Save user to MongoDB
            user = {
                'username': username,
                'password': password,
                'role': role
            }
            users_collection.insert_one(user)

            return redirect('/dashboard')
        else:
            return render_template('add_users.html')
    else:
        return redirect('/')


# Add other routes and functionalities as needed

if __name__ == '__main__':
    app.run(debug=True)
