from flask import Flask, redirect, url_for, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Your_Password'
app.config['MYSQL_DB'] = 'Database_Name'
mysql = MySQL(app)

@app.route("/interface", methods=["POST", "GET"])
def interface():
    if request.method=="GET":
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM mars_iot_not_received")
        userDetails =cur.fetchall()

        cur1 = mysql.connection.cursor()
        resultValue1 = cur1.execute("SELECT * FROM mars_iot_not_prepare")
        userDetails1 =cur1.fetchall()

        if resultValue > 0 or resultValue1>0:  
            return render_template('users.html',userDetails= userDetails, userDetails1=userDetails1)  

    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("users.html")

@app.route("/<usr>", methods=["POST", "GET"])
def user(usr):
    alpha = f"{usr}"
    if request.method=="GET":
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM mars_iot_not_received where name =%s",[alpha])
        if resultValue > 0:  
            userDetails = cur.fetchall()
            return render_template('confirm_order.html',userDetails= userDetails)

    if request.method == "POST":

        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM mars_iot_not_received WHERE name =%s",[alpha])
        mysql.connection.commit()
        cur.close()

        user1 = request.form["nm3"]
        user2 = request.form["nm2"]
        user3 = request.form["nm1"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO mars_iot_not_prepare VALUES (%s,%s,%s)",[user1, user2, user3])
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("interface"))

if __name__ == "__main__":
    app.run(debug=True)


