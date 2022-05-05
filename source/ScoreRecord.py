import os
import pickle

from LinkedList import LinkedList

RECORD_SIZE_BYTES = 200

class Scores:

    def __init__(self, fPath):

        if os.exists(fPath):
            with open(fPath, 'rb') as f:
                self.__scores = pickle.load(f)

        else:
            self.__scores = LinkedList()

    def write(self, fPath):

        with open(fPath, 'wb') as f:
            pickle.dump(self.__scores, f)


    def addScore(newScore):
        self.__scores.insert(newScore)

    def sortByStart(self):
        scoreData = self.__scores.getData()

        swapped = True
        while not swapped:
            for x in range(len(scoreData) - 1):
                if scoreData[x]["startTime"] > scoreData[x+1]["startTime"]:
                    scoreData[x], scoreData[x+1] = scoreData[x+1], scoreData[x]
                    swapped = True

        return scoreData

    def checkTie(self, time):
        idx = len(self.__scores) // 2
        pivot = idx
        remaining = self.__scores
        while remaining[pivot]["timeMs"] != time:

            pivot = len(remaining) // 2

            if remaining[pivot]["timeMs"] > time:
                idx -= pivot
                remaining = remaining[:pivot]
            if remaining[pivot]["timeMs"] < time:
                idx += pivot
                remaining = remaining[pivot:]

        return self.__scores[idx]["timeMs"] == time
