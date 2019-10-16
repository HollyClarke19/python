# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:29:35 2019

@author: medhcl
"""

import random 
import operator
import matplotlib.pyplot

# specify number of agents
num_of_agents = 10 
# specify number of interactions
num_of_interactions = 100

agents = [] # create agents list (empty)

# for however many number of agents create random x and y co-ord
for i in range(num_of_agents):
    agents.append([random.randint(0,100), random.randint(0,100)])

print(agents)

# code to move agent (refer to model 1)
#for specified number of interactions do: 
# for each agent randomise + or - 1 to x and y co-ord (move)
for i in range(num_of_interactions):
    # move agents
    for i in range(num_of_agents):
        if random.random()<0.5:
            agents[i][0] =(agents[i][0] +1) % 100 
        else:
            agents[i][0] = (agents[i][0] -1) % 100  
                
    for i in range(num_of_agents):
        if random.random() <0.5:
            agents[i][1] =(agents[i][1] +1) % 100 
        else:
            agents[i][1] = (agents[i][1] -1) % 100  


'''
solid wall solution (check if on edge and tell to stop if so)
        if agents [i][0] < 0:
            agents [i][0] = 0
        if agents [i][0] > 99:
            agents [i][0] = 99
            
        if agents [i][1] < 0:
            agents[i][1] = 0
        if agents [i][1] > 99:
            agents[i][1] = 99

'''

        
'''
or torus solution as used (leaves and reenters at bottom/top )

 if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100
'''

print(agents)

# tell agents to stop when they meet boundary edge 





# Which agent is furthest East? (max x)
print(max(agents, key = operator.itemgetter(1))) 
#itemgetter gets second item (x)

# plots agents on grid as a scatterplot 

#plots axis
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#for each agent plot on map 
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])


# assign furthers east value red colour 
m = max(agents, key=operator.itemgetter(1)) 
matplotlib.pyplot.scatter(m[1], m[0], color='red')
matplotlib.pyplot.show()
