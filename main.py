from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from beatCount import countBeats

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
@app.route('/start/', methods=['GET','POST'])
def start():
  return render_template("start.html")

#print(request.form)
@app.route('/meditating/', methods=['GET','POST'])
def med():
  if request.method == 'POST':
    #request.form
    # values=countBeats('https://open.spotify.com/track/6K4t31amVTZDgR3sKmwUJJ?si=S53B-lXPR9SFaku_RnzLsg', '4-4-8') 
    songURL = request.form['songURL']
    breathTechnique = request.form['breathTechnique']
    values=countBeats(songURL, breathTechnique)
    return render_template('med.html' ,inhale=values['inhale'], hold=values['hold'], exhale=values['exhale'])
  else:
    songURL = request.args.get['songURL']
    breathTechnique = request.args.get['breathTechnique']
    values=countBeats(songURL, breathTechnique)
    return render_template('med.html' ,inhale=values['inhale'], hold=values['hold'], exhale=values['exhale'])

#sample api endpoint
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
