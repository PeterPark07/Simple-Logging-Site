from flask import Flask, request, render_template

app = Flask(__name__)

# File names
LOGS_FILE = 'logs.txt'
DATA_FILE = 'data.txt'

def write_to_file(filename, data):
    # Append data to the specified file.
    with open(filename, 'a') as f:
        f.write(data + '\n')

def read_file(filename):
    # Read the contents of the specified file.
    with open(filename, 'r') as f:
        return f.read()

@app.route('/logs', methods=['POST', 'GET'])
def logs():
    # Handle POST and GET requests for logs.
    if request.method == 'POST':
        # Write log data to logs file
        log_data = request.get_data(as_text=True)
        write_to_file(LOGS_FILE, log_data)
        return 'Saved successfully'
    else:
        # Read logs file and return its contents
        logs = read_file(LOGS_FILE)
        return logs

@app.route('/data', methods=['POST', 'GET'])
def data():
    # Handle POST and GET requests for data.
    if request.method == 'POST':
        # Write log data to data file
        log_data = request.get_data(as_text=True)
        write_to_file(DATA_FILE, log_data)
        return 'Saved successfully'
    else:
        # Read data file and return its contents
        data = read_file(DATA_FILE)
        return data

@app.route('/show', methods=['GET'])
def show():
    # Render the home page and display contents of logs and data files.
    logs = read_file(LOGS_FILE)
    data = read_file(DATA_FILE)
    return render_template('home.html', logs=logs, data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
