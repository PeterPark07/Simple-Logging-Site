from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def save_logs():
    log_data = request.get_data(as_text=True)

    with open('logs.txt', 'a') as f:
        f.write(log_data + '\n')

    return 'Log saved successfully'

@app.route('/logs', methods=['GET'])
def get_logs():
    if not os.path.exists('logs.txt'):
        return 'No logs available'

    with open('logs.txt', 'r') as f:
        logs = f.read()

    return logs

@app.route('/show', methods=['GET'])
def home():
    if not os.path.exists('logs.txt'):
        # Create the file if it doesn't exist
        with open('logs.txt', 'w') as f:
            pass

    with open('logs.txt', 'r') as f:
        logs = f.read()

    return render_template('home.html', logs=logs)

if __name__ == '__main__':
    # Use Gunicorn as the production server
    from gunicorn.app.wsgiapp import run as run_gunicorn
    run_gunicorn(app, host='0.0.0.0', port=5000)
