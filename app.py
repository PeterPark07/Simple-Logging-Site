from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def save_logs():
    log_data = request.get_data(as_text=True)

    with open('logs.txt', 'a') as f:
        f.write(log_data + '\n')

    return 'Log saved successfully'

@app.route('/logs', methods=['GET'])
def get_logs():
    with open('logs.txt', 'r') as f:
        logs = f.read()
        
    return logs

@app.route('/', methods=['GET'])
def home():
    with open('logs.txt', 'r') as f:
        logs = f.read()

    return render_template('home.html', logs=logs)

if __name__ == '__main__':
    # Use Gunicorn as the production server
    from gunicorn.app.wsgiapp import run as run_gunicorn
    run_gunicorn(app, host='0.0.0.0', port=5000)
