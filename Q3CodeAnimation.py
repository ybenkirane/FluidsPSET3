# -*- coding: utf-8 -*-
"""
@author: Yacine Benkirane

Collaborators: Jasmine Zhang, Alexandre Stuart
"""

import numpy as np
import matplotlib.pyplot as plt

def steadyState(viscosity, height, inclination, x):
    return (-9.8*np.sin(inclination)*(0.5*x**2 - height*x))/viscosity 

LAVAvisco = 0.25
LAVAHeight = 0.1
LAVAinc = 0.17 

SSX = np.linspace(0, LAVAHeight, 30)
SSY = steadyState(LAVAvisco, LAVAHeight, LAVAinc, np.linspace(0, LAVAHeight, 30))

plt.plot(SSX, SSY)
plt.xlabel('Pos (m)')
plt.ylabel('Vel (m/s)')
plt.show()

#Step Conditions

timeStep = 0.0001
gridStep = 0.01
betaVal = LAVAvisco * timeStep / (gridStep**2)

gravFac = 9.8 * np.sin(LAVAinc)

xGrid = np.arange(0, 0.11, gridStep)
endTime = 0.06
initialF = np.zeros(len(xGrid))

# Let's Animate with multiple steps
M = np.eye(len(xGrid)) * (1.0 + 2.0*betaVal) + np.eye(len(xGrid), k = 1) *-betaVal + np.eye(len(xGrid), k=-1)*-betaVal

fNow = np.copy(initialF)
timeNow = 0
curr_percent = 0

plt.ion()
fig, ax = plt.subplots(1,1)
plot, = ax.plot(xGrid, initialF)

M[0][0] = 1
M[0][1] = 0
M[-1][-1] = 1 + betaVal

fig.canvas.draw()
plt.plot(SSX, SSY)

while (timeNow <= endTime): 
    if (timeNow != endTime):
        fNow = np.linalg.solve(M, fNow)
        
        fNow += gravFac*timeStep
        
        fNow[0] = 0
    
    timeNow += timeStep
    
    ax.collection = []
    ax.patches = []
    
    plot.set_ydata(fNow)
    plt.legend(['Time Evolution', 'Steady State'])
    plt.title('Velocity Profile of Lava Flowing down Inclined Plane')
    plt.xlabel('Pos (m)')
    plt.ylabel('Vel (m/s)')
    plt.ylim([0, 0.1])
    fig.canvas.draw()
    plt.pause(0.01)
    

