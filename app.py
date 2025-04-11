
from flask import Flask, render_template, request
from microscope_calculator import calculate_real_size
from microscope_database import save_to_db, init_db

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        specimen_name = request.form["specimen"]
        microscope_size = float(request.form["microscope_size"])
        magnification = float(request.form["magnification"])

        actual_size = calculate_real_size(microscope_size, magnification)
        save_to_db(username, specimen_name, microscope_size, magnification, actual_size)
        result = f"Actual size of {specimen_name}: {actual_size:.4f} mm"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
