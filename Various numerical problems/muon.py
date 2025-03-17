import numpy as np
import matplotlib.pyplot as plt


def replaceDelimiter(fileName):
    with open(fileName+'.txt', 'r') as inFile:
        data_raw = inFile.read().replace(';', ':').replace('.', ':')

    with open(fileName+'_Rep'+'.txt', 'w') as outFile:
        outFile.write(data_raw)


def integerHist(data):
    '''Make a histogram of integer data.'''
    plt.hist(data+0.5, bins=np.arange(np.amin(data),
             np.amax(data)+2), label='Data')


def showIntegerHist(data, xlabel, ylabel='Counts', title='Detectors 1,2,5, 17/02'):
    '''Show the histogram made by integerHist'''
    integerHist(data)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()


def importData(filePath):
    data = np.genfromtxt(filePath, skip_header=2, delimiter=':',
                         invalid_raise=False, usecols=[1, 2, 3])
    hours, minutes, seconds = data[:, 0], data[:, 1], data[:, 2]
    hours -= hours[0]
    return hours, minutes, seconds
