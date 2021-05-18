import clr
clr.AddReference(r'dll/Skender.Stock.Indicators')

import FinanceHistoryDataReader.QouteHistory as qh
import FinanceHistoryDataReader.Indicator as Indicator

# NASDAQ
apple_history = qh.get_history("AAPL", "2021", per=True, pbr=True)
nasdaq_history = qh.get_history("IXIC", "2020")
bond_u3y_history = qh.get_history('US3YT=X', "2020")
wti_history = qh.get_history("CL", "2020")

nasdaq_sma5 = Indicator.get_SMA(nasdaq_history, 5)
nasdaq_sma20 = Indicator.get_SMA(nasdaq_history, 20)
bond_u3y_sma5 = Indicator.get_SMA(bond_u3y_history, 5)
bond_u3y_sma20 = Indicator.get_SMA(bond_u3y_history, 20)
wti_sma5 = Indicator.get_SMA(wti_history, 5)

qh.add_column_by_day(apple_history, "nasdaq_ma5", nasdaq_sma5)
qh.add_column_by_day(apple_history, "nasdaq_ma20", nasdaq_sma20)
qh.add_column_by_day(apple_history, "bond_u3y_ma5", bond_u3y_sma5)
qh.add_column_by_day(apple_history, "bond_u3y_ma20", bond_u3y_sma20)
qh.add_column_by_day(apple_history, "wti_ma5", wti_sma5)

qh.save_as_csv(apple_history, "AAPL_2021_with_nasdaq_ma_bond_wti.csv")

print(apple_history)
