def function_end(): 
	print('-'*50+'\n')

stock_data_folder_path = '.\DataSet\Securities\RawData'
# TWSE didn't provide load data before 2010
first_year = 2010
first_month = 1
second_year = 2018
second_month = 12

current_year = 2019
current_month = 5
title = ["Date", "Capacity", "Turnover", "Open", "High", "Low", "Close", "Change", "Transaction"]

securities_20MA = [3504, 6118, 6283]
# 1215, 2014, 2049, 2329, 2342, 2405, 2425, 2455, 2456, 2530, 2542, 2545, 3049, 3231, 3346, 3406, 
# 上櫃: 3430, 