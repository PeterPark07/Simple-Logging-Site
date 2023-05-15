from flask import Flask, request

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def save_logs():
    log_data = request.get_data(as_text=True)

    with open('logs.txt', 'a') as f:
        f.write(log_data + '\n')

    return 'Log saved successfully'

def run():
    # Use Gunicorn as the production server
    from gunicorn.app.wsgiapp import run as run_gunicorn
    run_gunicorn(app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    run()
