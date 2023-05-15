from flask import Flask, request

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def save_logs():
    log_data = request.get_data(as_text=True)

    with open('logs.txt', 'a') as f:
        f.write(log_data + '\n')

    return 'Log saved successfully'

if __name__ == '__main__':
    app.run()
