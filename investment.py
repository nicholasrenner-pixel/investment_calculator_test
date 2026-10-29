print('an investor purcahses 10 shares of apple stock at 150$ each')
new_share_price = 175
shares_bought = 10
price = 150
investment = shares_bought*price
new_investment = shares_bought*new_share_price
print(f"an investor bought ${investment} of apple stock")
print('the investor sold it at 175 per share a year later')
profit = new_investment - investment
pct_return = (profit/investment)*100
print(f'your profit is {profit}$')
print(f'your return on investment is {pct_return:2f}%')