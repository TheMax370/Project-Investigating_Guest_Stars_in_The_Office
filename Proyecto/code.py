import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = pd.read_csv('datasets/office_episodes.csv')

x = np.array(file.loc[:,'episode_number'])

y = np.array(file.loc[:, 'viewership_mil'])

scaled_ratings = np.array(file.loc[:, 'scaled_ratings'])

has_guests = np.array(file.loc[:,'has_guests'])

sizing = np.array([])

for i in has_guests:
    if i == True:
     sizing = np.append(sizing, 250)
    else:
     sizing = np.append(sizing, 25)
    
colors = pd.cut(x=scaled_ratings, bins=[np.NINF, 0.25, .5, .75, np.inf], labels=['red', 'orange', 'lightgreen', 'darkgreen'],right=False)

plt.title("Popularity, Quality, and Guest Appearances on the Office")

plt.xlabel("Episode Number")

plt.ylabel("Viewership (Millions)")

plt.scatter(x, y, color=colors, s=sizing)



plt.show()
