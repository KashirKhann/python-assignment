from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)

@app.route('/')
def home():
    app.route('/')
    return render_template("home.html")

@app.route('/signup', methods = ['POST'])
def signup():
 email = mysql.connector.connect(user='root', password='',host='localhost',database='python')     
 mycursor = email.cursor()
 sql = "INSERT INTO product_order (name,street,city,accessory1,accessory2,accessory3,accessory4,payment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
 val = [
    (request.form['name'],request.form['street'],request.form['city'],request.form['accessory1'],request.form['accessory2'],request.form['accessory3'],request.form['accessory4'],request.form['payment'])
    ]

 mycursor.executemany(sql, val)
 mycursor.execute("SELECT * FROM product_order")
 data = mycursor.fetchall()
 email.commit()
 return render_template("about.html",data=data)

if __name__=="__main__":
    app.run(debug=True)

