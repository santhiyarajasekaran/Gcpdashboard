from flask import Flask, request, render_template, redirect, url_for, session
from google.cloud import storage

app = Flask(__name__)
app.secret_key = 'dev_key'  # Required for session management

# Google Cloud Storage config

storage_client = storage.Client(project='storied-box-460407-j5')

USERS = {
    'admin': {'password': 'password123', 'bucket': 'santhiya_bucket12'},
    'admin2': {'password': 'password1234', 'bucket': 'santhiya_bucket13'}
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = USERS.get(username)

        if user and user['password'] == password:
            session['logged_in'] = True
            session['username'] = username
            session['bucket'] = user['bucket']
            return redirect(url_for('upload_file'))
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    message = None
    if request.method == 'POST':
        if 'file' not in request.files:
            message = 'No file part'
        else:
            file = request.files['file']
            if file.filename == '':
                message = 'No selected file'
            else:
                bucket_name = session.get('bucket')
                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob(file.filename)
                blob.upload_from_file(file)
                message = f'✅ File "{file.filename}" uploaded successfully '

    return render_template('index.html', message=message)


if __name__ == '__main__':
    # Ensure the environment variable for the GCS service account key is set
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/service-account-file.json'
    app.run(debug=True)
#http://localhost:5000/