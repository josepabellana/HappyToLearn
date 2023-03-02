import pandas as pd
import yfinance as yf
import pandas_ta as ta
import yahoo_fin.stock_info as si

tickers = si.tickers_sp500()

df = (pd.DataFrame(yf.download(tickers, '2015-01-01'))
      .dropna(axis=1)
      .stack(level=1)
      .reset_index()
      .set_index("Date")
      .sort_values(by=["level_1", "Date"]))

indicadores = ta.Strategy(
    name='All',
    description='All',
    ta=None

)

def strat(x):
    x.ta.strategy(indicadores)
    return x

full= df.groupby(['level_1'], group_keys=False).apply(strat)
full = full.pivot(columns='level_1')