import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

class Statistics:
    def __init__(self, statsList, coordinatesList):
        self.statsList = statsList
        self.coordinatesList = coordinatesList

    def average(self):
        count = 0
        for i in self.statsList:
            try:
                count += int(i)
            except ValueError:
                pass
        return count / len(self.statsList)

    def standardDeviation(self):
        average = self.average()
        deviationTotal = 0
        sample_divisor = 10
        for i in self.statsList:
            if i % sample_divisor == 0:
                deviationTotal += (average - int(i)) ** 2 #distance from average, squared
        return (deviationTotal / (len(self.statsList) // sample_divisor)) ** .5 #find mean, then square root

    def sampleStandDardDeviation(self):
        average = self.average()
        deviationTotal = 0
        for i in self.statsList:
            deviationTotal += (average - int(i)) ** 2  # distance from average, squared
        return (deviationTotal / (len(self.statsList) -1) ** .5)

    def median(self):
        medianList = self.statsList
        medianList.sort()
        length = len(medianList)
        index = (length -1 ) // 2
        if  length % 2 == 0:
            return medianList[index]
        else:
            return (medianList[index] + medianList[index + 1]) / 2.0

    def mode(self):
        c = Counter(self.statsList)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    def bestFit(self):
        bestFit_x_axis = []
        bestFit_y_axis = []
        for i in range(len(self.coordinatesList)):
            bestFit_x_axis.append(self.coordinatesList[i].x)
            bestFit_y_axis.append(self.coordinatesList[i].y)

        numpy_X = np.array(bestFit_x_axis)
        numpy_Y = np.array(bestFit_y_axis)
        m, b = np.polyfit(numpy_X, numpy_Y, 1)

        plt.plot(bestFit_x_axis, bestFit_y_axis, 'o')

        plt.plot(bestFit_x_axis, m * numpy_X + b)

        plt.show()




