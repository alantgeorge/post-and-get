from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/read',methods=['GET','POST'])
def getname():
    if(request.method=='POST'):
        studentname=request.form.get('name')
        admissionno=str(request.form.get('addmno'))
        emailid=str(request.form.get('email'))
        mobileno=str(request.form.get('mobileno'))


        return "Name="+studentname+"addmno ="+admissionno+"email="+emailid+"mobileno="+mobileno

if(__name__=='__main__'):
    app.run()

