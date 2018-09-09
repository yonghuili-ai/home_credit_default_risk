#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
import requests
import numpy as np
import pandas as pd
import bokeh
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.embed import components
from prediction import predict
bv = bokeh.__version__


# # app Flask
# -----------------------------------------------------|
app = Flask(__name__)
app.vars={}


@app.route('/')
def main():
	return redirect('/index')
	
@app.route('/visual')
def visual():
	return render_template('edu_occup_income.html')

@app.route('/form', methods=['GET','POST'])g
def form():
	if request.method == 'GET':
		return render_template('form.html')
	else:
		input_dict = {}
		#request was a POST
		input_dict['AMT_ANNUITY'] = float(request.form['amt_annuity'])
		input_dict['AMT_CREDIT'] = float(request.form['amt_credit'])
		input_dict['AMT_GOODS_PRICE'] = float(request.form['amt_goods_price'])
		input_dict['DAYS_BIRTH'] = float(request.form['days_birth'])
		input_dict['DAYS_EMPLOYED'] = float(request.form['days_employed'])
		input_dict['DAYS_ID_PUBLISH'] = float(request.form['days_id_publish'])
		input_dict['EXT_SOURCE_2'] = float(request.form['ext_source_2'])
		input_dict['EXT_SOURCE_3'] = float(request.form['ext_source_3'])
		input_dict['i_AMT_PAYMENT'] = float(request.form['i_amt_payment'])
		input_dict['pc_CNT_INSTALMENT_FUTURE'] = float(request.form['pc_cnt_instalment_future'])
#		print(input_dict)
#		print(predict(input_dict))
		
		try: 
			app.vars['result'] = predict(input_dict)[0]
		except ValueError: 
			pass
#			app.vars['start_year'] = ''
#			app.vars['tag'] = 'Start year not specified/recognized'
#		app.vars['select'] = [feat[q] for q in range(3) if feat[q] in request.form.values()]
		return redirect('/result')

@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/result',methods=['GET','POST'])
def result():
	if 0.5<= app.vars['result']:
		result_default = "High Dafault Risk"
	else:
		result_default = "Low Default Risk"
	
	return render_template('result.html', result=result_default)
		
	
@app.errorhandler(500)
def error_handler(e):
	return render_template('error.html')
    
if __name__ == '__main__':
  app.run(port=33509,debug=False)
