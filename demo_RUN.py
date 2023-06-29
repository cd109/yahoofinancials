from yahoofinancials import YahooFinancials
import pandas as pd
import json
from pandas import json_normalize


def main_Quarterly():
  stockCode       = "0751.HK"
  stockName       = "PEGATRON 和碩"
  financial_stmts = "incomeStatementHistoryQuarterly"
  dataType        = "IS_US"
  fin = YahooFinancials(stockCode)
  currency = fin.get_currency()
  sheet_name = stockCode + '-' + currency + '-' + stockName
  yahoo_financials = YahooFinancials(stockCode)
  statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income' )
  dict_list = statement_data_qt[financial_stmts][stockCode]
  df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
  df = df.rename_axis(financial_stmts).reset_index()
  df.insert(0, 'ticker', stockCode)
  df.drop(df.columns[[0]], axis=1, inplace=True)
  df.to_excel('yahooExport_Quarterly_'+ dataType + '_' + stockCode + '.xlsx', sheet_name = sheet_name)

def main_Annual():
  stockCode       = "HPE"
  stockName       = "HPE"
  financial_stmts = "incomeStatementHistory"
  dataType        = "IS_US"
  fin = YahooFinancials(stockCode)
  currency = fin.get_currency()
  sheet_name = stockCode + '-' + currency + '-' + stockName
  yahoo_financials = YahooFinancials(stockCode)
  statement_data_qt = yahoo_financials.get_financial_stmts('annual', 'income' )
  dict_list = statement_data_qt[financial_stmts][stockCode]
  df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
  df = df.rename_axis(financial_stmts).reset_index()
  df.insert(0, 'ticker', stockCode)
  df.drop(df.columns[[0]], axis=1, inplace=True)
  df.to_excel('yahooExport_Annual_'+ dataType + '_' + stockCode + '.xlsx', sheet_name = sheet_name)



if __name__ == '__main__':
    main_Annual()
