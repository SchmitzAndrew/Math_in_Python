import math

class Statistics:
    def __init__(self, statsList):
        self.statsList = statsList

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
        for i in self.statsList:
            deviationTotal += (average - int(i)) ** 2 #distance from average, squared
        return (deviationTotal / len(self.statsList)) ** .5 #find mean, then square root

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
        pass



