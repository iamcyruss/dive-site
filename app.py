from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('home.html')

@app.route('/about')
def about():
        return render_template('about.html')

@app.route('/contact')
def contact():
        return render_template('contact.html')

@app.route('/destinations')
def destinations():
        return render_template('destinations.html')

@app.route('/indonesia')
def indonesia():
        return render_template('indonesia.html')

@app.route('/maldives')
def maldives():
        return render_template('maldives.html')

@app.route('/galapagos')
def galapagos():
        return render_template('galapagos.html')

@app.route('/french-polynesia')
def french_polynesia():
        return render_template('french-polynesia.html')

@app.route('/papua-new-guinea')
def papua_new_guinea():
        return render_template('papua-new-guinea.html')

@app.route('/fiji')
def fiji():
        return render_template('fiji.html')

if __name__ == '__main__':
    app.run(debug=True)
