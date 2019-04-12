from ..common import common as c
from twstock import Stock
import pathlib
import time

def introduction():
	print("introduction".title().center(50)+'\n'+'-'*50)
	introduction = 'Hi Dear,\nI\'m Chapter 8.\nData Has to Go Somewhere.'
	print(introduction)
	c.function_end()



#def test_


def test_load_historical_data(code, begin_year, begin_month, end_year, end_month): 
	"""
	Intruction ...

	Parameters
	----------
	filename : str
		Description of parameter `filename`.
	copy : bool
	dtype : data-type
	iterable : iterable object
	shape : int or tuple of int
	files : list of str

	Return
	----------
	...


	TODO List
	----------
	1. get last date
	2. check end date is valid
	3. 
	...

	n. Call months, years, months
	n+1. Call save file

	"""


def test_load_historical_data_months(code, year, begin_month, end_month):
	"""
	Parameters
	----------
	code : int or str
	year : int
	begin_month : int
	end_month : int

	"""
	if begin_month > end_month:
		return []
	stock = Stock(str(code))
	for month in range(begin_month, end_month+1):
		time.sleep(2)
		stock.fetch(year, month)
		#if (month) --- check is empty?
		# 也有可能是停牌
		# 回傳錯誤，並說明原因

	return ...


def test_load_historical_data_years(code, begin_year, end_year):
	"""
	Parameters
	----------
	code : int or str
	begin_year : int
	end_year : int
	"""
	if begin_year > end_year:
		return []

	for year in range(begin_year, end_year+1) :
		test_load_historical_data_months(code, year, 1, 12)


def test_get_local_date_last_date(code):
	# 檔案存在就是有資料，因為如果沒資料是不會創建檔案的
	a = c.stock_data_folder_path + '\\' + str(code) + '.csv'

	with open( fileName, 'r', newline='') as csvObj:
		rows = csv.reader(csvObj)
		for row in rows:
			lastDate = row[0]


def test_is_local_data_exist(code):
	tick_file = pathlib.Path(c.stock_data_folder_path + str(code) + '.csv')


def test_temp(code):
	stock = Stock(str(code))
	stock.fetch(2012, 12)
	new_data = list(stock.data)
	return new_data
