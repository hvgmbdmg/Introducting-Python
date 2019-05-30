# -*- coding:utf-8 -*-
import module.first.fun1st as f1
import module.Chapter2.c2 as c2
import module.Chapter3.c3 as c3

from module.Chapter8 import c8
from module.common import common as c

from module.TestCopy import holly

from twstock import Stock
import pathlib
import twstock
import time
import datetime

# page 3 -- dictionary {key : value}
quotes = {
    "Moe": "A wiseguy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!"
}


'''
stooge = "Curly"
print(stooge, "says:", quotes[stooge])

stock = Stock('2371')
# print(twstock.codes)
twstock.__update_codes()

time.sleep(2)
stock.fetch(2015, 1)
for index in range(len(stock.data)):
	print(stock.data[index])
A = stock.data[0][0].strftime("%Y-%m-%d %H:%M:%S")
print(stock.data[0][0])
print(A)
print(stock.data[0][0].day)
print(type(stock.data[0][0]))


D = datetime.datetime.strptime(A, '%Y-%m-%d %H:%M:%S')
print(D)
print(type(D))
'''

'''
import pathlib
# from pathlib import Path
tick_file = pathlib.Path(path_clean + '\Clean_Tick_' + str(year).zfill(4) + '_' + str(month).zfill(2) + '_' + str(day).zfill(2) + '.csv')

	cleanTick = pd.read_csv(tick_file, encoding='big5', sep=r",")
	cleanTick.to_csv('my_csv.csv', mode='a', header=False)
'''


'''
f1.fun1()
#f1.fun2()

c2.introduction()
c2.test_operator()
c2.test_base()
c2.test_str()
c2.test_characters()
c2.test_split_join()
c2.test_str_long()
c2.test_align()
c2.test_replace()

c3.introduction()
'''

c8.introduction()
c8.test_write()

print(c.stock_data_folder_path)

# code = 2867
# holly.test_load_historical_data(code, 2018, 10, 2019, 4)
# holly.test_load_historical_data_gradually(2031, c.first_year, c.second_year)

# holly.test_load_historical_data_gradually(2867, 2000, 2018)
# holly.test_load_historical_data_gradually(2867, 2011, 2018)

'''
for item in c.securities_20MA:
	holly.test_load_historical_data_gradually(item, c.first_year, c.second_year)
'''

from FinMind.Data import Load
TaiwanStockInfo = Load.FinData(dataset = 'TaiwanStockInfo')
data = Load.FinData(dataset = 'TaiwanStockPrice',select = ['2425'],date = '2017-10-10')
# data = Load.FinData(dataset = 'TaiwanStockStockDividend',select = ['2425'],date = '2017-10-10')
print(data)