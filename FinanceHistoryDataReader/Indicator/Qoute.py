# C-Sharp Modules
from Skender.Stock.Indicators import Quote
from System import DateTime, Decimal

class Qoute(Quote):
    def __init__(self, pandasSeries):
        t = str(pandasSeries.name)[:10].split("-")
        self.Date = DateTime(int(t[0]), int(t[1]), int(t[2]))
        self.Open = Decimal(float(pandasSeries["Open"]))
        self.High = Decimal(float(pandasSeries["High"]))
        self.Low = Decimal(float(pandasSeries["Low"]))
        self.Close = Decimal(float(pandasSeries["Close"]))
        self.Volume = Decimal(float(pandasSeries["Volume"]))
