import numpy as np

stock_prices = np.array([100, 150, 200, 250, 300, 270])
returns_ar = (stock_prices[1:] - stock_prices[:-1]) / stock_prices[:-1]
print(returns_ar)

deposits = np.array([10, 15, 20, 25, 30, 27])
total_amount_ar = np.cumsum(deposits)
print(total_amount_ar)

co2 = np.array([100, 150, 200, 250, 300])
co2_norm = (co2 - np.min(co2)) / (np.max(co2) - np.min(co2))
print(co2_norm)

salaries = np.array([800, 1200, 3000, 6000])
new_salary_ar = np.where(salaries < 1000, salaries * 1.20,
                np.where(salaries <= 5000, salaries * 1.10, salaries * 1.05))
print(new_salary_ar)