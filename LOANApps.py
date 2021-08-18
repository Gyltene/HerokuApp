from flask import Flask,render_template,request,redirect
import pickle
import pandas as pd
import numpy as np
model=pickle.load(open('LoanModel.pkl','rb'))
app=Flask(__name__,template_folder='./')
@app.route('/',methods=['GET','POST'])
def LOAN():
    return render_template('LOAN.html')
@app.route('/predict',methods=['GET','POST'])
def Predict():
    ApplicantIncome=request.form['ApplicantIncome']
    CoapplicantIncome=request.form['CoapplicantIncome']
    ApplicantIncome=request.form['ApplicantIncome']
    Loan_Amount_Term=request.form['Loan_Amount_Term']
    Credit_History=request.form['Credit_History']
    Property_Area=request.form['Property_Area']
    columns=np.array([[ApplicantIncome,CoapplicantIncome,ApplicantIncome, Loan_Amount_Term,  Credit_History,Property_Area]])
    
    prediction=model.predict(columns)
    
    prediction1=np.where(prediction>0,"Aprovohet","Nuk Aprovohet")
    prediction2=str(prediction1)
    prediction3=prediction2[2:-2]
    
    return render_template('LOAN.html',prediction_text='Statusi i Kredise:{}'.format(prediction3))

if __name__ == '__main__':
 app.run(debug=True)

