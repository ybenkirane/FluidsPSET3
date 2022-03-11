# -*- coding: utf-8 -*-
"""
@author: Yacine Benkirane

Collaborators: Jasmine Zhang, Alexandre Stuart
"""

import numpy as np 
import matplotlib.pyplot as plt

nu_val = 1

#use this function to solve for u numerically for a range of nu values
def f(u): 
    return 10000*(u**3)+500*(u**(5/2))*((nu_val*0.01)**(1/2))-(9.8*10**9)

# Manually calculated f(u) as was experiencing buggy fsolve with collaborators... 

pow_1 = 99.99
pow_2 = 99.95
pow_3 = 99.85
pow_4 = 99.55
pow_5 = 98.65
pow_6 = 95.85
pow_7 = 88.45

#Plot with some Common Fluids
# Reference for Kinematic Viscosity Values from  https://www.engineersedge.com/fluid_flow/kinematic-viscosity-table.htm

xVal = np.linspace(1,10**4)

plt.xscale('log')
plt.xlabel('Kinematic Viscosity [cm$^{2}$/s]')
plt.ylabel('Velocity [cm/s]')
plt.title('Swimmer Vel vs Kinematic Viscosity')

plt.plot(np.array([np.power(10,1), np.power(10,2), np.power(10,3), np.power(10,4), np.power(10,5), np.power(10,6), np.power(10,7)]), np.array([pow_1, pow_2, pow_3, pow_4, pow_5, pow_6, pow_7]))

plt.axvline(x=52, color='brown',label = "Glycol")
plt.axvline(x=7.9, color='blue',label = "Jet Fuel")
plt.axvline(x=110, color='green',label = "Quenching Oil (typical)")
plt.axvline(x=0.01, color='grey',label = "Water")
plt.axvline(x=5640, color='red',label = "Rosin (wood)")

plt.legend()
plt.show