import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# for t as time, t0 as initial time, P0 is initial value, K as capacity, and r is increase_rate
def logistic(t, K, P0, r):
    t0 = 10
    r = 0.45
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

# import data
t = [10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
t = np.array(t)
P = [9, 43, 76, 94, 128, 172, 488, 627, 817, 1078, 1951]
P = np.array(P)


popt1, pcov1 = curve_fit(logistic, t, P)

# for t as time, t0 as initial time, P0 is initial value, K as capacity, and r is increase_rate
def logistic(t, K, P0, r):
    t0 = 10
    r = 0.45
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)


P_predict = logistic(t, popt1[0], popt1[1], popt1[2])

# predict future
future = [10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 39, 49, 59, 69, 79, 89, 99]
future = np.array(future)
future_predict = logistic(future, popt1[0], popt1[1], popt1[2])

# predict tomorrow
tomorrow = [26, 27, 28, 29, 30, 33, 37, 40]
tomorrow = np.array(tomorrow)
tomorrow_predict = logistic(tomorrow, popt1[0], popt1[1], popt1[2])

# Print picture
plot1 = plt.plot(t, P, 's', label="cumulative_hospitalized_patients")
plot2 = plt.plot(t, P_predict, 'r', label='predict cumulative_hospitalized_patients')
plot3 = plt.plot(tomorrow, tomorrow_predict, 's', label='tomorrow cumulative_hospitalized_patients')
plt.xlabel('time')
plt.ylabel('cumulative_hospitalized_patients')
plt.legend(loc=0)
plt.show()