from yahoofinancials import YahooFinancials
import pandas as pd
import json
from pandas import json_normalize
from tqdm import tqdm, trange


def GET_annual_FILE(dataType , stockCode , stockName , currency , financial_stmts):
    sheet_name = stockCode + '-' + currency + '-' + stockName
    yahoo_financials = YahooFinancials(stockCode)
    if dataType == 'IS': statement_data_qt = yahoo_financials.get_financial_stmts('annual', 'income' )
    if dataType == 'CF': statement_data_qt = yahoo_financials.get_financial_stmts('annual', 'cash' )
    if dataType == 'BS': statement_data_qt = yahoo_financials.get_financial_stmts('annual', 'balance' )
    dict_list = statement_data_qt[financial_stmts][stockCode]
    df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
    df = df.rename_axis(financial_stmts).reset_index()
    df.insert(0, 'ticker', stockCode)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df.to_excel('D:\\ALL_2\\yahoofinancials\\FIN_0617\\yahooExport_annual_'+ dataType + '_' + stockCode + '.xlsx', sheet_name = sheet_name)

def GET_quarterly_FILE(dataType , stockCode , stockName , currency , financial_stmts):
    sheet_name = stockCode + '-' + currency + '-' + stockName
    yahoo_financials = YahooFinancials(stockCode)
    if dataType == 'IS': statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income' )
    if dataType == 'CF': statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'cash' )
    if dataType == 'BS': statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance' )
    dict_list = statement_data_qt[financial_stmts][stockCode]

    if len(dict_list) > 0 :
       df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
       df = df.rename_axis(financial_stmts).reset_index()
       df.insert(0, 'ticker', stockCode)
       df.drop(df.columns[[0]], axis=1, inplace=True)
       df.to_excel('D:\\ALL_2\\yahoofinancials\\FIN_0617\\yahooExport_Quarterly_'+ dataType + '_' + stockCode + '.xlsx', sheet_name = sheet_name)
    else:   
       print(stockCode + " is pass !!")

def rum_YYYY():
    df = pd.read_excel("D:\\ALL_2\\yahoofinancials\\yahoo_FIN_0401.xlsx",sheet_name="Sheet1",usecols=["國外股票名稱", "國外股票代號"])
    df = df.reset_index()
    # print(df)

    progress = tqdm(total=len(df))      
    
    for index, row in df.iterrows():
        # print(row['國外股票名稱'], row['國外股票代號'])
        progress.update(1)
        stockCode  = row['國外股票代號']
        stockName  = row['國外股票名稱']
        fin = YahooFinancials(stockCode)
        currency = fin.get_currency()
        GET_annual_FILE('IS' , stockCode , stockName , currency , 'incomeStatementHistory'  )
        GET_annual_FILE('CF' , stockCode , stockName , currency , 'cashflowStatementHistory' )
        GET_annual_FILE('BS' , stockCode , stockName , currency , 'balanceSheetHistory'   )

def rum_QQQQ():
  
    df = pd.read_excel("D:\\ALL_2\\yahoofinancials\\yahoo_FIN_0401.xlsx",sheet_name="Sheet1",usecols=["國外股票名稱", "國外股票代號"])
    df = df.reset_index()
    # print(df)
  
    progress = tqdm(total=len(df))    
    
    for index, row in df.iterrows():
        print(row['國外股票名稱'], row['國外股票代號'])
        #progress.update(1)
        stockCode  = row['國外股票代號']
        stockName  = row['國外股票名稱']
        fin = YahooFinancials(stockCode)
        currency = fin.get_currency()
        print(row['國外股票代號'] + " " + stockCode +  " " + currency)
        GET_quarterly_FILE('IS' , stockCode , stockName , currency , 'incomeStatementHistoryQuarterly'  )
        GET_quarterly_FILE('CF' , stockCode , stockName , currency , 'cashflowStatementHistoryQuarterly' )
        GET_quarterly_FILE('BS' , stockCode , stockName , currency , 'balanceSheetHistoryQuarterly'   )


if __name__ == '__main__':
    rum_YYYY()
   # rum_QQQQ()