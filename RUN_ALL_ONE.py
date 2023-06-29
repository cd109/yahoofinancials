from yahoofinancials import YahooFinancials
import fun

def rum_YYYY():
    stockCode  ='COMM'
    stockName  = 'CommScope'
    fin = YahooFinancials(stockCode)
    currency = fin.get_currency()
    fun.GET_annual_FILE('IS' , stockCode , stockName , currency , 'incomeStatementHistory'  )
    fun.GET_annual_FILE('CF' , stockCode , stockName , currency , 'cashflowStatementHistory' )
    fun.GET_annual_FILE('BS' , stockCode , stockName , currency , 'balanceSheetHistory'   )

def rum_QQQQ():
    stockCode  ='COMM'
    stockName  = 'CommScope'
    fin = YahooFinancials(stockCode)
    currency = fin.get_currency()
    fun.GET_quarterly_FILE('IS' , stockCode , stockName , currency , 'incomeStatementHistoryQuarterly'  )
    fun.GET_quarterly_FILE('CF' , stockCode , stockName , currency , 'cashflowStatementHistoryQuarterly' )
    fun.GET_quarterly_FILE('BS' , stockCode , stockName , currency , 'balanceSheetHistoryQuarterly'   )


if __name__ == '__main__':
    rum_YYYY()
    rum_QQQQ()