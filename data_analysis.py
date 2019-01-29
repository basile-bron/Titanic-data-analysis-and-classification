import numpy as np
import matplotlib.pyplot as plt
from data_import import passagers
#REMINDER
"""The passagers attributes are : survived, pclass, name, sex, age, sibsp, parch, ticket, fare, cabin, embarked"""

#STATISTICS
#gender distrubution pie
def gender_distribution():
    """gender distribution pie chart """
    male = len([passager for passager in passagers if passager.sex == "male"])
    female = len([passager for passager in passagers if passager.sex == "female"])
    sizes = [male, female]
    labels = 'male', 'female'
    explode = (0, 0.1)  #"explode" the 2nd slice
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

#gender survival distrubution
def gender_survival():
    """gender survival bars"""
    #survived
    male_survived = len([passager for passager in passagers if passager.sex == "male" if passager.survived == 1])
    female_survived = len([passager for passager in passagers if passager.sex == "female" if passager.survived == 1])
    #died
    female_died = len([passager for passager in passagers if passager.sex == "female"  if passager.survived == 0])
    male_died = len([passager for passager in passagers if passager.sex == "male" if passager.survived == 0])
    #number of column
    N = 2
    ind = np.arange(N)    # the x locations for the groups
    #seting bars
    men = (male_died,male_survived)
    woman = (female_died,female_survived)
    width = 0.5 #bars width
    p1 = plt.bar(ind, men, width,)
    p2 = plt.bar(ind, woman, width ,bottom=men)
    #captions
    plt.ylabel('passagers')
    plt.title('survival by group and gender')
    plt.xticks(ind, ('died', 'survived'))
    plt.yticks(np.arange(0, 800, 100))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    plt.show()

#showing the stats
gender_distribution()
gender_survival()
