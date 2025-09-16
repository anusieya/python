from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name", "").strip() or "Guest"
        return render_template("hello.html", name=name)
    return render_template("hello_form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
