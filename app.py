from flask import Flask, render_template
app = Flask(__name__)

@app.route("/alfagrad")
def hello():
    one_tit = 'Строительство заборов'
    zaboru = 'заборы'
    # return "Hello World!"
    return render_template('index.html', one_tit=one_tit, zaboru=zaboru)

if __name__ == "__main__":
    app.run(debug=True)
