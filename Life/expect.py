import matplotlib.pyplot as plt
import csv
import numpy as np



filename  = "Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"
csvfile = open(filename, newline='')
life = csv.reader(csvfile, delimiter=',')


def worst_county(year):

    minium = 100000
    first_line = True

    for i in life:

        if first_line:
            first_line = False
            continue

        g = float(i[4]) + float(i[7]) / 2

        if i[3] == str(year):

            if g < minium:
                minium = g
                S = i[0]
                C = i[1]

    return(S,C)



def plotdata(state,county):
    filename  = "Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"
    csvfile = open(filename, newline='')
    life = csv.reader(csvfile, delimiter=',')
    #years
    yy = []
    #female plot
    fc = []
    fs = []
    fn = []
    #male plot
    mc = []
    ms = []
    mn = []

    for i in life:

        if i == -2:
            return None

        elif i[0] == state and i[1] == county:
            #years
            yy += [int(i[3])]
            #female
            fc += [float(i[4])]
            fs += [float(i[6])]
            fn += [float(i[5])]
            #male
            mc += [float(i[7])]
            ms += [float(i[9])]
            mn += [float(i[8])]

    plt.plot(yy, fc, color='g',) #green
    plt.plot(yy, fs, color='r',)
    plt.plot(yy, fn, color='y',)
    plt.plot(yy, mc, color='c',)
    plt.plot(yy, ms, color='b',)
    plt.plot(yy, mn, color='m',)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title(state + ' , ' + county + ' : Life Expectancy')
    plt.show()
   



if __name__ == "__main__": 
    state,county =  worst_county(2010)  
    plotdata(state,county)
    print(state, county)
