from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_bootstrap import Bootstrap
# from beatCount import 

# declare constants
HOST = '0.0.0.0'
PORT = 5000

beats = 0

# initialize flask application
app = Flask(__name__)
Bootstrap(app)

# sample hello world page
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")
  
@app.route('/resources/')
def resources():
    return render_template("resources.html")

#                                                actual app components
@app.route('/start/')
def start():
    return render_template("start.html")



#@app.route('/meditating/', methods=['GET', 'POST'])
@app.route('/meditating/')
def med():
  # if request.method == "POST":
  #   #beats = countBeats()
  #   return redirect(url_for("process"))
  return render_template("med.html")

# @app.route('/process/', methods=['GET', 'POST'])
# def process():
#   if request.method == "POST":
#     #if()
#     #beats = countBeats()
#     return redirect(url_for("process"))
#   return render_template("process.html")


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
    app.run(host=HOST, debug=True, port=PORT)
