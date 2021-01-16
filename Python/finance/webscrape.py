import requests
import pandas as pd
from bs4 import BeautifulSoup

tickers = ["LSE.L","REL.L", "EXPN.L"]
data = {}


for ticker in tickers:
    
    #get balance sheet
    temp_dict = {}
    url = "https://uk.finance.yahoo.com/quote/"+ticker+"/balance-sheet?p="+ticker
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    tabl = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class": "rw-expnded"})
        for row in rows:
            temp_dict[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]

    #get income statement
    url = "https://uk.finance.yahoo.com/quote/"+ticker+"/financials?p="+ticker
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    tabl = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class": "rw-expnded"})
        for row in rows:
            temp_dict[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]

    #get cashflow statement
    url = "https://uk.finance.yahoo.com/quote/"+ticker+"/cash-flow?p="+ticker
    page = requests.get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    tabl = soup.find_all("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        rows = t.find_all("div", {"class": "rw-expnded"})
        for row in rows:
            temp_dict[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]

    #TODO: Update Scraper for new webpage
    #get key statistics
    # url = "https://uk.finance.yahoo.com/quote/"+ticker+"/key-statistics?p="+ticker
    # page = requests.get(url)
    # content = page.content
    # soup = BeautifulSoup(content, 'html.parser')
    # tabl = soup.find_all("table", {"class": "W(100%) Bdc1(c) Mt(10px) "})   
    # for t in tabl:
    #     rows = t.find_all("tr")
    #     for row in rows:
    #         print(row)
    #         if len(row.get_text(separator='|').split("|")[0:2])>0:
    #             temp_dict[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[-1]

    #combine for ticker data
    data[ticker] = temp_dict

#combine data for all tickers
combined = pd.DataFrame(data)
tickers = combined.columns

#remove non numeric data
for ticker in tickers:
    combined = combined[~combined[ticker].str.contains("[a-z]").fillna(False)]

