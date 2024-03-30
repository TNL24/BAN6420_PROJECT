Utilising Survey Data to Analyse Spending and Income 
Summary of
The goal of this project is to create a survey instrument that will gather information from participants so that their income and spending patterns may be examined. With an emphasis on spending areas like utilities, entertainment, school fees, shopping, and healthcare, the tool will be used to collect user information such as age, gender, total income, and expenses. The gathered data will be analysed with Python, saved in a MongoDB database, and shown using Jupyter notebooks to provide insights. Furthermore, Amazon Web Services (AWS) will host the Flask application that houses the survey tool.
Components
1. Web Development with Flask
Simple webpage created using Flask to collect user data.
2. Data Storage with MongoDB
User details stored in MongoDB, including Age, Gender, Total Income, and Expenses.
Checkboxes provided for expense categories with corresponding textboxes to insert amounts spent.
3. Data Processing with Python
Python class named "User" created to handle user data.
Data collected from MongoDB looped through and stored in a CSV file.
4. Data Visualization
Jupyter notebook utilized for data visualization.
Visualizations include:
Ages with the highest income.
Gender distribution across spending categories.
Charts exported for use in a PowerPoint presentation for client use.
5. Deployment on AWS
Flask application hosted on Amazon Web Services (AWS) for accessibility.
Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/survey-tool.git
Set up MongoDB:

Install MongoDB on your system.
Configure MongoDB connection settings in the Flask application.
Install dependencies:

Copy code
pip install -r requirements.txt
Run the Flask application:

Copy code
python app.py
Access the survey tool in your web browser at http://localhost:5000.

Collect user data and check MongoDB for stored information.

Run the Python script to process data:

Copy code
python data_processing.py
Access the Jupyter notebook for data visualization:

Copy code
jupyter notebook
Open the notebook and run cells to generate visualizations.

Deploy the Flask application on AWS for production use.

Technologies Used
Flask
MongoDB
Python
Jupyter Notebook
Amazon Web Services (AWS)
