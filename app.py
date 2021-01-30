from flask import Flask, render_template, request, redirect, url_for
import pymongo
 
client = pymongo.MongoClient("mongodb+srv://testuser:testuser@cluster0.uqb77.mongodb.net/auth?retryWrites=true&w=majority")
db = client["users"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']

        user = db.users.find_one({"email": email, "password": password})
        print(user)
        if user != None:
            return redirect(url_for('secretPage'))
        else:
            print("Email doesn't exist for wrong password")

    return render_template("login.html")

@app.route('/secretPage')
def secretPage():
    return render_template("secret.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        confirmPassword = request.form['psw-repeat']
        
        if password == confirmPassword:
            isValidEmail =  True if db.users.find({"email": email}).count() == 0 else False
            if isValidEmail:
                try:
                    db.users.insert_one({
                        "email": email,
                        "password": password
                    })
                    print("User added")
                except:
                    print("Something went wrong")
            else:
                print("Email already exists")

    return render_template("register.html")



if __name__ == '__main__':
    app.run()
