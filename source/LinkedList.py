#!/usr/bin/env python3
class Node():
    def __init__(self,datac,pointerc):
        self.__data = datac
        self.__pointer = pointerc

    def getpointer(self):
        return self.__pointer

    def setpointer(self,pointerc):
        self.__pointer = pointerc

    def getdata(self):
        return self.__data

    def setdata(self,datac):
        self.__data = datac

class Linkedlist():

    def __init__(self):
        self.__nodes = [Node("",0) for i in range(10)]
        self.__nullpointer = -1
        self.__startpointer = self.__nullpointer
        self.__nextpointer = 0
        #self.__newval = ""
        for index in range(0,10):
            self.__nodes[index].setpointer(index+1)
        self.__nodes[index].setpointer(self.__nullpointer)

    def insert(self,newval):
        newnodepointer = 0
        thisnodepointer = 0
        previousnodepointer = 0
        if self.__nextpointer != self.__nullpointer:
            newnodepointer = self.__nextpointer
            self.__nodes[newnodepointer].setdata(newval)
            self.__nextpointer = self.__nodes[newnodepointer].getpointer()
            thisnodepointer = self.__startpointer
            while thisnodepointer != self.__nullpointer and self.__nodes[thisnodepointer].getdata() < newval:
                previousnodepointer = thisnodepointer
                thisnodepointer = self.__nodes[thisnodepointer].getpointer()
            if thisnodepointer == self.__startpointer:
                self.__nodes[newnodepointer].setpointer(self.__startpointer)
                self.__startpointer = newnodepointer
            else:
                self.__nodes[newnodepointer].setpointer(self.__nodes[previousnodepointer].getpointer())
                self.__nodes[previousnodepointer].setpointer(newnodepointer)

    def delete(self,delval):
        thisnodepointer = self.__startpointer
        while thisnodepointer != self.__nullpointer and self.__nodes[thisnodepointer].getdata() != delval:
            previousnodepointer = thisnodepointer
            thisnodepointer = self.__nodes[thisnodepointer].getpointer()
        if thisnodepointer != self.__nullpointer:
            if thisnodepointer == self.__startpointer:
                self.__startpointer = self.__nodes[self.__startpointer].getpointer()
            else:
                self.__nodes[previousnodepointer].setpointer(self.__nodes[thisnodepointer].getpointer())
        self.__nodes[thisnodepointer].setpointer(self.__nextpointer)
        self.__nextpointer = thisnodepointer

    def find(self,finddata):
        currentnodepointer = self.__startpointer
        while currentnodepointer != self.__nullpointer and self.__nodes[currentnodepointer].getdata() != finddata:
            currentnodepointer = self.__nodes[currentnodepointer].getpointer()
        return currentnodepointer

    def replace(self,finddata,replacedata):
        candelete = False
        for i in range(10):
            if self.__nodes[i].getdata() == finddata: candelete = True
        if candelete == True:
            self.delete(finddata)
            self.insert(replacedata)
        else:
            return -1
