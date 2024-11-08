from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the main HTML page

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
