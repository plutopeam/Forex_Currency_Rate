# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:25:33 2020

@author: bhudis.wi
"""

#Install Library forex-python

from forex_python.converter import CurrencyRates
import pandas as pd
from datetime import datetime, timedelta

df_currency = pd.DataFrame(columns=['date', 'currency_rate'])
#list_currency = []
currency = CurrencyRates()
start_date = datetime(2019, 1, 1)
end_date = datetime(2020, 1, 1)
delta = timedelta(days=1)
while start_date <= end_date:
    currency_rates = currency.get_rate('USD', 'THB', start_date)
    df_currency = df_currency.append({'date':start_date, 'currency_rate':currency_rates}, ignore_index=True)
    start_date += delta

df_currency['mean'] = df_currency['currency_rate'].mean()
df_currency['-1SD'] = df_currency['currency_rate'].mean() - df_currency['currency_rate'].std()
df_currency['+1SD'] = df_currency['currency_rate'].mean() + df_currency['currency_rate'].std()
df_currency['-2SD'] = df_currency['currency_rate'].mean() - 2*(df_currency['currency_rate'].std())
df_currency['+2SD'] = df_currency['currency_rate'].mean() + 2*(df_currency['currency_rate'].std())
df_currency.plot(y=['currency_rate','-1SD','mean','+1SD','-2SD','+2SD'])