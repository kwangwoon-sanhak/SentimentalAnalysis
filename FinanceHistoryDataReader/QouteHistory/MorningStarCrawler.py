import requests
import datetime
from bs4 import BeautifulSoup


class MorningStarCrawler:

    CUR = datetime.datetime.now().year

    def __init__(self, symbol, market):
        '''
        Fetch PER, PBR, ROE data of the recent 10 years.
        Market
        XHKG: Hong Kong Stock Exchange
        XASE: American Stock Exchange
        XNAS: Nasdaq Stock Exchange
        XNYS: New York Stock Exchange
        XSHE: ShenZhen Stock Exchange
        XSHG: Shanghai Stock Exchange
        '''

        self.symbol = symbol
        self.market = market
        self.url = "http://financials.morningstar.com/valuate/valuation-history.action?&t={market}:{symbol}&type=price-earnings"\
            .format(market=market, symbol=symbol)
        # url = "http://financials.morningstar.com/valuate/valuation-history.action?&t=<MARKET>:<SYMBOL>&type=price-book"
        # url = "http://financials.morningstar.com/valuate/valuation-history.action?&t=<MARKET>:<SYMBOL>&type=price-sales"
        
        html= requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        
        # P/E ratio
        per_list = soup.select("#valuation_history_table > tbody > tr:nth-child(2) > td")
        per_list = list(map(lambda x : x.text, per_list))
        per_dict = { str(self.CUR-len(per_list)+i+1) : per for i, per in enumerate(per_list) }
        
        # P/B ratio
        pbr_list = soup.select("#valuation_history_table > tbody > tr:nth-child(5) > td")
        pbr_list = list(map(lambda x : x.text, pbr_list))
        pbr_dict = { str(self.CUR-len(pbr_list)+i+1) : pbr for i, pbr in enumerate(pbr_list) }
        
        roe_list = []
        for per, pbr in zip(per_list, pbr_list):
            if per != '—' and pbr != '—':
                roe_list.append(round(float(pbr)/float(per),1))
            else:
                roe_list.append('—')

        roe_dict = { str(self.CUR-len(roe_list)+i+1) : roe for i, roe in enumerate(roe_list) }

        self.per = per_dict
        self.pbr = pbr_dict
        self.roe = roe_dict

    def get_per(self):
        return self.per

    def get_pbr(self):
        return self.pbr
        
    def get_roe(self):
        return self.roe