from flask import Flask,render_template
app = Flask(__name__)

class Demo:
    def __init__(self):
        self.name="demo"
        


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/user/<name>')
def user(name):
    demo=Demo()
    return render_template("user.html",content=name,x=42,demo=demo)

if __name__ == '__main__':
    app.run(debug=True)