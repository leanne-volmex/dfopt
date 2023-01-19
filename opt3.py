import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

instId = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# create options dataframe
options = pd.DataFrame()
#options[['underlying','base_opt','expiry','K','O']] = instId.str.split('-', expand = True)
options['instId'] = instId

# create data dictionary
data = {
    "bookSummary": {
        "instId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "ts": [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
        "fwdPx": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        "markVol": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4]
    },
    "optionMarkPrices": {
        "instId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "ts": [200, 201, 202, 203, 204, 205, 206, 207, 208, 209],
        "markPx": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    },
    "optionQuotes": {
        "instId": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "ts": [300, 301, 302, 303, 304, 305, 306, 307, 308, 309],
        "bidPx": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        "bidSz": [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "askPx": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
        "askSz": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    }
}

# create dataframes from data dictionary
bookSummary = pd.DataFrame(data["bookSummary"])
optionMarkPrices = pd.DataFrame(data["optionMarkPrices"])
optionQuotes = pd.DataFrame(data["optionQuotes"])

# merge options with bookSummary using instId as key and left join method
options = pd.merge(options, bookSummary, on="instId", how="left")
logging.info("options after bookSummary merge: %s", options)

# merge result with optionMarkPrices using instId as key and left join method, use suffixes to distinguish columns
options = pd.merge(options, optionMarkPrices, on="instId", how="left", suffixes=('','_mark'))
logging.info("options after optionMarkPrices merge: %s", options)

# merge result with option quotes using instId as key and left join method, use suffixes to distinguish columns
options = pd.merge(options, optionQuotes, on="instId", how="left", suffixes=('','_quote'))
logging.info("options after optionQuotes merge: %s", options)

# the options dataframe now has all the columns from the bookSummary, optionMarkPrices, and option quotes dataframes
print(options)
