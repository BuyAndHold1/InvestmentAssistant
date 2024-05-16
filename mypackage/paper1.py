from collections import defaultdict
import yfinance as yf
from datetime import datetime




def tradeRobot():
        #end_date = datetime.today().strftime('%Y-%m-%d')
        data_sp500 = yf.download('^GSPC', period='1y')
        max_price = int(data_sp500['High'].max())
        closing_price = int(data_sp500['Close'].iloc[-1])
        data_gold = yf.download('GC=F', period='1d')
        max_price_gold = int(data_gold['High'].max())
        data_dow = yf.download('^DJI', period='1d')
        max_price_dow = int(data_dow['High'].max())
        print(data_gold)
        print(max_price)
        print(f"today price gold {max_price_gold}")
        print(f"today price gold {max_price_dow}")
        min_price = int(data_sp500['Low'].min())
        print(f"S&P_500_cena HighHight {max_price}")
        print(f"S&P_500_cena LowLow {min_price}")
        print(f"S&P_500_cena close {closing_price}")
        buyOrSellGold = max_price_dow / max_price_gold
        williamsR = ((max_price - closing_price) / (max_price - min_price)) * (-100)
        #obligacii = 35
        returnString = ""
        if williamsR < (-20):
            sp500 = "Good price for S&P 500 ETF"
            #print(sp500)
            returnString += sp500 + "\n"
        if buyOrSellGold >= 16:
            Gold = "Good price for GOLD"
            returnString += Gold + "\n"
        else:
            franki = "buy currency CHF"
            print("kupite valjutu")
            returnString += franki + "\n"
        
        #print(returnString)

        return returnString

tradeRobot()
