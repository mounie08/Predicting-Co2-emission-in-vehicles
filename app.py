from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import joblib
app=Flask(__name__)
model=pickle.load(open("CO2.pkl",'rb'))
LE=joblib.load('column2')
@app.route('/')
def home():
    return render_template('home1.html')
@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home1.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    Make = float(request.form["Make"])
    Vehicle_class = float(request.form["Vehicle_class"])
    Engine_Size = float(request.form["Engine_Size"])
    Cylinders = float(request.form["Cylinders"])
    Transmission = float(request.form["Transmission"])
    Fuel_Type = float(request.form["Fuel_Type"])
    Fuel_Consumption_City = float(request.form["Fuel_Consumption_City"])
    Fuel_Consumption_Hwy = float(request.form["Fuel_Consumption_Hwy"])
    Fuel_Consumption_Comb = float(request.form["Fuel_Consumption_Comb"])
    data=[[Make,Vehicle_class,Engine_Size,Cylinders,Transmission,Fuel_Type,Fuel_Consumption_City,Fuel_Consumption_Hwy,Fuel_Consumption_Comb]]
    x=model.predict(data)
    
    
    return render_template("resultnew1.html",y=x[0][0])
if __name__=="__main__": 
    app.run(host='0.0.0.0', port=5000)