import flask
import os
from flask import send_from_directory

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home_(a,b):
    sum_=a+b
    return sum_

if __name__ == "__main__":
    a=6
    b=7
    ad=home_(a,b)
    print(ad)
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
    





# import time
# #our function for counting from 0-20
# def counting():
#     for i in range(0,21):
#         if i==20:
#             print("counting at: "+str(i))
#             print("Done counting...")
#         else:
#             print("counting at: "+str(i))
#             time.sleep(1) #sleep for 5 seconds

# #our main function
# if __name__ == '__main__':
#     counting() #call our counting method