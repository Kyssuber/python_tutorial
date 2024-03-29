# -*- coding: utf-8 -*-
def rawdata():
  from matplotlib import pyplot as plt
  import numpy as np
  from astropy.io import ascii

  data = ascii.read("bestfitdata.txt")
  x = data['x']
  y = data['y']
  dy = data['dy']
  
  plt.scatter(x,y)
  plt.errorbar(x,y,data['dy'],ls='None')
  plt.title('Reported Spontaneous Combustions per Unit Century',fontsize=14)
  plt.xlabel('X, Century',fontsize=12)
  plt.ylabel('Y, Spontaneous Combustion',fontsize=12)
  plt.grid() 

def bestfit():
  from matplotlib import pyplot as plt
  import numpy as np
  from astropy.io import ascii
  
  data = ascii.read("bestfitdata.txt")
  x = data['x']
  y = data['y']
  dy = data['dy']
  m,b = np.polyfit(x,y,1) #assume linear relationship
  m1,b1 = np.polyfit(x,y+dy,1) #upper limit
  m2,b2 = np.polyfit(x,y-dy,1) #lower limit

  plt.scatter(x,y)
  plt.errorbar(x,y,data['dy'],ls='None')
  plt.plot(x,m*x + b,'g',label='Best Fit, y = mx + b')
  plt.plot(x,m1*x+b1,'r',label='Best Fit Upper Limit')
  plt.plot(x,m2*x+b2,'r',label='Best Fit Lower Limit')
  plt.title('Reported Spontaneous Combustions per Unit Century',fontsize=14)
  plt.xlabel('X, Century',fontsize=12)
  plt.ylabel('Y, Spontaneous Combustion',fontsize=12)
  plt.legend()
  plt.grid()
  print('The slope of best-fit line is:', m)
  print('The y-intercept of the best-fit line is:',b) #Best Fit (green line below)

