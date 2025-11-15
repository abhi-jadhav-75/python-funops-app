from flask import Flask, render_template, request, redirect, url_for, flash
import pathlib

app = Flask(__name__)
app.secret_key = "change-me-to-a-random-secret"  # replace for production

DATA_DIR = pathlib.Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
SUBSCRIBERS_FILE = DATA_DIR / "subscribers.txt"

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email", "").strip()
    if not email:
        flash("Please enter a valid email.", "error")
        return redirect(url_for("home"))
    # Simple append to a file (for demo). Replace with DB/email service in prod.
    with open(SUBSCRIBERS_FILE, "a", encoding="utf-8") as f:
        f.write(email + "\n")
    flash("Thanks! You're on the FunOps list 🎉", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

