import numpy as np
import pandas as pd

# Generate options dataframe with 10 entries
options = pd.DataFrame(np.random.randn(10, 4), columns=["instId", "ts", "fwdPx", "markVol"])

# Create dictionary with 3 dataframes
data = {"bookSummary": pd.DataFrame(np.random.randn(10, 4), columns=["instId", "ts", "fwdPx", "markVol"]),
        "optionMarkPrices": pd.DataFrame(np.random.randn(10, 3), columns=["instId", "ts", "markPx"]),
        "optionQuotes": pd.DataFrame(np.random.randn(10, 6), columns=['instId', 'ts', 'bidPx', 'bidSz', 'askPx', 'askSz'])}

# Merge options dataframe with "bookSummary" dataframe using "instId" as key and "left" join method
merged_df1 = pd.merge(options, data["bookSummary"], on='instId', how='left')

# Merge result with "optionMarkPrices" dataframe using "instId" as key and "left" join method, using suffixes ('','_mark')
merged_df2 = pd.merge(merged_df1, data["optionMarkPrices"], on='instId', how='left', suffixes=('','_mark'))

# Merge result with "option quotes" dataframe using "instId" as key and "left" join method, using suffixes ('','_quote')
final_merged_df = pd.merge(merged_df2, data["optionQuotes"], on='instId', how='left', suffixes=('','_quote'))

print(final_merged_df)
