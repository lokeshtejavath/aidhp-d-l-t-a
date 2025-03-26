🚀 Banking Product Recommendation System 

## 📌 Table of Contents
- [Introduction](#🎯-introduction)
- [Demo](#🎥-demo)
- [Presentation](#🖼️-Screenshots) 
- [Inspiration](#💡-inspiration)
- [What-It-Does](#⚙️-what-it-does)
- [How-We-Built-It](#🛠️-how-we-built-it)
- [How-to-Run](#🏃-how-to-run)
- [Tech-Stack](#🏗️-tech-stack)
- [Team](#👥-team)

---

## 🎯 Introduction
A bank has a wealth of information about it's customers. This project aims to utilize said information to generate recommendations for new products that an existing/recently joined customer may be interested in.

We recommend product lines (from the major lines of business products WF has for retail customers: Accounts/Credit Cards/Deposits/Loans/Investments/etc.) that the customer will potentially be interested in, leveraging GenAI to generate personalized insights that can be used to form a more effective strategy to approach these potential customers. 

## 🎥 Demo 
📹 [Video Demo](https://drive.google.com/drive/folders/1GzQtuRuyRilDbH1sSKsiXE9sdYwZFQi_?usp=sharing)  drive link

📹 [Click here to watch the Demo Video](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/demo.mp4?raw=true)

## 🖼️ Screenshots:


[![Screenshot 1](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/first.jpg?raw=true)](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/first.jpg)

[![Screenshot 2](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/second.jpg?raw=true)](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/second.jpg)

[![Screenshot 3](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/third.jpg?raw=true)](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/third.jpg)

[![Screenshot 4](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/fourth.jpg?raw=true)](https://github.com/ewfx/aidhp-d-l-t-a/blob/main/artifacts/demo/fourth.jpg)
<!-- display the screenshots -->



## 💡 Inspiration
Financial products are a necessity for almost all individuals, and uniquely benefit all parties involved. Through them, customers are able to better manage their financial assets while also gaining the ability to achieve their overarching life-goals.

We believe that in today's world, the inefficiency of the financial industry in leveraging the data that they possess creates an opportunity to convert new customers given that these customers are approached with products specifically tailored to their lives, goals and characteristics. Often, institutions only recommend a generic set of widely-used financial products (like credit/deposits/savings accounts) to their mass retail-customer audience. This is contrary to the customer expectation of a personalized experience in today's highly data-driven user-centric world, and they therefore are less likely to respond to a telemarketer/an email about a Home Loan as opposed to a targeted Auto Loan when they're looking to purchase a vehicle. 

Leveraging the power of Recommender Systems to generate personalized insights, we believe we can exploit this opportunity to create a better and more targeted customer journey. 

## ⚙️ What It Does
### (Input):- 
Our project lets a user input any context they'd like our system to have for generating recommendations along with their unique user ID (In a production environment, both of these can be easily inferred from data about the user). 
### (Output):-
We generate 3 product lines that our system thinks will be of interest to the user based on the existing data we have, the context they've given us and their history of interactions with the bank at large. Alongside, we leverage genAI to explain our system's thinking, allowing our system to generate insights on why particularly a line of products may be of interest to a specific customer. 

## 🛠️ How We Built It
### Dataset:-
1. https://www.kaggle.com/competitions/santander-product-recommendation
2. https://www.kaggle.com/competitions/playground-series-s4e10
   
The first dataset contains a real-life record of all interactions of a bank's customers with their financial products, while the second contains synthetically generated data (based on a real-life dataset) of Loan Approval information. We leveraged this two datasets to model the information a financial institution may possess about their customers.

### Recommender:- 
We built an integrated recommendation system using TensorFlow and Google Gemini, training it using these two datasets on kaggle. Our model is based on a Deep Neural Network that uses vector embeddings to understand user behavior at scale, utilizing it to generate recommendations for future items that a user would likely interact with. On top of this, we utlize a genAI Gemini model to convert the information the our Neural Network has learned into textual form to generate insights about the decisions the system is making, leading to an integrated Reason + Recommendation output.

## 🏃 How to Run
Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidhp-d-l-t-a.git
   ```
### Backend
1. Navigate to the backend directory
   ```sh
   cd code/src/backend
   ```
2. Install the dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
   python main.py
   ```

### Frontend
1. Navigate to the frontend directory
   ```sh
   cd code/src/frontend
   ```
2. Install the dependencies  
   ```sh
   npm install
   ```
3. Run the project  
   ```sh
   npm start
   ```


## 🏗️ Tech Stack
- 🔹 Frontend: React 
- 🔹 Backend: Flask
- 🔹 Recommender: TensorFlow, Keras, XGBoost, Pandas, Kaggle

## 👥 Team
- Surendra Kancherla (Mentor)
- Aditya Srivastava - [GitHub](https://github.com/adisrivastava121) | [LinkedIn](https://www.linkedin.com/in/aditya-srivastava-73b28520b/)
- Stubh Lal - [GitHub](https://github.com/Artshouldterrify) | [LinkedIn](https://www.linkedin.com/in/stubh-lal-085597163/)
- Lokesh Tejavath - [GitHub](https://github.com/lokeshtejavath) | [LinkedIn](https://www.linkedin.com/in/lokeshtejavath/)
- Yukti Dahiya - [GitHub](https://github.com/YuktiDahiya) | [LinkedIn](https://www.linkedin.com/in/yukti-dahiya/)
- Surendra Babu Kancherla
