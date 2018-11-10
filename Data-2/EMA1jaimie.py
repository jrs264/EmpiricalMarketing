import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm

def winsorize(variables, df):
    for i in range(0,len(variables)):
        for j in range (0,len(variables[i])):
            df[variables[i][j]] = stats.mstats.winsorize(df[variables[i][j]], limits=0.025)

def regression(array, df):
    res = sm.OLS(endog=df[array[0]], exog=df[array[1:len(array)+1]], missing='drop')
    results = res.fit()
    print(results.summary())

beer = pd.read_excel('berdata1.xls', delimiter=',', skipinitialspace=True)

columnValues = [['VOL1', 'PRICE1', 'PROMO11', 'PROMO21'],['VOL2', 'PRICE2', 'PROMO12', 'PROMO22'], ['VOL3', 'PRICE3', 'PROMO13', 'PROMO23'], ['VOL4', 'PRICE4', 'PROMO14', 'PROMO24'] ]

winsorize(columnValues, beer)

for i in range(0,len(columnValues)):
    regression(columnValues[i], beer)

