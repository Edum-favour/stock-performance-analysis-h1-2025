def assign_strategy(row):
    
    if row["Ticker"] in aristocrat_tickers:
        return "Income-Focused"
    elif row["Price Return %"] >=10 and row["Dividend Yield %"] <1:
        return "Growth-Focused"
    elif row["Price Return %"] >=5 and row["Dividend Yield %"] >= 1:
        return "Balanced"
    else:
        return "Unclassified"