#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## groundhog.py
## File description:
## Do my groundhog....
##

import sys
import os
from sys import stdin
from math import *
from statistics import *
from collections import OrderedDict
import statistics as stats
import random
import operator

def usage():
    print("SYNOPSIS")
    print("\t./groundhog period\n\nDESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

def err_groundhog():
    if len(sys.argv) == 1:
        print("./205IQ -h")
        exit(84)
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            usage()
            exit(0)
    elif len(sys.argv) > 2:
        print("Too many arguments")
        exit(84)

def get_value():
    try:
        nb_value = int(sys.argv[1])
    except ValueError:
        print("One arg isn't a number")
        sys.exit(84)
    if (nb_value < 0):
        print("The number is negative")
        sys.exit(84)
    return nb_value

class MYGroundhog:
    def __init__(self, period):
        self._nb_tendency = int(0)
        self._weirdestValueList = list()
        self._Lastr_temp = int(0)
        self._r_temp = int(0)
        self._s_temp = float(0)
        self._g_temp = float(0)
        self._period = int(period)
        self._tab_temp = list()

    def get_input(self):
        input_nbr = input("")
        if input_nbr == "STOP":
            if (len(self._tab_temp) <= self._period):
                print("Insufficient data")
                sys.exit(84)
            self.EndingGroundhog()
            sys.exit(0)
        try:
            nbr = float(input_nbr)
        except:
            print("The value isn't a float")
            sys.exit(84)
        if nbr < 0:
            print("The value is negative")
            sys.exit(84)
        return nbr
    
    def TemperatureIncreaseAverage(self):
        if (len(self._tab_temp) <= self._period):
            self._g_temp = "nan"
        else:
            self._g_temp = 0
            for index in range(len(self._tab_temp) - self._period, len(self._tab_temp)):
                nb = self._tab_temp[index] - self._tab_temp[index - 1]
                if (nb < 0):
                    self._g_temp = self._g_temp + 0
                else:
                    self._g_temp = self._g_temp + nb
            try:
                self._g_temp /= self._period
            except ZeroDivisionError:
                self._g_temp = 0

    def RelativeTemperatureEvolution(self):
        if (len(self._tab_temp) <= self._period):
            self._r_temp = "nan"
        else:
            if (self._r_temp != "nan"):
                self._Lastr_temp = self._r_temp
            var1 = self._tab_temp[len(self._tab_temp) - self._period - 1]
            var2 = self._tab_temp[-1]
            if var1 == 0:
                self._r_temp = 0
            else:
                self._r_temp = round((var2 - var1) / var1 * 100)

    def TemperatureSwitched(self):
        if (self._r_temp != "nan"):
            if (self._Lastr_temp < 0 and self._r_temp > 0):
                return True
            elif (self._Lastr_temp > 0 and self._r_temp < 0):
                return True
            else:
                return False
        else:
            return False

    def StandardDeviation(self):
        if (len(self._tab_temp) < self._period):
            self._s_temp = "nan"
        else:
            x = 0
            y = 0
            for index in range(len(self._tab_temp) - self._period, len(self._tab_temp)):
                x = x + self._tab_temp[index]
                y = y + pow(self._tab_temp[index], 2)
            self._s_temp = sqrt((y / self._period) - pow((x / self._period), 2))

    def CalculTempWeather(self):
        self.TemperatureIncreaseAverage()
        self.RelativeTemperatureEvolution()
        self.StandardDeviation()
    
    def DisplayTempWeather(self):
        if (len(self._tab_temp) < self._period):
            print("g=nan\tr=nan%\ts=nan")
        elif (len(self._tab_temp) <= self._period):
            print("g=nan\tr=nan\ts=" + "%.2f" % self._s_temp)
        else:
            message = "g=" + str(round(self._g_temp, 2)) + "\tr=" + str(round(self._r_temp, 2)) + "%\ts=" + ("%.2f" % self._s_temp)
            if (self.TemperatureSwitched() == True):
                message += "\ta switch occurs"
                self._nb_tendency = self._nb_tendency + 1
            print(message)

    def GetTheWeirdestValue(self, user_input):
        TempArray = list()
        LastPeriodeValue = len(self._tab_temp) - self._period
        for i in range(LastPeriodeValue, len(self._tab_temp)):
                TempArray.append(self._tab_temp[i])
        TempArray.sort()
        if (len(TempArray) % 2) == 0:
            M = median(TempArray)
        else:
            M = ((median_low(TempArray) + median_high(TempArray)) / 2)
        if (len(TempArray) % 4) == 0:
            Q1 = TempArray[len(TempArray)//4 - 1]
            Q3 = TempArray[3 * len(TempArray)//4 - 1]
        else:
            Q1 = TempArray[len(TempArray)//4]
            Q3 = TempArray[3 * len(TempArray)//4]
        InterQ = Q3 - Q1
        InterLimit = InterQ * 0.8
        InterLimitInf = Q1 - InterLimit
        InterLimitSup = Q3 + InterLimit
        if (user_input < InterLimitInf or user_input > InterLimitSup):
            self._weirdestValueList.append(user_input)

    def GetTheMostWeirdestValue(self):
        try:
            Avg = sum(self._weirdestValueList) / len(self._weirdestValueList)
        except ZeroDivisionError:
            Avg = 0
        d = dict()
        for i in self._weirdestValueList:
            Nb = Avg - i
            Nb = Nb**2
            d[round(Nb, 2)] = i
        d = OrderedDict(sorted(d.items(), key=lambda t: t[0], reverse = True))
        ReturnList = list(d.values())
        if (len(ReturnList) > 5):
            while len(ReturnList) > 5:
                ReturnList.pop()
        if (len(ReturnList) < 5):
            while(len(ReturnList) < 5):
                ReturnList.append(random.choice(self._tab_temp))
        return ReturnList

    def EndingGroundhog(self):
        my_values = list()
        message_tendency = "Global tendency switched " + str(self._nb_tendency) + " times"
        print(message_tendency)
        if (self._nb_tendency > 0):
            my_values = self.GetTheMostWeirdestValue()
            print("5 weirdest values are", my_values)

    def my_groundhog(self):
        while (True):
            nb_input = self.get_input()
            self._tab_temp.append(nb_input)
            self.CalculTempWeather()
            if (len(self._tab_temp) >= self._period):
                self.GetTheWeirdestValue(nb_input)
            self.DisplayTempWeather()


def groundhog():
    if len(sys.argv) == 2:
        nb_value = get_value()
        my_ground = MYGroundhog(nb_value)
        my_ground.my_groundhog()

def main():
    err_groundhog()
    groundhog()
    

if __name__ == "__main__":
    main()