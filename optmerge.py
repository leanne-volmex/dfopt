import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

# create the option dataframe
options = pd.DataFrame({'instId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                      'other_col': ['a','b','c','d','e','f','g','h','i','j']
                      })

# create the data dictionary
data = {'bookSummary': np.random.rand(10, 4),
        'optionMarkPrices': np.random.rand(10, 3),
        'optionQuotes': np.random.rand(10, 6)
       }

# create the bookSummary dataframe
bookSummary = pd.DataFrame(data['bookSummary'], columns=["instId", "ts", "fwdPx", "markVol"])

# merge the options dataframe with the bookSummary dataframe on the 'instId' column
options = options.merge(bookSummary, on='instId', how='left')
logging.info("options after bookSummary merge: %s", options)

# create the optionMarkPrices dataframe
optionMarkPrices = pd.DataFrame(data['optionMarkPrices'], columns=["instId", "ts", "markPx"])

# merge the options dataframe with the optionMarkPrices dataframe on the 'instId' column
options = options.merge(optionMarkPrices, on='instId', how='left', suffixes = ('','_mark'))
logging.info("options after optionMarkPrices merge: %s", options)

# create the option quotes dataframe
optionQuotes = pd.DataFrame(data['optionQuotes'], columns=['instId', 'ts', 'bidPx', 'bidSz', 'askPx', 'askSz'])

# merge the options dataframe with the option_quotes dataframe on the 'inst
options = options.merge(optionQuotes, on='instId', how='left', suffixes = ('','_quote'))
logging.info("options after optionQuotes merge: %s", options)
