import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from xgboost import XGBClassifier
from sklearn.utils.class_weight import compute_class_weight


# initial model loads.
recommender_model = tf.keras.models.load_model('hackathon_model.keras')
a,b,c,d = XGBClassifier(), XGBClassifier(), XGBClassifier(), XGBClassifier()
a.load_model('hackathon_xgboost_model_0.model')
b.load_model('hackathon_xgboost_model_1.model')
c.load_model('hackathon_xgboost_model_2.model')
d.load_model('hackathon_xgboost_model_3.model')
xgb_models = [a,b,c,d]
pd.set_option('display.max_columns', None)
df_pivot = pd.read_csv("pivot.csv", index_col=False)
df_pivot_l = pd.read_csv("pivot_loan_info.csv")
df_pivot_loan = pd.get_dummies(df_pivot_l, columns=['Gender','Marital_Status','Dependents','Education','Employment_Status','Occupation_Type','Residential_Status'], dtype='float32')
df_pivot_loan = df_pivot_loan.drop(columns="Loan_Purpose")
df_pivot = df_pivot.drop(columns=["Unnamed: 0"])

# infer recommendation model - in the form of a rank list.
def infer_recommendations(cust_id=15889):
    cust_id = int(cust_id)
    row = df_pivot[df_pivot["Customer code"] == cust_id].drop(columns=["Customer code","Accounts","Investments","Credit Cards",
                                                                    "Loans","Short Term Deposit","Medium Term Deposit",
                                                                    "Long Term Deposit"])
    print(row)
    inputs = [np.array(cust_id).reshape(-1,1), row.to_numpy()]
    print(inputs, inputs[0].shape, inputs[1].shape)
    predictions = recommender_model.predict(inputs)
    print(predictions)
    mappings = ["Accounts","Investments","Credit Cards","Loans","Short Term Deposit","Medium Term Deposit","Long Term Deposit"]
    rank_dict = dict()
    ranked_indexes = np.argsort(predictions[0])[::-1]
    print(ranked_indexes)
    for i in range(7):
        rank_dict[ranked_indexes[i]] = mappings[i]
    return rank_dict

# infer xgboost model.
def infer_xgboost(cust_id=15906):
    cust_id = int(cust_id)
    row = df_pivot_loan[df_pivot_loan["Applicant_ID"] == cust_id].drop(columns=["Applicant_ID","Unnamed: 0","Loan_Approval_Status"])
    print(row)
    predictions = []
    for i in range(4):
        predictions.append(xgb_models[i].predict_proba(row.to_numpy())[0][1])
    print(predictions)
    mappings = ["Home","Auto","Personal","Educational"]
    rank_dict = dict()
    ranked_indexes = np.argsort(predictions)[::-1]
    print(ranked_indexes)
    for i in range(4):
        rank_dict[ranked_indexes[i]] = mappings[i]
    print(rank_dict)
    return rank_dict

# entire inference pipeline.
def infer(cust_id=15906):
    recom_dict = infer_recommendations(cust_id)
    ranked_suggestions = [recom_dict[i] for i in range(3)]
    loan_suggestions = []
    if "Loans" in ranked_suggestions:
        xgboost_dict = infer_xgboost(cust_id)
        loan_suggestions.append(xgboost_dict["Loan_Purpose"])
    return ranked_suggestions, loan_suggestions

# inference function for all the data we have on customer.
def customer_info(cust_id=15906):
    cust_id = int(cust_id)
    row_1 = df_pivot_l[df_pivot_l["Applicant_ID"] == cust_id].drop(columns=["Applicant_ID","Unnamed: 0","Loan_Approval_Status"])
    print(row_1)
    return row_1.to_dict()

# main
# c_id = 15906
# customer_info(c_id)
# r_suggestions, l_suggestions = infer(c_id)
# print(r_suggestions, l_suggestions)
