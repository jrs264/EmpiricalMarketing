import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def regression(array):
    res = sm.OLS(endog=beer[array[0]], exog=beer[array[1:len(array)+1]], missing='drop')
    results = res.fit()
    print(results.summary())


beer = pd.read_excel('berdata1.xls', delimiter=',', skipinitialspace=True)
frozen_diner = pd.read_excel('frddata1.xls', delimiter=',', skipinitialspace=True)

beerVariables = [['VOL1', 'PRICE1', 'PROMO11', 'PROMO21'],['VOL2', 'PRICE2', 'PROMO12', 'PROMO22'], ['VOL3', 'PRICE3', 'PROMO13', 'PROMO23'], ['VOL4', 'PRICE4', 'PROMO14', 'PROMO24'] ]

for i in range(0,len(beerVariables)):
    regression(beerVariables[i])

