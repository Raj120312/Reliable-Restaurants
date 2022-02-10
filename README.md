# Reliable-Restaurants

A project on predicting the success and rating of the restaurant present at a particular location in Bengaluru based on Zomato restuarant dataset

This project is tested over lot of ml models like Decision Tree , Random Forest , Logistic Regression , Naive Bayes , K Nearest Neighbors(KNN), ExtraTree Regressor , Linear Regression etc .

For predicting the success of the restaurant at a particular location , Decision Tree worked best as it gave 83.01% accuracy which was highest among Random Forest , KNN , Logistic Regression, Naive Bayes

For predicting the rating of the restaurant , ExtraTree Regressor performed best giving the R2 score of 93.45% among Linear Regression and Random Forest.


 


# Tech Stack
* Front-End: HTML, CSS, Bootstrap
* Back-End: Flask
* IDE: Jupyter notebook, Pycharm

# How to run this app
* First create a virtual environment by using this command:
* conda create -n myenv python=3.8
* Activate the environment using the below command:
* conda activate myenv
* Then install all the packages by using the following command
* pip install -r requirements.txt
* Now for the final step. Run the app
* python app.py


# Workflow


[Zomato Dataset](https://www.kaggle.com/himanshupoddar/zomato-bangalore-restaurants) from Kaggle

Two Separate Jupyter Notebooks were created for predicting the success of the restaurant at particullar location and to predict the rating of the restaurant at a particular location . This was done because there was separate need of respective features for predicting the success and rating ,and based on that data preprocessing , feature engineering and models were developed.

Data Processing and feature engineering were done efficiently .
models like Decision Tree , Random Forest , Naive Bayes , KNN and logistic regression were  used for predicting the success of restaurant feature and Decision Tree Algorithm worked best as it gave 83.01% accuracy which is higher than the accuracy of rest of the models
For predicting the rating of the restaurant feature  ExtraTreeRegressor worked best as it gave R2 score of 93.45%.

Using pickle module .pkl files were generated for respective models .

A simple frontend web application was developed using html and css for taking inputs from the user.
Flask a module of python was used for integration purpose of the web application and .pkl files .
The respective inputs were then passed to the respective .pkl files  for prediction purpose .
.pkl files in return gave the predicted values .

This Entire system was deployed on Microsoft Azure which simplified the deployment process 
Major three services used in deploying the Web application are :-
1)App Service
2)App Service Plan
3)Network Watcher
4)Storage Plan

With the help of these 4 services The Machine Learning Web Application to predict the Success and Rating of the Restaurant at particular location was deployed successfully.
# If you like this project please do give a star. I am also giving my LinkedIn profile. If you want we can connect there too
https://www.linkedin.com/in/raj-parmar-1ba2b51a9/




