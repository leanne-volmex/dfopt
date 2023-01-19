import pandas as pd
# create the options dataframe with 10 entries
options = pd.DataFrame({'instId':[1,2,3,4,5,6,7,8,9,10],
                       'ts':[100,200,300,400,500,600,700,800,900,1000],
                       'fwdPx':[10,20,30,40,50,60,70,80,90,100],
                       'markVol':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]})

# create the data dictionary with the 3 dataframes
data = {'bookSummary': pd.DataFrame({'instId':[1,2,3,4,5,6,7,8,9,10],
                                    'ts':[100,200,300,400,500,600,700,800,900,1000],
                                    'fwdPx':[10,20,30,40,50,60,70,80,90,100],
                                    'markVol':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]}),
               'optionMarkPrices': pd.DataFrame({'instId':[1,2,3,4,5,6,7,8,9,10],
                                                'ts':[100,200,300,400,500,600,700,800,900,1000],
                                                'markPx':[11,21,31,41,51,61,71,81,91,101]}),
               'optionQuotes': pd.DataFrame({'instId':[1,2,3,4,5,6,7,8,9,10],
                                             'ts':[100,200,300,400,500,600,700,800,900,1000],
                                             'bidPx':[12,22,32,42,52,62,72,82,92,102],
                                             'bidSz':[1,2,3,4,5,6,7,8,9,10],
                                             'askPx':[13,23,33,43,53,63,73,83,93,103],
                                             'askSz':[11,12,13,14,15,16,17,18,19,20]})}


# merge the options dataframe with the dataframe created from the "bookSummary" key of the "data" dictionary
options = options.merge(data['bookSummary'], on='instId', how='left')

# merge the result with another dataframe created from the "optionMarkPrices" key of the "data" dictionary
options = options.merge(data['optionMarkPrices'], on='instId', how='left', suffixes=('','_mark'))

# merge the result with another dataframe created from the "option quotes" key of the "data" dictionary
options = options.merge(data['optionQuotes'], on='instId', how='left', suffixes=('','_quote'))

print(options)
