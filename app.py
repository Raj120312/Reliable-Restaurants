from flask import Flask,render_template,request
from flask_cors import cross_origin
import numpy as np
import pickle
import bz2
import _pickle as cPickle


# initializing the template folder for all the html files to look for
app = Flask(__name__, template_folder="template")

#loading decision tree model from models folder for predicting the success of the restaurant at a particular location
predict_success_model=pickle.load(open("./models/decision_tree_model.pkl","rb"))
print("predict_success_model_loaded")

#loading the rating_prediction model from models folder for predicting the rating of the restaurant
def decompress_pickle(file):
     data = bz2.BZ2File(file,"rb")
     data = cPickle.load(data)
     return data
data = decompress_pickle('./models/rating_prediction_me_compressed.pbz2')

predict_rating_model=data
#predict_rating_model=pickle.load(open("./models/rating_prediction.pkl","rb"))
print("predict_rating_model_loaded")


#setting the route for main homepage
@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")


#routing to predict_success_of_resto.html
@app.route("/predict_success_of_resto",methods=['GET', 'POST'])
def success():
    if request.method =="POST":
        arr=[]
        approx_cost_for_two_people = int(request.form['approx_cost_for_two_people'])
        arr.append(approx_cost_for_two_people)

        no_of_cuisines_offered = int(request.form['number_of_cuisines_offered'])
        arr.append(no_of_cuisines_offered)

        multiple_types_offered = int(request.form['multiple_types'])
        arr.append(multiple_types_offered)


        online_order = request.form['online_order']
        ol = [int(x) for x in str(online_order)]
        arr=arr+ol


        book_table = request.form['book_table']
        bt =[int(x) for x in str(book_table)]
        arr=arr+bt

        location = request.form['location']
        lo=[int(x) for x in str(location)]
        arr=arr+lo
        print(" the location is ",arr)

        restaurant_type=request.form['restaurant_type']
        rt=[int(x) for x in str(restaurant_type)]
        arr=arr+rt

        listed_in_type=request.form['listed_in_type']
        lit=[int(x) for x in str(listed_in_type)]
        arr=arr+lit

        listed_in_city=request.form['listed_in_city']
        lic=[int(x) for x in str(listed_in_city)]
        arr=arr+lic


        fin = [np.array(arr)]
        print(fin)

        prediction =predict_success_model.predict(fin)
        output=prediction

        danger=" Your restaurant might be in danger ";
        succ="High Chances of Restaurant to be successful ";

        if output == 0:
            return render_template("predict_success_of_resto.html",success=danger)

        else:
            return render_template("predict_success_of_resto.html",success=succ)

    return render_template('predict_success_of_resto.html')


# routing to predict_rating_of_resto.html
@app.route("/predict_rating_of_resto",methods=['GET','POST'])
def rating():
    if request.method == "POST":

        pr=[]

        Votes = int(request.form['votes'])
        pr.append(Votes)

        approx_cost_for_two_people = int(request.form['approx_cost_for_two_people'])
        pr.append(approx_cost_for_two_people)

        no_of_cuisines_offered = int(request.form['number_of_cuisines_offered'])
        pr.append(no_of_cuisines_offered)

        online_order = request.form['online_order']
        online = [int(x) for x in str(online_order)]
        pr = pr + online

        book_table = request.form['book_table']
        book = [int(x) for x in str(book_table)]
        pr = pr + book

        location = request.form['location']
        loc = [int(x) for x in str(location)]
        pr = pr + loc


        restaurant_type = request.form['restaurant_type']
        rtype = [int(x) for x in str(restaurant_type)]
        pr = pr + rtype


        final = [np.array(pr)]


        prediction = predict_rating_model.predict(final)


        output = round(prediction[0], 1)
        return render_template('predict_rating_of_resto.html', prediction_text='Your Rating is: {}'.format(output))


    return render_template('predict_rating_of_resto.html')


#routing to the dashboard.html page
@app.route("/dashboard",methods=['GET'])
@cross_origin()
def dash():
    return render_template("dashboard.html")


if __name__=='__main__':
    app.run(debug=True,port=5008)