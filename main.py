import os
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import pickle
import pred
#from random import randint

#imports for model pred
import numpy as np
import pandas as pd
pd.set_option('max_columns', None)

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC, SVC
#imports for model pred end


app = Flask(__name__)
app.secret_key = "abc"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.csv', '.xlsx']
#app.config['UPLOAD_PATH'] = '/' 


#uploader
@app.route('/', methods=['GET', 'POST'])
def index():
    #file_name = ""
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        #file_name+=filename
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(filename))
            #var = "File Uploaded Successfully"
            res = pred.pred2(filename)
            os.remove(filename)
            return render_template('index.html', res = res)
        else:    
            return render_template('index.html', msg = "File Upload Failed. Please Try Again!")
    return render_template('index.html', msg = "File not uploaded. Please upload a csv file.")

#Page2
'''
@app.route("/page2")
def page2():
    return "Hello, Welcome to Page2"
'''   

if __name__ == "__main__":
    app.run(debug=True)