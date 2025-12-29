import pandas as pd

data = {'Price': [12000, 18000, 25000, 14000, 30000]}
df = pd.DataFrame(data)

def price_category(price):
    if price < 15000:
        return "Low Price (Below 15000)"
    elif 15000 <= price < 25000:
        return "Medium Price (15000-24999)"
    else:
        return "High Price (25000 and above)"

df['Price_Category'] = df['Price'].apply(price_category)
print(df)
