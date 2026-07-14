import numpy as np

cost_prices = [100, 150, 200, 250, 300]

cp_ar = np.array(cost_prices)
print(cp_ar)
print(cp_ar.shape)
print(cp_ar.dtype)

sp_ar = cp_ar * 1.13
print(sp_ar)

profit_ar = sp_ar - cp_ar
print(profit_ar)

def price_range(price):
    if price < 150:
        return "low"
    elif 150 <= price <= 250:
        return "medium"
    else:
        return "high"

price_range_vec = np.vectorize(price_range)
price_cat_ar = price_range_vec(cp_ar)
print(price_cat_ar)

print(np.char.upper(price_cat_ar))
print(np.char.lower(price_cat_ar))
print(np.char.title(price_cat_ar))

rev_ar = profit_ar - 2
print(rev_ar)

sp_ar_rounded = np.round(sp_ar, 2)
print(sp_ar_rounded)