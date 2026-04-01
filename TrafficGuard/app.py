from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 🔹 Login Page
@app.route('/')
def login():
    return render_template("loginpage.html")


# 🔹 Dashboard (Officer)
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# 🔹 Citizen Dashboard
@app.route('/citizen-dashboard')
def citizen_dashboard():
    return render_template("citizen-dashboard.html")


# 🔹 Report Violation (Officer side)
@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        plate = request.form.get('plate')
        violation = request.form.get('violation')

        print("Plate:", plate)
        print("Violation:", violation)

        return redirect('/dashboard')

    return render_template("reportviolation.html")


# 🔹 Emergency Page
@app.route('/emergency')
def emergency():
    return render_template("emergency.html")


# 🔹 Citizen Violations Page
@app.route('/citizen-violations')
def citizen_violations():
    return render_template("citizen-violations.html")


# 🔹 Payment Page
@app.route('/citizen-payment')
def payment():
    return render_template("citizen-payment.html")


# 🔹 Profile Page
@app.route('/citizen-profile')
def profile():
    return render_template("citizen-profile.html")


# 🔹 Run App
if __name__ == "__main__":
    app.run(debug=True)