# app.py
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Olusola:<Olusola2013>@atlascluster.s4sm28s.mongodb.net/'  # Replace with your MongoDB URI
mongo = PyMongo(app)

def store_user_data(age, gender, income, expenses):
    user_data = {
        'age': age,
        'gender': gender,
        'income': income,
        'expenses': expenses
    }
    mongo.db.users.insert_one(user_data)

@app.route('/', methods=['GET', 'POST']
def survey_form():
    if request.method == 'GET':
        return render_template('survey.html')  # Render initial form
    elif request.method == 'POST':
        data = request.form
        age = int(data['age'])
        gender = data['gender']
        income = float(data['income'])
        expenses = {category: float(data.get(f'expenses_{category}', 0)) for category in ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']}
        store_user_data(age, gender, income, expenses)
        return render_template('survey.html')  # Correct if 'survey.html' exists in the 'templates' folder

@app.route('/visualize')
def visualize_data():
    user_data = mongo.db.users.find()
    df = pd.DataFrame(list(user_data))

    # Visualization 1: Ages with the highest income
    plt.figure(figsize=(10, 6))
    plt.bar(df['age'], df['income'])
    plt.xlabel('Age')
    plt.ylabel('Income')
    plt.title('Ages with the Highest Income')
    plt.savefig('static/ages_income.png')
    plt.close()

    # Visualization 2: Gender distribution across spending categories
    gender_expenses = df.groupby('gender').sum()[['expenses_utilities', 'expenses_entertainment', 'expenses_school_fees', 'expenses_shopping', 'expenses_healthcare']]
    gender_expenses.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.xlabel('Gender')
    plt.ylabel('Total Expenses')
    plt.title('Gender Distribution Across Spending Categories')
    plt.savefig('static/gender_expenses.png')
    plt.close()

    return render_template('visualize.html')

if __name__ == '__main__':
    app.run(debug=True
