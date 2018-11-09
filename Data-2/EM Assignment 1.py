import pandas as pd
import numpy as np
import numpy.random as rnd
import scipy as sp
import scipy.stats as stats
import scipy.linalg as spla
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math

dir(math)
        
def OrdinaryLeastSquares(y, X):
    X = sm.add_constant(X)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary(),"\n")
    
def ScatterPlot(x, y):
    a, b = np.polyfit(x, y, 1)
    plt.plot(x, a*x+b, color='red')  
    plt.scatter(x, y)  
    #plt.show()

def TracePlot(y):
    x_values = np.arange(0, 176, 1)
    plt.plot(x_values, y)
    plt.xlabel('Time')
    plt.ylabel('Sales')
    #plt.show()
    
def main():
    beer = pd.read_excel('berdata1.xls', delimiter=',', skipinitialspace=True)
    beer = beer[51:]
    frozen_diner = pd.read_excel('frddata1.xls', delimiter=',', skipinitialspace=True)
    frozen_diner = frozen_diner[:176]
    #beer_sorted = (np.sort(beer.T)).T
    #diner_sorted = (np.sort(diner.T)).T
    #quantiles = np.array([int(round(0.025*176)), int(round(0.975*176))])
    #beer = beer_sorted[quantiles[]]
    
    sales_beer = beer.loc[:,"CSALES"]
    vol1_beer = beer.loc[:,"VOL1"]
    vol2_beer = beer.loc[:,"VOL2"]
    vol3_beer = beer.loc[:,"VOL3"]
    vol4_beer = beer.loc[:,"VOL4"]
    price1_beer = beer.loc[:,"PRICE1"]
    price2_beer = beer.loc[:,"PRICE2"]
    price3_beer = beer.loc[:,"PRICE3"]
    price4_beer = beer.loc[:,"PRICE4"]
    promo11_beer = beer.loc[:,"PROMO11"]
    promo12_beer = beer.loc[:,"PROMO12"]
    promo13_beer = beer.loc[:,"PROMO13"]
    promo14_beer = beer.loc[:,"PROMO14"]
    promo21_beer = beer.loc[:,"PROMO21"]
    promo22_beer = beer.loc[:,"PROMO22"]
    promo23_beer = beer.loc[:,"PROMO23"]
    promo24_beer = beer.loc[:,"PROMO24"]
    
    ScatterPlot(promo21_beer, vol1_beer)
    ScatterPlot(promo22_beer, vol2_beer)
    ScatterPlot(promo23_beer, vol3_beer)
    ScatterPlot(promo24_beer, vol4_beer)
    
    promo21_beer = stats.mstats.winsorize(promo21_beer, limits = 0.025)
    promo22_beer = stats.mstats.winsorize(promo22_beer, limits = 0.025)
    promo23_beer = stats.mstats.winsorize(promo23_beer, limits = 0.025)
    promo24_beer = stats.mstats.winsorize(promo24_beer, limits = 0.025)
    
    ScatterPlot(promo21_beer, vol1_beer)
    ScatterPlot(promo22_beer, vol2_beer)
    ScatterPlot(promo23_beer, vol3_beer)
    ScatterPlot(promo24_beer, vol4_beer)
    
    TracePlot(vol1_beer)
    ScatterPlot(price1_beer, vol1_beer)
    ScatterPlot(price2_beer, vol2_beer)
    ScatterPlot(price3_beer, vol3_beer)
    ScatterPlot(price4_beer, vol4_beer)
    ScatterPlot(promo11_beer, vol1_beer)
    ScatterPlot(promo12_beer, vol2_beer)
    ScatterPlot(promo13_beer, vol3_beer)
    ScatterPlot(promo14_beer, vol4_beer)
    ScatterPlot(promo21_beer, vol1_beer)
    ScatterPlot(promo22_beer, vol2_beer)
    ScatterPlot(promo23_beer, vol3_beer)
    ScatterPlot(promo24_beer, vol4_beer)
    
    #sales_frozen = np.vstack((vol1_frozen, vol2_frozen, vol3_frozen, vol4_frozen, promo11_frozen, promo12_frozen, promo13_frozen, promo14_frozen, promo21_frozen, promo22_frozen, promo23_frozen, promo24_frozen)).T
    variables1 = np.vstack((vol1_beer, price1_beer, promo11_beer, promo21_beer)).T
    variables2 = np.vstack((vol2_beer, price2_beer, promo12_beer, promo22_beer)).T
    variables3 = np.vstack((vol3_beer, price3_beer, promo13_beer, promo23_beer)).T
    variables4 = np.vstack((vol4_beer, price4_beer, promo14_beer, promo24_beer)).T
    
    #Descriptive statistics
    print("Statistics daily returns 1:\n", stats.describe(variables1))
    print("Statistics daily returns 2:\n", stats.describe(variables2))
    print("Statistics daily returns 3:\n", stats.describe(variables3))
    print("Statistics daily returns 4:\n", stats.describe(variables4))
    
    print(pd.DataFrame(variables1).corr())
    print(pd.DataFrame(variables2).corr())
    print(pd.DataFrame(variables3).corr())
    print(pd.DataFrame(variables4).corr())
    
    X1 = np.vstack((price1_beer, promo11_beer, promo21_beer)).T
    X2 = np.vstack((price2_beer, promo12_beer, promo22_beer)).T
    X3 = np.vstack((price3_beer, promo13_beer, promo23_beer)).T
    X4 = np.vstack((price4_beer, promo14_beer, promo24_beer)).T
    
    OrdinaryLeastSquares(vol1_beer, X1)
    OrdinaryLeastSquares(vol2_beer, X2)
    OrdinaryLeastSquares(vol3_beer, X3)
    OrdinaryLeastSquares(vol4_beer, X4)
    
    X1_new = np.vstack((price1_beer, promo21_beer)).T
    X2_new = np.vstack((price2_beer, promo22_beer)).T
    X3_new = np.vstack((price3_beer, promo13_beer, promo23_beer)).T
    X4_new = np.vstack((price4_beer, promo14_beer)).T
    
    OrdinaryLeastSquares(vol1_beer, X1_new)
    OrdinaryLeastSquares(vol2_beer, X2_new)
    OrdinaryLeastSquares(vol3_beer, X3_new)
    OrdinaryLeastSquares(vol4_beer, X4_new)
    
    
    #y = sales_frozen
    #X = np.vstack((promo11_frozen, promo12_frozen, promo13_frozen, promo14_frozen, promo21_frozen, promo22_frozen, promo23_frozen, promo24_frozen)).T
    #OrdinaryLeastSquares(y, X)

    
if __name__ == '__main__':
    main()
