import streamlit as st
import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials


st.title('YahooFinancials app')


# Boolean to resize the dataframe, stored as a session state variable
##st.checkbox("Use container width", value=False, key="use_container_width")


code = st.text_input("輸入stockCode", 'COMM')


st.button('query')

stockCode  ='COMM'
stockName  = 'CommScope'

financial_stmts = 'incomeStatementHistory'
yahoo_financials = YahooFinancials(stockCode)
statement_data_qt = yahoo_financials.get_financial_stmts('annual', 'income' )
dict_list = statement_data_qt[financial_stmts][stockCode]
df = pd.concat([pd.DataFrame(i) for i in dict_list], axis=1)
df = df.rename_axis(financial_stmts).reset_index()
df.insert(0, 'ticker', stockCode)
df.drop(df.columns[[0]], axis=1, inplace=True)


st.dataframe(df) ##, use_container_width=st.session_state.use_container_width

##chart_data = pd.DataFrame(np.random.randn(20, 3), columns=df.columns)

##print(df.columns)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


col1, col2, col3 = st.columns(3)

with col1:
   st.header("DATA_1")
   st.line_chart(chart_data)

with col2:
   st.header("DATA_1")
   st.line_chart(chart_data)

with col3:
   st.header("DATA_1")
   st.line_chart(chart_data)

