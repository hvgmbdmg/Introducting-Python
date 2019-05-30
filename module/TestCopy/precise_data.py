"""
Docstring
----------

TODO List
----------
1. 計算增減資 + 配股/息
"""
import pandas as pd

def read_csv_to_pandas(code):
	"""
    Goal
    ----------
    Gradually download historical data.

    Parameters
    ----------
    code : int or str
    begin_year : int
    end_year : int

    Return
    ----------
    security_df : pandas.core.frame.DataFrame
    """
    folder_path = pathlib.Path(c.stock_data_folder_path)
    filename = str(code)+'.csv'
    file_path = folder_path / filename
    security_df = pd.read_csv(file_path) # class 'pandas.core.frame.DataFrame'

    return security_df


def cal_reasonable(last_close, refund, distribute_equity, capital_reduce):
	"""
    Goal
    ----------
    Calculate resonable price.
	Dividend per share
	# 增資不該影響price

    Parameters
    ----------
    code : int or str
    begin_year : int
    end_year : int
    """

    reasonable_price = (last_close-refund) / (1+distribute_equity/10)
    equity = 1+distribute_equity/10;

	'''
    if capital_reduce != 0:
    	...
    	...

	''' 
    return [reasonable_price, equity, refund]


def simple_moving_average(txdf, period):

	newColumn = str(period) + "MA"
    txdf[newColumn] = txdf["Close"].rolling(period).mean()


"""
可嘗試交易量加權移動平均
"""
def weighted_moving_average(txdf, period):
	newColumn = str(period) + "WMA"
	txdf['weighted_close'] = txdf['Close']*txdf['Turnover']
	txdf['weighted_count'] = txdf["weighted_close"].rolling(period).mean()
	txdf['Turnover_count'] = txdf["Turnover"].rolling(period).mean()
    txdf[newColumn] = txdf['weighted_count']/txdf['Turnover_count']

	# del txdf['weighted_close']
	# del txdf['weighted_count']
	# del txdf['Turnover_count']

# def exponential_moving_average():

# 減資後的股價=(減資前最後交易日收盤價－每股退還金額）/（減資後資本額/原資本額）

'''
NYSE:紐約證交所
SEC：美國證券交易委員會
London Stock Exchange:倫敦證券交易所
NASDAQ:美國納斯達克 世界最大的證券交易
CBOE:世界上最大的期權交易所

After-hours Deal:盤後交易
Annual Report:年報
Balance Sheet:資產負債表
Bargain:股票交易 如: Stock and bill bargain的中文意思：股票與證券交易
Bearer Stocks:不記名股票
Bed and Breakfast Deal:隔日交易
Bellwether stock:代表目前市場的指標股
Bid Price:買入價
Blue Button:股票交易員
Blue Chip:藍籌股 知名公司的股票統稱
Book Value:帳面價值
Bond fund :債券型基金
Bond Index:債券指數 
Bond market:債券市場 
Broker:股票、證券經紀人
Bull:牛市 表示市場情況良好
Bubble economyL泡沫經濟 
Call:買權
Call warrant:認購權證 
Capital:公司資本額
Capital reduction:減資 
Cash capital increase:增資 
Cash Settlemnet :現金結算、沖算
Carrying value:帳面價值
Cash earnings per share: EPS 每股現金盈餘 
Certificate of deposit:存款證明 
CFO (Chief Financial Officer) :財務總監 
Clearing marginl:結算保證金 
Closing price:收盤價 
Commission Fee:折讓手續費
Common stock:普通股
Corporate Bond:公司債
Convertible Bond :可轉換公司債 
Contract Note: 確認交易
Credit accounts:信用帳戶
Credit Default Swap:違約交割
Credit rating:信用評等 
Coupon: 固定股息
Cumulative Dividend: 股息政策
Day-trading 當日沖銷(當沖)
Default fine 違約金
Default interest:違約利息
Depositary receipt 存託憑證
Daily pricing / Price Fluctuation Limit:當日漲跌幅 
Dawn Raid: 開盤交易
Dealing: 處理購買、出售股份交易
Debenture: 債權股票證券
Depreciation: 折舊
Dividend: 股息;股利
Emerging stock:興櫃股票 
Employee stock option certificates :員工認股權憑證
Equities:股本、股權
Equity fund 
Ex-dividend:除息
Financial Advisor:財務顧問 
Final Dividend:期未分紅
Futures:期貨
Gross Spread:價差
Hedge Fund : 對沖基金
Inflation : 通貨膨脹 
Initial Public Offering:IPO 首次發行股票
Limit Order: 限價交易
Liquidation:清算
Loan Stock:債券市場
Merge&Acquisitions :公司合併或併購
Nominee:代理人 
Offer Price:出價 
Options:選擇權
Ordinary Share:普通股
Over the Counter Market (OTC):櫃檯市場 
Option premium 權利金 
PLC: Public Limited Company 公開發行公司
Portfolio:投資組合
Proxy:股東會代理
P/E Ratio:本益比 
Put option:賣權 
Stock Warrants: 個股權證
Security Lending:借券 
Shareholder Meeting:股東會
Shell company:空殼公司 
Short Sale 放空 
Stock loan 融券
StockBroker 股票經記人
Stop loss limit停損點

Value investment價值投資 
Yearlings: 政府公債
Yield:收益

 ---------------------------------------------------

股東會或法說會常見簡報英文

營業收入淨額- Net Revenue 
營業毛利率 -Gross Margin 
營業費用- Operating Expenses 
營業淨利率 -Operating Margin 
營業外收入及支出 -Non-Operating Items 
歸屬予母公司業主之本期淨利 -Net Income to Shareholders of the Parent Company 
純益率 -Net Profit Margin
每股盈餘- EPS 
股東權益報酬率 -ROE


Selected Items from Balance Sheets -資產負債表項目

Key Indices- 重要財務指標
A/R Turnover Days -平均收現日數
Inventory Turnover Days -平均銷貨日數 
Current Ratio (x)-流動比率 (倍) 
Asset Productivity (x)-資產生產力(倍)

Total Shareholders' Equity -股東權益總計

Total Assets -負債總計
Current Liabilities -流動負債
Long-term Interest-bearing Debts- 長期計息負債
Total Liabilities -資產總計

Cash & Marketable Securities -現金及有價金融商品投資
Accounts Receivable -應收帳款
Inventories -存貨
Long-term Investments- 長期投資
Net PP&E -不動產、廠房及設備 
'''


'''
https://stackoverflow.com/questions/3430372/how-to-get-full-path-of-current-files-directory-in-python
If you mean the directory of the script being run:

import os
os.path.dirname(os.path.abspath(__file__))

If you mean the current working directory:

import os
os.getcwd()
'''