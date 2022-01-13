from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/users/new')
def index():
    return render_template("users_new.html")

@app.route('/create_users', methods=['POST'])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect("/users")

@app.route('/users')
def users():

    users = User.get_all()
    print(users)

    return render_template("users.html", users=users)

if __name__=="__main__":
    app.run(debug=True)