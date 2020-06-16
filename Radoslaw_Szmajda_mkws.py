import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas = ct.Solution('gri30.xml')
gas2 = ct.Solution('gri30.xml')
npoints = 60

T0 = 273.15
P0 = 101325.0

fuel_species = 'H2'
fuel_species2 = 'CH4'
# T(Phi)

phi = np.linspace(0.3, 3.5, npoints)
myk0 = np.zeros(npoints)

for i in range(npoints):
    gas.set_equivalence_ratio(phi[i], fuel_species, 'O2:1.0, N2:3.76')
    gas.TP = T0, P0
    gas.equilibrate('HP')
    myk0[i] = gas.T


print('T(Phi)H')
fig, ax = plt.subplots()
ax.plot(phi, myk0)
ax.set(xlabel='Equivalence ratio [-]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi1

P = np.linspace(0.1 * ct.one_atm, ct.one_atm * 6, npoints)
phi1 = 0.5
myk2 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi1, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk2[i] = gas.T


print('T(p) for Phi1H')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk2)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi2

phi2 = 1
myk3 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi2, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk3[i] = gas.T


print('T(p) for Phi2H')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk3)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi3

phi3 = 1.5
myk4 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi3, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk4[i] = gas.T


print('T(p) for Phi3H')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk4)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi4

phi4 = 2
myk5 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T0, P[i]
    gas.set_equivalence_ratio(phi4, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk5[i] = gas.T


print('T(p) for Phi4H')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk5)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for all Phi values

fig, ax = plt.subplots()
plt.plot(P / 100000, myk2, label='$ \Phi1 $')
plt.plot(P / 100000, myk3, label='$ \Phi2 $')
plt.plot(P / 100000, myk4, label='$ \Phi3 $')
plt.plot(P / 100000, myk5, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi1

T = np.linspace(273, 2000, npoints)
myk12 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi1, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk12[i] = gas.T


print('T(T) for Phi1H')
fig, ax = plt.subplots()
ax.plot(T, myk12)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi2

T = np.linspace(273, 2000, npoints)
myk13 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi2, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk13[i] = gas.T


print('T(T) for Phi2H')
fig, ax = plt.subplots()
ax.plot(T, myk13)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi3

T = np.linspace(273, 2000, npoints)
myk14 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi3, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk14[i] = gas.T


print('T(T) for Phi3H')
fig, ax = plt.subplots()
ax.plot(T, myk14)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi4

T = np.linspace(273, 2000, npoints)
myk15 = np.zeros(npoints)

for i in range(npoints):
    gas.TP = T[i], P0
    gas.set_equivalence_ratio(phi4, fuel_species, 'O2:1.0, N2:3.76')
    gas.equilibrate('HP')
    myk15[i] = gas.T


print('T(T) for Phi4H')
fig, ax = plt.subplots()
ax.plot(T, myk15)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for all Phi values

fig, ax = plt.subplots()
plt.plot(T, myk12, label='$ \Phi1 $')
plt.plot(T, myk13, label='$ \Phi2 $')
plt.plot(T, myk14, label='$ \Phi3 $')
plt.plot(T, myk15, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# FROM HERE METHANE
# FROM HERE METHANE
# FROM HERE METHANE
# FROM HERE METHANE
# FROM HERE METHANE
# T(Phi)

phi = np.linspace(0.3, 3.5, npoints)
myk000 = np.zeros(npoints)

for i in range(npoints):
    gas2.set_equivalence_ratio(phi[i], fuel_species2, 'O2:1.0, N2:3.76')
    gas2.TP = T0, P0
    gas2.equilibrate('HP')
    myk000[i] = gas2.T


print('T(Phi)C')
fig, ax = plt.subplots()
ax.plot(phi, myk000)
ax.set(xlabel='Equivalence ratio [-]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi1

P = np.linspace(0.1 * ct.one_atm, ct.one_atm * 6, npoints)
phi1 = 0.5
myk002 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T0, P[i]
    gas2.set_equivalence_ratio(phi1, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk002[i] = gas2.T


print('T(p) for Phi1C')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk002)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi2

phi2 = 1
myk003 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T0, P[i]
    gas2.set_equivalence_ratio(phi2, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk003[i] = gas2.T


print('T(p) for Phi2C')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk003)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi3

phi3 = 1.5
myk004 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T0, P[i]
    gas2.set_equivalence_ratio(phi3, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk004[i] = gas2.T


print('T(p) for Phi3C')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk004)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for Phi4

phi4 = 2
myk005 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T0, P[i]
    gas2.set_equivalence_ratio(phi4, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk005[i] = gas2.T


print('T(p) for Phi4C')
fig, ax = plt.subplots()
ax.plot(P / 100000, myk005)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(p) for all Phi values

fig, ax = plt.subplots()
plt.plot(P / 100000, myk002, label='$ \Phi1 $')
plt.plot(P / 100000, myk003, label='$ \Phi2 $')
plt.plot(P / 100000, myk004, label='$ \Phi3 $')
plt.plot(P / 100000, myk005, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Pressure [bar]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi1

T = np.linspace(273, 2000, npoints)
myk0012 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T[i], P0
    gas2.set_equivalence_ratio(phi1, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk0012[i] = gas2.T


print('T(T) for Phi1C')
fig, ax = plt.subplots()
ax.plot(T, myk0012)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi2

T = np.linspace(273, 2000, npoints)
myk0013 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T[i], P0
    gas2.set_equivalence_ratio(phi2, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk0013[i] = gas2.T


print('T(T) for Phi2C')
fig, ax = plt.subplots()
ax.plot(T, myk0013)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi3

T = np.linspace(273, 2000, npoints)
myk0014 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T[i], P0
    gas2.set_equivalence_ratio(phi3, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk0014[i] = gas2.T


print('T(T) for Phi3C')
fig, ax = plt.subplots()
ax.plot(T, myk0014)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for Phi4

T = np.linspace(273, 2000, npoints)
myk0015 = np.zeros(npoints)

for i in range(npoints):
    gas2.TP = T[i], P0
    gas2.set_equivalence_ratio(phi4, fuel_species2, 'O2:1.0, N2:3.76')
    gas2.equilibrate('HP')
    myk0015[i] = gas2.T


print('T(T) for Phi4C')
fig, ax = plt.subplots()
ax.plot(T, myk0015)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()

# T(T) for all Phi values

fig, ax = plt.subplots()
plt.plot(T, myk0012, label='$ \Phi1 $')
plt.plot(T, myk0013, label='$ \Phi2 $')
plt.plot(T, myk0014, label='$ \Phi3 $')
plt.plot(T, myk0015, label='$ \Phi4 $')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
ax.set(xlabel='Temperature [K]', ylabel='Adiabatic flame temperature [K]')
ax.get_yaxis().get_major_formatter().set_useOffset(False)
plt.show()