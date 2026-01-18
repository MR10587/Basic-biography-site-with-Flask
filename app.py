from flask import Flask, render_template
import os

# Set template and static folders to current directory
template_dir = os.path.abspath('.')
static_dir = os.path.abspath('.')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='')

@app.route('/')
def home():
    return render_template('insan.html')

@app.route('/haqqinda')
def biography():
    return render_template('haqqinda.html')

@app.route('/ugurlari')
def achievements():
    return render_template('ugurlari.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)