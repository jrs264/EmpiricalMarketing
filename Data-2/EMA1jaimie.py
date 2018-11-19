import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm

def winsorize(variables, df):
    for i in range(0,len(variables)):
        for j in range (0,len(variables[i])):
            df[variables[i][j]] = stats.mstats.winsorize(df[variables[i][j]], limits=0.025)

def jarqueBera(variables, df):
    for i in range(0,len(variables)):
        jb = sm.stats.stattools.jarque_bera(df[variables[i]])
        print(variables[i], jb)

def linearRainbow(res):
    testresult = sm.stats.diagnostic.linear_rainbow(res, frac=0.5)
    print('Rainbow test result:', testresult)

def tests(variables, df):
    jarqueBera(variables, df)

def regression(array, df):
    exog = df[array[1:len(array)+1]]
    exog = sm.add_constant(exog)
    results = sm.OLS(endog=df[array[0]], exog=exog).fit()

    linearRainbow(results)

    print(results.summary())

def main():
    df = []
    beer = pd.read_excel('berdata1.xls', delimiter=',', skipinitialspace=True)
    beer2 = pd.read_excel('berdata1.xls', delimiter=',', skipinitialspace=True)
    frozenDinner = pd.read_excel('frddata1.xls', delimiter=',', skipinitialspace=True)

    df.append(beer)
    df.append(frozenDinner)

    columnValues = [['VOL1', 'PRICE1', 'PROMO11', 'PROMO21'],['VOL2', 'PRICE2', 'PROMO12', 'PROMO22'], ['VOL3', 'PRICE3', 'PROMO13', 'PROMO23'], ['VOL4', 'PRICE4', 'PROMO14', 'PROMO24'] ]


    for j in range(0, len(df)):
        print('--------------NEW DATAFRAME--------------')
        winsorize(columnValues, df[j])
        for i in range(0,len(columnValues)):
            tests(columnValues[i], df[j])
            regression(columnValues[i], df[j])

if __name__ == '__main__':
    main()
