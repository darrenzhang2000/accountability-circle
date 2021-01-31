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


@app.route('/missioncategories')
def missionCategories():

    mission_categories = ["Health", "Tech Interviews", "Academics"]

    return render_template("missionCategories.html", mission_categories = mission_categories)


@app.route('/missionsetting')
def missionSetting():

    return render_template("missionSetting.html")


@app.route('/feedback')
def feedback():

    return render_template("feedback.html")


@app.route('/goaltables')
def goalTables():
    your_goals = [
        {
            "date": "01-30-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-07-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-14-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "02-21-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-01-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-07-2021",
            "goal": "Do 15 LeetCode questions"
        }
    ]


    partner_goals = [
        {
            "date": "01-30-2021",
            "goal": "Do 3 LeetCode questions"
        },
        {
            "date": "02-07-2021",
            "goal": "Do 3 LeetCode questions"
        },
        {
            "date": "02-14-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "02-21-2021",
            "goal": "Do 5 LeetCode questions"
        },
        {
            "date": "03-01-2021",
            "goal": "Do 10 LeetCode questions"
        },
        {
            "date": "03-07-2021",
            "goal": "Do 15 LeetCode questions"
        }
    ]

    return render_template("goalTables.html", your_goals = your_goals, partner_goals = partner_goals)


if __name__ == '__main__':
    app.run()
