from flask import Flask, request

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def save_logs():
    log_data = request.get_data(as_text=True)

    with open('logs.txt', 'a') as f:
        f.write(log_data + '\n')

    return 'Log saved successfully'

# Uncomment the following lines if you want to run the app using gunicorn or a WSGI server
# def run():
#     app.run()

# if __name__ == '__main__':
#     app.run()

# Comment out the app.run() line above and uncomment the lines below if you want to run the app using gunicorn or a WSGI server
# if __name__ == '__main__':
#     run()
