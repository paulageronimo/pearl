from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_bootstrap import Bootstrap

# declare constants
HOST = '0.0.0.0'
PORT = 5000

# initialize flask application
app = Flask(__name__)
Bootstrap(app)

# sample hello world page
@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/start/')
# def startx():
#     return render_template("start.html")

@app.route('/resources/')
def resources():
    return render_template("resources.html")

@app.route('/about/')
def about():
    return render_template("about.html")

# sample api endpoint
@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # get parameters from post request
        parameters = request.get_json()
        if 'test' in parameters:
            return jsonify({'value': parameters['test']})
        return jsonify({'error'})
    else:
        return jsonify({'test': 'success'})


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
