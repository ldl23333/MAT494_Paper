import pandas as pd
import csv

file = pd.read_csv("./hospitalizations.csv")
file2 = file
file3 = pd.read_csv("./HK_hospitalizations.csv")
file4 = pd.read_csv("./HK_hospitalizations.csv")
file5 = pd.read_csv("./HK_hospitalizations.csv")

file = file[file['location_key'].isin(["US"])]
file2 = file2[file2['location_key'].isin(["HK"])]


file=file.drop(["new_hospitalized_patients","current_hospitalized_patients","new_intensive_care_patients","current_intensive_care_patients","cumulative_intensive_care_patients","new_ventilator_patients","cumulative_ventilator_patients","current_ventilator_patients"],axis=1)
file2=file2.drop(["new_hospitalized_patients","current_hospitalized_patients","new_intensive_care_patients","current_intensive_care_patients","cumulative_intensive_care_patients","new_ventilator_patients","cumulative_ventilator_patients","current_ventilator_patients"],axis=1)

file3.drop(file3.index[120:688],inplace=True)

file4.drop(file4.index[0:120],inplace=True)
file4.drop(file4.index[123:568],inplace=True)

file5.drop(file5.index[0:242],inplace=True)
file5.drop(file5.index[409:446],inplace=True)


file.to_csv("./US_hospitalizations.csv",index=0)
file2.to_csv("./HK_hospitalizations.csv",index=0)

file3.to_csv("./HK_hospitalizations_Part1.csv",index=0)
file4.to_csv("./HK_hospitalizations_Part2.csv",index=0)
file5.to_csv("./HK_hospitalizations_Part3.csv",index=0)