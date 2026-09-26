from flask import Flask, render_template

app = Flask(__name__)

# Static route
@app.route("/")
def home():
    return render_template("index.html")


# Dynamic route
@app.route("/order/<order_id>")
def order(order_id):
    return render_template("index.html", order_id=order_id)


if __name__ == "__main__":
    app.run(debug=True)