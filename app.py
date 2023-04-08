from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)