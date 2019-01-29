import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt
import os
import sys
import re
import pandas
import csv
################################################################################
#Import data function
def import_csv(path):
    """Data import function """
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader) # exclude the header of the data and store it in variable "header"
    data = [row for row in reader]
    return data

#Passager class
class passager():
    """class for the passagers."""
    def __init__(self, data):
        #self.passager_id = int(data[0])
        self.survived = int(data[1]) # survived
        self.pclass = int(data[2]) # ticket class
        self.name = str(data[3]) #name
        self.sex = data[4] #sex
        self.age = 0 if data[5] is "" else int(round(float(data[5])))  #age (0 if none)
        self.sibsp = int(data[6]) # number of siblings
        self.parch = int(data[7]) #number of parent / children
        self.ticket = data[8] #ticket number (we don't need it)
        self.fare = float(data[9]) #price
        self.cabin = data[10] # cabin number
        self.embarked = data[11] # port of embarkement

#IMPORTING TRAIN DATASET
data=[]
data = import_csv("data/train.csv")
passagers = [passager(row) for row in data]
