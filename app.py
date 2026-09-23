from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        print("Confirm Password:", confirm_password)

        if password != confirm_password:
            return "Passwords do not match"

        return "Registration successful!"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)