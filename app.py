from flask import Flask, render_template

app = Flask("webapp")

@app.route("/")
def home():
    return render_template("index.html", heading="Hello!")

if __name__ == "__main__":
    app.run(debug=True)