from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key='key'

# Displays all users
@app.route('/')
def index():
    users=User.get_all()
    return render_template("index.html", users=users)

# Show user
@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
    'id' : user_id
    }
    user = User.get_one(data)
    return render_template('show_user.html', user=user)


# Form to create new user
@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

# Creates user
@app.route('/create_user', methods=['POST'])
def create_user():
    User.create(request.form)
    return redirect('/')

# Edit User
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    data = {
        'id' : user_id
    }
    user = User.get_one(data)
    return render_template('edit_user.html', user=user)


# Update User
@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    data = {
    'id' : user_id,
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'email' : request.form['email']
    }
    User.update(data)
    return redirect('/')

# Delete user
@app.route('/delete/<int:user_id>/user')
def destroy(user_id):
    data = {
        'id' : user_id
    }
    User.destroy(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)