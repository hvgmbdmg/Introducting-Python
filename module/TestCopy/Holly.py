"""
Docstring
----------

TODO List
----------
1. Add new function to check local data file format.
2. Add new function to
"""
import csv
import time
import pathlib
import datetime
from twstock import Stock
from ..common import common as c # Should adjust

def test_load_historical_data_gradually(code, begin_year, end_year):
    """
    Goal
    ----------
    Gradually download historical data.

    Parameters
    ----------
    code : int or str
    begin_year : int
    end_year : int
    """
    for year in range(begin_year, end_year+1):
        test_load_historical_data(code, year, 1, year, 12)


def test_update_data_until(code, end_year, end_month):
    """
    Goal
    ----------
    Update data until end date.

    Parameters
    ----------
    code : int or str
    end_year : int
    end_month : int

    Return
    ----------
    bool
    """
    if not test_is_local_data_exist(code):
        return False
    date_str = test_get_local_date_last_date(code)
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    test_load_historical_data(code, date_obj.year, date_obj.month, end_year, end_month)
    return True


def test_load_historical_data(code, begin_year, begin_month, end_year, end_month):
    """
    Goal
    ----------
    Generally download historical data.

    Parameters
    ----------
    code : int or str
    begin_year : int
    begin_month : int
    end_year : int
    end_month : int

    Return
    ----------
    bool

    TODO List
    ----------
    ...
    """
    # Ex. 2015 09 - 2016 02
    # Ex. 2015 09 - 2017 02
    data_list = []
    if begin_year < end_year:
        new_data = test_load_historical_data_months(code, begin_year, begin_month, 12)
        data_list.extend(new_data)

    if begin_year+1 < end_year:
        new_data = test_load_historical_data_years(code, begin_year+1, end_year-1)
        data_list.extend(new_data)

    if begin_year < end_year:
        new_data = test_load_historical_data_months(code, end_year, 1, end_month)
        data_list.extend(new_data)
    else: # begin_year == end_year
        new_data = test_load_historical_data_months(code, end_year, begin_month, end_month)
        data_list.extend(new_data)

    if not data_list:
        print('資料是空的 or 沒有新的資料')
        return False

    if test_is_local_data_exist(code):
        data_list = test_remove_duplicate_data(code, data_list)
        test_update_save_data(code, data_list)
    else:
        test_create_new_data(code, data_list, c.title)
    return True


def test_load_historical_data_months(code, year, begin_month, end_month):
    """
    Goal
    ----------
    Download historical data and basic unit is one month.

    Parameters
    ----------
    code : int or str
    year : int
    begin_month : int
    end_month : int

    TODO
    ----------
    1. Thinl trade suspension case
    2.
    """
    data_list = []
    if begin_month > end_month:
        return data_list

    stock = Stock(str(code))
    print("\n[" + str(code) + "]")
    for month in range(begin_month, end_month+1):
        time.sleep(5)
        stock.fetch(year, month)
        print(str(year) + '/' + str(month) + '   \tfinish')

        for index in range(len(stock.data)):
            new_data = list(stock.data[index])
            new_data[0] = stock.data[index][0].strftime("%Y-%m-%d %H:%M:%S")
            data_list.append(new_data)
        #if (month) --- check is empty?
        # 也有可能是停牌
        # 回傳錯誤，並說明原因
    return data_list


def test_load_historical_data_years(code, begin_year, end_year):
    """
    Goal
    ----------
    Download historical data and basic unit is one year.

    Parameters
    ----------
    code : int or str
    begin_year : int
    end_year : int
    """
    data_list = []
    if begin_year > end_year:
        return data_list

    for year in range(begin_year, end_year+1):
        new_data = test_load_historical_data_months(code, year, 1, 12)
        data_list.extend(new_data)
    return data_list


def test_get_local_date_last_date(code):
    """
    Goal
    ----------
    Get last date in local data

    Parameters
    ----------
    code : int or str

    Notice
    ----------
    1. If row is empty, this function will crash.
    """
    folder_path = pathlib.Path(c.stock_data_folder_path)
    filename = str(code)+'.csv'
    file_path = folder_path / filename

    with file_path.open(mode='r', newline='') as csv_obj:
        rows = csv.reader(csv_obj)
        for row in rows:
            last_date = row[0]

    return last_date


def test_is_local_data_exist(code):
    """
    Goal
    ----------
    For readability

    Parameters
    ----------
    code : int or str
    """
    folder_path = pathlib.Path(c.stock_data_folder_path)
    filename = str(code)+'.csv'
    file_path = folder_path / filename

    return file_path.exists()


def test_remove_duplicate_data(code, data_list):
    """
    Goal
    ----------
    Reomve already be save in the local file data.

    Parameters
    ----------
    code : int or str
    data_list : list of securities structure
    """
    unique_data_list = []
    date_str = test_get_local_date_last_date(code)
    for index in range(len(data_list)):
        if data_list[index][0] > date_str:
            unique_data_list.append(data_list[index])
    return unique_data_list


def test_create_new_data(code, data_list, title):
    """
    Goal
    ----------
    Create file and save data.

    Parameters
    ----------
    code : int or str
    data_list : list of securities structure
    title : list of str

    TODO List
    ----------
    1. save mode
    """
    folder_path = pathlib.Path(c.stock_data_folder_path)
    filename = str(code)+'.csv'
    file_path = folder_path / filename
    # Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
    with file_path.open(mode='w+', newline='') as csv_obj:
        writer = csv.writer(csv_obj)
        writer.writerow(title)
        writer.writerows(data_list)


def test_update_save_data(code, data_list):
    """
    Goal
    ----------
    Save append data.

    Parameters
    ----------
    code : int or str
    data_list : list of securities structure
        data_list should be clean and no repeat data

    TODO List
    ----------
    1. check title
    2. save mode
    """
    folder_path = pathlib.Path(c.stock_data_folder_path)
    filename = str(code)+'.csv'
    file_path = folder_path / filename

    with file_path.open(mode='a+', newline='') as csv_obj:
        writer = csv.writer(csv_obj)
        writer.writerows(data_list)
