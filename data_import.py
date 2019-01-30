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
        self.sex = str(data[4]) #sex
        self.age = data[5] #age
        self.sibsp = int(data[6]) # number of siblings
        self.parch = int(data[7]) #number of parent / children
        self.ticket = data[8] #ticket number (we don't need it)
        self.fare = float(data[9]) #price
        self.cabin = data[10] # cabin number
        self.embarked = data[11] # port of embarkement

#IMPORTING TRAIN DATASET
passagers = [passager(row) for row in import_csv("data/train.csv")]#create all the passager

#DATA CLEANING FUNCTION
def missing_age_setter(passagers):
    """Setting age based on title for the empty age row"""
    for passager in passagers:
        if passager.age == '':
            if passager.name.count('Mr'):
                passager.age =33
            if passager.name.count('Master'):
                passager.age =5
            if passager.age == '' and passager.name.count('Miss'):
                passager.age =22
            if passager.age == '' and passager.name.count('Sir'):
                passager.age =43
            if passager.age == '' and passager.name.count('Nobal'):
                passager.age =40
            if passager.age == '' and passager.name.count('Capt'):
                passager.age =57
            else:
                passager.age =30 #arbitrary
        if type(passager.age) == int: #clean remaining dirty type
            passager.age = int(round(float(passager.age))) #dirty but most efficient

def check_missing_value(passagers):
    """listing missing value of the given object """
    missing_value =[]
    for passager in passagers:
        for attribute, value in passager.__dict__.items():
            if value == '':
                missing_value.append(attribute)
    unique = set(missing_value)
    [print(attribute,missing_value.count(attribute)) for attribute in unique ]


missing_age_setter(passagers)
check_missing_value(passagers)
