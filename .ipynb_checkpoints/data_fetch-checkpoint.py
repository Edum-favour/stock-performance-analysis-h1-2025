import yfinance as yf
from datetime import datetime

start_date = "2025-01-01"
end_date = "2025-06-30"

def get_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        
        hist = stock.history(start=start_date, end=end_date)
        if hist.empty:
            print(f"{ticker}: No price data - retrying once...")
            time.sleep(0.5)
            hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
            print(f"{ticker}: Still no price data - skipping.")
            return None

        # Calculate price return + momentum
        start_price = hist.iloc[0]["Close"]
        end_price = hist.iloc[-1]["Close"]
        price_return = ((end_price - start_price) / start_price) * 100
        momentum = end_price - start_price

        # Volatility (Daily returns standard deviation)
        hist["Daily Return"] = hist["Close"].pct_change()
        volatility = hist["Daily Return"].std() * (252 ** 0.5) * 100
        
        # Dividend Yield
        dividends = stock.dividends
        q1_dividends = dividends.loc[(dividends.index >= start_date) & (dividends.index <= end_date)].sum()
        dividend_yield = (q1_dividends / start_price) * 100

        # Liquidity
        avg_volume = hist["Volume"].mean()

        # Total Return
        total_return = price_return + dividend_yield

        # Extract fundamentals from yahoo finance
        try:
            info = stock.info
            roe = info.get("returnOnEquity", None)
            roe = roe * 100 if roe is not None else None
            pe_ratio = info.get("trailingPE", None)
            
        except:
            roe = None
            pe_ratio = None
            
            return {
        "Ticker": ticker,
        "Company Name": ticker_name_map.get(ticker, ""),
        "Start Price": round(start_price, 2),
        "End Price": round(end_price, 2),
        "Price Return %": round(price_return, 2),
        "Q1 Dividends ($)": round(q1_dividends, 2),
        "Dividend Yield %": round(dividend_yield, 2),
        "Total Return %": round(total_return, 2),
        "Volatility %": round(volatility, 2),
        "Avg Daily Volume": round(avg_volume),
        "Momentum ($)": round(momentum, 2),
        "ROE": round(roe, 2) if roe is not None else None,
        "P/E Ratio": round(pe_ratio, 2) if pe_ratio is not None else None
        
        }
    except Exception as e:
        return None

results = []

for i, ticker in enumerate(tickers):
    ticker = ticker.replace(".", "-")
    print(f"[{i+1}/{len(tickers)}] Checking: {ticker}")
    data = get_stock_data(ticker)
    if data:
        print(" Appending:", data)
        results.append(data)

print(f"\n✅ Completed. Total stocks found: {len(results)}")