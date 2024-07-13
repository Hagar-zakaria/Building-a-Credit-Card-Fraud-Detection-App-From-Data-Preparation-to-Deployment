# Building-a-Credit-Card-Fraud-Detection-App-From-Data-Preparation-to-Deployment
In this tutorial, we will walk through the process of creating a credit card fraud detection app using Python, Jupyter Notebook, and Streamlit. We will cover data preparation, model training, and deploying the app. By the end of this tutorial, you will have a fully functional web app that can predict credit card fraud based on transaction details.

# Table of Contents
1. Introduction
2. Data Preparation
3. Model Training
4. Building the Streamlit App
5. Running and Deploying the App
6. Conclusion

# 1. Introduction
Credit card fraud is a significant issue in the financial sector. Detecting fraudulent transactions is crucial to protect users and institutions. In this tutorial, we'll build a machine learning model to detect fraud and deploy it using Streamlit, a popular framework for building interactive web applications.

# 2. Data Preparation
We start by preparing the dataset. We'll use Jupyter Notebook to clean and preprocess the data.

## Step 1: Import Libraries and Load Data
First, import the necessary libraries and load the datasets.

![image](https://github.com/user-attachments/assets/dd8aa74c-7021-43e4-b07a-62a66f660ab2)

## Step 2: Handle Categorical Variables and Balance the Dataset
We encode the categorical variables and balance the dataset to handle the imbalance between fraudulent and non-fraudulent transactions.

![image](https://github.com/user-attachments/assets/57d472d2-fa79-4223-9a09-7142c477f3fc)

# 3. Model Training
Next, we train multiple machine learning models and select the best one based on performance.

## Step 1: Train Multiple Models
We will train various models and evaluate their performance using accuracy and confusion matrix.

![image](https://github.com/user-attachments/assets/0d92b687-f8da-4ef9-bb62-cf29a56cbb49)

## Step 2: Save the Best Model
We will save the best-performing model for deployment.

![image](https://github.com/user-attachments/assets/5d549889-e737-4d08-b68c-cf33d9619e8c)

# 4. Building the Streamlit App
Now, we build the Streamlit app to deploy our model and visualize the data.

## Step 1: Create app.py
Create a new file named app.py and add the following code:

![image](https://github.com/user-attachments/assets/ab96891c-9559-409d-8a50-b984ddebf0cc)


## Step 2: Ensure All Required Files Are in Place

Make sure your project directory contains app.py, best_model.pkl, and cleaned_data_with_lat_long.csv.

# 5. Running and Deploying the App
## Step 1: Install Required Packages
Open a terminal and navigate to your project directory. Install the required packages:

![image](https://github.com/user-attachments/assets/bef96aa1-f52b-4d2b-b454-91956525ee95)

## Step 2: Run the Streamlit App
In the terminal, navigate to the project directory and run the app:

![image](https://github.com/user-attachments/assets/24f3e875-6323-4cdc-be68-94ce7a402b9a)


# conclusion

By following these steps, you have successfully created and deployed a credit card fraud detection app using Python, Jupyter Notebook, and Streamlit. This app can predict fraudulent transactions and visualize fraud data across different categories and locations.

Feel free to customize and enhance this app further to suit your needs. Happy coding!
