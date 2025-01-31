# MATH199 CHP Project 2
#
# Program that determines which pitch types are likliest to hit
#
# Kenneth Tochihara

import csv #to access csv files
import matplotlib.pyplot as plt #to create cool graffs

# This part gathers the data for the event that occured as a result of the pitch type
with open('../data/pitches.csv', mode = 'r') as csv_file:
    pitches = csv.DictReader(csv_file)

    #swinging strike, called strike, foul, hit out, hit on, ball
    data_fastball = {'count': 0, 'STW': 0, 'C': 0, 'F': 0, 'X': 0, 'DE': 0, 'B': 0}
    data_offspeed = {'count': 0, 'STW': 0, 'C': 0, 'F': 0, 'X': 0, 'DE': 0, 'B': 0}

    for row in pitches:
        #fastballs
        if row['Is Fastball'] == 'True':
            data_fastball['count'] += 1

            if (row['Call'] == 'S') | (row['Call'] == 'T') | (row['Call'] == 'W'): #swinging strike
                data_fastball['STW'] += 1

            if row['Call'] == 'C': #called strike
                data_fastball['C'] += 1

            if row['Call'] == 'F': #foul
                data_fastball['F'] += 1

            if row['Call'] == 'X': #hit out
                data_fastball['X'] += 1

            if (row['Call'] == 'D') | (row['Call'] == 'E'): # hit in play
                data_fastball['DE'] += 1

            if (row['Call'] == 'B'): # ball
                data_fastball['B'] += 1

        #offspeeds
        elif row['Is Fastball'] == 'False':
            data_offspeed['count'] += 1

            if (row['Call'] == 'S') | (row['Call'] == 'T') | (row['Call'] == 'W'):
                data_offspeed['STW'] += 1

            if row['Call'] == 'C':
                data_offspeed['C'] += 1

            if row['Call'] == 'F':
                data_offspeed['F'] += 1

            if row['Call'] == 'X':
                data_offspeed['X'] += 1

            if (row['Call'] == 'D') | (row['Call'] == 'E'):
                data_offspeed['DE'] += 1

            if (row['Call'] == 'B'): # ball
                data_offspeed['B'] += 1

#This part analyzes the data into a pie chart

labels = ['Swinging Strike', 'Called Strike', 'Foul', 'Hit Out', 'Hit Safe', 'Ball']
labels_distribution = ['Fastballs', 'Offspeed']

sizes_fastball = [data_fastball['STW'], data_fastball['C'], data_fastball['F'], data_fastball['X'], data_fastball['DE'], data_fastball['B']]
sizes_offspeed = [data_offspeed['STW'], data_offspeed['C'], data_offspeed['F'], data_offspeed['X'], data_offspeed['DE'], data_offspeed['B']]
sizes_distribution = [data_fastball['count'], data_offspeed['count']]

colors = ['#DEF6CA', '#DB162F', '#DBDFAC', '#5F758E', '#D9D9D9', '#F8BDC4']
colors_distribution = ['#DBDFAC', '#5F758E']

# fastballs figures
plt.pie(sizes_fastball, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Result Breakdown For Fastball Pitches')
plt.savefig('figures/fastball.png')

plt.clf() # clears

# offspeeds figures
plt.pie(sizes_offspeed, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Result Breakdown For Offspeed Pitches')
plt.savefig('figures/offspeed.png')

plt.clf() # clears

# pitch distribution figures
plt.pie(sizes_distribution, labels=labels_distribution, colors=colors_distribution, autopct='%1.1f%%')
plt.title('Result Breakdown For Pitches Thrown')
plt.savefig('figures/distribution.png')
