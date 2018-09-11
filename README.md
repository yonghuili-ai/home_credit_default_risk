This capstone project is to predict default risk of home loans for Home Credit Group. I have designed the data processing pipeline and reconstructed 59 million rows of telco and transactional data entries. These data were collected from financial institutions which were reported to Credit Bureau, balancing histories in Credit Bureau, previous cash loans, credit cards application records, and repayment history. Data wranglings including missing data handling, outlier detection, numerical features normalization, and one-hot encoding on categorical features. Matplotlib and Bokeh were applied to overview the missing features and to visualize distribution of the applicants age, loan types, genders, ownership of cars, education types, number of children, annual income and occupation types and the correlations with the default risk.  About 200 features were collected and reconstructed through merging collected information for applicants. Supervised learning algorithm LightGBM was chosen to train the model through parameters tuning. ROC under area at 0.78 was achieved to predict the test dataset provided by Home Credit Group. The trained model was re-trained with top 10 features. A bank-oriented app which predict loan default risk was developed and deployed on Google Cloud with the link at http://home-credit-215621.appspot.com/index

# Step 1: Pre-processing Data


# Step 2: Train with Lightgbm


# Step 3: Predict with top 10 features


# Step 4: API on Google Cloud
