import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#  import file
n = "./HK_hospitalizations.csv"
data = pd.read_csv(n)
data = data[data['location_key'] == 'HK']
date_list = list(data['date'])
date_list = list(map(lambda x: str(x), date_list))

# for t as time, t0 as initial time, P0 is initial value, K as capacity, and r is increase_rate
def logistic(t, K, P0, r):
    t0 = 10
    r = 0.02
    exp_value = np.exp(r * (t - t0))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

confirm_list = list(data['cumulative_hospitalized_patients'])

time_array = np.array(range(30, len(date_list) + 30))
long_time_array = np.array(range(30, len(date_list) + 150))
confirm_array = np.array(confirm_list)

popt, pcov = curve_fit(logistic, time_array, confirm_array)

P_predict = logistic(long_time_array, popt[0], popt[1], popt[2])
# draw the picture
plot1 = plt.plot(time_array, confirm_array, 's', label="confirmed cumulative_hospitalized_patients")
plot2 = plt.plot(long_time_array, P_predict, 'r', label='predict hospitalized_patients')
plt.xlabel('time')
plt.ylabel('cumulative_hospitalized_patients')
plt.legend(loc=0)
plt.show()