def normalize(series, inverse=False):
    norm = (series - series.min()) / (series.max() - series.min())
    return 1 - norm if inverse else norm

performers["Score_Value"] = normalize(performers["P/E Ratio"], inverse=True)
performers["Score_Growth"] = normalize(performers["Price Return %"])
performers["Score_Quality"] = normalize(performers["ROE"])
performers["Score_Yield"] = normalize(performers["Dividend Yield %"])
performers["Score_Stability"] = normalize(performers["Volatility %"], inverse=True)
performers["Score_Liquidity"] = normalize(performers["Avg Daily Volume"])


performers["Final Score"] = (
    0.25 * performers["Score_Quality"] +
    0.20 * performers["Score_Growth"] +
    0.15 * performers["Score_Value"]+
    0.15 * performers["Score_Yield"] +
    0.15 * performers["Score_Stability"] +
    0.10 * performers["Score_Liquidity"]
)

return performers