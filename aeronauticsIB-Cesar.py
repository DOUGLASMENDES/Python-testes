import math
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# Assumptions
pi=math.pi
b = 2
chord = 10
rho = 0.002378
weight = 3000
alpha = 2*pi
pitch_angle_tip = 5
inflow_angle_tip = 2
Rvetor = np.arange(1.0, 30.0, 0.1)
degree_to_radian = (pi/180)

# Omega Calculation
Omega = []
K = (4*weight)/(b*rho*alpha*chord*(pitch_angle_tip-inflow_angle_tip)*degree_to_radian)

for R in Rvetor:
    Omega.append(math.sqrt(K/R**3))

# Ct Calculation
Ct = []
K = (alpha*b*chord*(pitch_angle_tip-inflow_angle_tip)*degree_to_radian)/(4*pi)
for R in Rvetor:
    Ct.append(K/R)

# Omega * R
OmegaR = Omega*Rvetor

# V Calculation
v = []
for i in range(0,len(OmegaR)):
    v.append(OmegaR[i] * math.sqrt(Ct[i]/2))

# Graphics
plt.figure(figsize=(6,6))
# plt.axis([0, 6, 0, 20])
plt.plot(Rvetor,Omega)
plt.grid()
plt.ylabel('Angular Velocity \u03A9 (rad/s)')
plt.xlabel('Radius (ft)')
plt.title('Angular Velocity vs Radius')
plt.show()
plt.figure(figsize=(6,6))
plt.plot(OmegaR,v)
plt.grid()
plt.ylabel('Induced Velocity (ft/s)')
plt.xlabel('\u03A9 R')
plt.title('Induced Velocity vs Radius')
plt.show()