from datetime import datetime
from System.Collections.Generic import List
from Skender.Stock.Indicators import Indicator
from .Qoute import Qoute


def get_SMA(history, lookbackPeriod):
    sma_list = Indicator.GetSma[Qoute](_convert_df_to_csharp_list(history), lookbackPeriod)
    sma_dict = { _convert_csharp_datetime(i.Date) : (float(str(i.Sma)) if i.Sma else None) for i in sma_list }

    return sma_dict

def _convert_csharp_datetime(csharp_datetime):
    return datetime.strptime(str(csharp_datetime).split(" ")[0], '%m/%d/%Y').strftime('%Y-%m-%d')

def _convert_df_to_csharp_list(history):
    listed = List[Qoute]()
    history.apply(lambda x: listed.Add(Qoute(x)), axis=1)
    
    return listed