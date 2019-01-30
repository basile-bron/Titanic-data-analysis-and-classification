import numpy as np
import matplotlib.pyplot as plt
from statistics import mean #average function
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

#social class survival distribution
def class_survival():
    """social class survival purcentage bars"""
    #number of column
    N = 3
    ind = np.arange(N)
    #seting bars
    first_class = mean([passager.survived for passager in passagers if passager.pclass == 1])*100
    second_class = mean([passager.survived for passager in passagers if passager.pclass == 2])*100
    third_class = mean([passager.survived for passager in passagers if passager.pclass == 3])*100
    width = 0.5 #bars width
    p1 = plt.bar(ind, [first_class,second_class,third_class], width )
    #captions
    plt.ylabel('passagers')
    plt.title('survival by class')
    plt.xticks(ind, ('1st class', '2nd class', '3rd class'))
    plt.yticks(np.arange(0, 110, 10))
    plt.legend(["survived %"])
    plt.show()

#social class survival distribution
def class_gender_survival():
    """social class and gender survival purcentage bars"""
    #number of column
    N = 3
    ind = np.arange(N)
    #seting bars
    female_first_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 1 if passager.sex == "female"]) / len([passager for passager in passagers if passager.pclass == 1]))
    female_second_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 2 if passager.sex == "female"]) / len([passager for passager in passagers if passager.pclass == 2]))
    female_third_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 3 if passager.sex == "female"]) / len([passager for passager in passagers if passager.pclass == 3]))
    female = [female_first_class,female_second_class,female_third_class]

    male_first_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 1 if passager.sex == "male"]) / len([passager for passager in passagers if passager.pclass == 1]))
    male_second_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 2 if passager.sex == "male"]) / len([passager for passager in passagers if passager.pclass == 2]))
    male_third_class = 100*( sum([passager.survived for passager in passagers if passager.pclass == 3 if passager.sex == "male"]) / len([passager for passager in passagers if passager.pclass == 3]))
    male = [male_first_class, male_second_class, male_third_class]
    width = 0.5 #bars width
    p1 = plt.bar(ind, male, width)
    p2 = plt.bar(ind, female, width ,bottom=male)
    #captions
    plt.ylabel('passagers')
    plt.title('survival by class')
    plt.xticks(ind, ('1st class', '2nd class', '3rd class'))
    plt.yticks(np.arange(0, 110, 10))
    plt.legend((p1[0], p2[0]), ('Men survived %', 'Women survived %'))
    plt.show()

#showing the stats
gender_distribution()
gender_survival()
class_survival()
class_gender_survival()
