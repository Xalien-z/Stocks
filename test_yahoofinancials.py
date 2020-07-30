from yahoofinancials import YahooFinancials


ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)
balance_sheet_data = yahoo_financials.get_financial_stmts('quarterly', 'balance')
earnings_data = yahoo_financials.get_stock_earnings_data()
historical_prices = yahoo_financials.get_historical_price_data('2015-01-15', '2017-10-15', 'weekly')

'''
error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Inna\AppData\Local\Programs\Python\Python38-32\lib\site-packages\yahoofinancials\__init__.py", line 592, in get_financial_stmts
    data = self._run_financial_stmt(statement_type, report_num, reformat)
  File "C:\Users\Inna\AppData\Local\Programs\Python\Python38-32\lib\site-packages\yahoofinancials\__init__.py", line 582, in _run_financial_stmt
    raw_data = self.get_stock_data(statement_type, report_name=report_name)
  File "C:\Users\Inna\AppData\Local\Programs\Python\Python38-32\lib\site-packages\yahoofinancials\__init__.py", line 473, in get_stock_data
    dict_ent = self._create_dict_ent(self.ticker, statement_type, tech_type, report_name, hist_obj)
  File "C:\Users\Inna\AppData\Local\Programs\Python\Python38-32\lib\site-packages\yahoofinancials\__init__.py", line 399, in _create_dict_ent
    re_data = self._scrape_data(YAHOO_URL, tech_type, statement_type)
  File "C:\Users\Inna\AppData\Local\Programs\Python\Python38-32\lib\site-packages\yahoofinancials\__init__.py", line 153, in _scrape_data
    self._cache[url] = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
AttributeError: 'NoneType' object has no attribute 'group'
'''