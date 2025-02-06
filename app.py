from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded username and password (for simplicity)
USERNAME = "mylesd"
PASSWORD = "121723"

@app.route("/")
def home():
    """Render the login page."""
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    """Handle login requests."""
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        # Redirect to your Framer website
        return redirect("https://dazzled-seat-711783.framer.app/newpage")
    else:
        # Show an error message
        return render_template("login.html", error="Invalid username or password.")

if __name__ == "__main__":
    app.run(debug=True)