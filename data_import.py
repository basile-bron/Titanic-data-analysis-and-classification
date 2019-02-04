import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt
import os
import sys
import re
import pandas
import csv
from string import ascii_lowercase
################################################################################
#Import data function
def import_csv(path):
    """Data import function """
    file = open(path, newline='')
    reader = csv.reader(file)
    header = next(reader) # exclude the header of the data and store it in variable "header"
    #print(header)
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
        #self.ticket = data[8] #ticket number (we don't need it)
        self.fare = 0 if data[9] == "" else float(data[9]) #price
        self.cabin = data[10] # cabin number
        self.embarked = data[11] # port of embarkement

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

    def sex_to_boolean(passagers):
        for passager in passagers:
            if passager.sex == "female":
                passager.sex = 0
            elif passager.sex == "male":
                passager.sex = 1
            else:
                print("missing sex")
                passager.sex = 0

    def cabin_fill_and_convert(passagers):
        for passager in passagers:
            if passager.cabin == "":
                passager.cabin = 0.0
            else:
                nums = [str(ord(x) - 96) for x in passager.cabin.lower() if x >= 'a' and x <= 'z']
                passager.cabin = float("".join(nums))

def clean_passagers(passagers):
    passager.cabin_fill_and_convert(passagers)
    passager.sex_to_boolean(passagers)
    passager.missing_age_setter(passagers)
    passager.check_missing_value(passagers)
    return passagers

#SETTING TRAIN DATASET
def setting_input(passagers):
    train_x = []
    train_y = []
    for passager in passagers:
        train_x.append([passager.pclass,passager.sex,passager.age ,passager.sibsp,passager.parch,passager.fare,passager.cabin])
        train_y.append(passager.survived)
    print(np.array(train_x).shape)
    print(len(train_y))
    return train_x, train_y
