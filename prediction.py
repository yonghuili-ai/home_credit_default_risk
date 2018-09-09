""" 
this file used pre-trained lgb supervised algorithm on merged datasets from kaggle ...
to predict loan applications default rate
"""
import pandas as pd
import pickle

# Convert all user input to 0-1 for model training 
def convert_input(dict,new_df):
    out_dict = {}
    for k,v in dict.items():
        X_min = new_df.at[k,'min']
        X_max = new_df.at[k,'max']
        X_std = (v - X_min) / (X_max-X_min)
        out_dict[k]=X_std
    return out_dict


def predict(input_dict):
	new_df = pd.read_csv('new_df.csv')
	new_df.set_index('Unnamed: 0',inplace=True)
	user_input = convert_input(input_dict,new_df)
	filename = 'finalized_est_top.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	onerow = pd.DataFrame(data=user_input,index=[0])
	return loaded_model.predict(onerow)
	

#test_dict={'AMT_ANNUITY': 2000,
# 'AMT_CREDIT': 500000,
# 'AMT_GOODS_PRICE': 80000,
# 'DAYS_BIRTH': -15000,
# 'DAYS_EMPLOYED': 20000,
# 'DAYS_ID_PUBLISH': -3000,
# 'EXT_SOURCE_2': 1.5,
# 'EXT_SOURCE_3': 0.3,
# 'i_AMT_PAYMENT': 800000,
# 'pc_CNT_INSTALMENT_FUTURE': 30}
# predict
