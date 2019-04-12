# -*- coding:utf-8 -*-
import module.first.fun1st as f1
import module.Chapter2.c2 as c2
import module.Chapter3.c3 as c3

from module.Chapter8 import c8
from module.common import common as c

from module.TestCopy import Holly

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

stooge = "Curly"
print(stooge, "says:", quotes[stooge])

stock = Stock('2371')
# print(twstock.codes)

'''
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

import pathlib
# from pathlib import Path
tick_file = pathlib.Path(path_clean + '\Clean_Tick_' + str(year).zfill(4) + '_' + str(month).zfill(2) + '_' + str(day).zfill(2) + '.csv')

# Date, capacity, turnover, open, high, low, close, change, transaction
# DateTime String: %Y, %M, %D, %H, %M, %S
# this stock file already exist, so need to append.
if (tick_file.exist()):
	cleanTick = pd.read_csv(tick_file, encoding='big5', sep=r",")
	> last date

	cleanTick.to_csv('my_csv.csv', mode='a', header=False)

else:
	# check data is not empty
	if :

	else:
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

code = 2030

folder_path = pathlib.Path(c.stock_data_folder_path)
folder_path.mkdir(parents=True, exist_ok=True)
filename = folder_path / (str(code)+'.csv')


print(filename.exists())
new_data = Holly.test_temp(code)
# Holly.test_load_historical_data()

title = ["Date", "Capacity", "Turnover", "Open", "High", "Low", "Close", "Change", "Transaction"]
with open( fileName, 'w+', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(title)
	writer.writerows(new_data)