# Home Credit Default Web App
## Project Description
This capstone project is to predict default risk of home loans for Home Credit Group. I have designed the data processing pipeline and reconstructed 59 million rows of telco and transactional data entries. These data were collected from financial institutions which were reported to Credit Bureau, balancing histories in Credit Bureau, previous cash loans, credit cards application records, and repayment history. Data wranglings including missing data handling, outlier detection, numerical features normalization, and one-hot encoding on categorical features. Matplotlib and Bokeh were applied to overview the missing features and to visualize distribution of the applicants age, loan types, genders, ownership of cars, education types, number of children, annual income and occupation types and the correlations with the default risk.  About 200 features were collected and reconstructed through merging collected information for applicants. Supervised learning algorithm LightGBM was chosen to train the model through parameters tuning. ROC under area at 0.78 was achieved to predict the test dataset provided by Home Credit Group. The trained model was re-trained with top 10 features. A bank-oriented app which predict loan default risk was developed and deployed on Google Cloud with the link at http://home-credit-215621.appspot.com/index

## About
This repository contains the essential code for a web app to check the risk of home credit default.

## Setup and Deploy
We deployed this app on Google Cloud.
- In Google Cloud, start a project say `home-credit`.
- Start the shell terminal in that project. Git clone this repository.
- Go to the directory of the repository. Start Python virtual environment by running: `
virtualenv --python python3 env
`
- Start the virtual environment: `source env/bin/activate`
- Install Python packages: `pip install -t lib -r requirements.txt`
- To run the app locally in the shell: `python main.app`
- To deploy the app: `gcloud app deploy app.yaml`
