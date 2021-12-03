## Weekly Greenhouse Gas Estimation

import numpy as np
import pandas as pd
import os
import datetime 

# ### Dynamic Data: Weekly GDP tracker

# Weekly Updated GDP change estimate by OECD: 
#     https://www.oecd.org/economy/weekly-tracker-of-gdp-growth/

# The variable **Change** is defined as 
#     the percent change of last week's GDP 
#     compared to the same week of the pre-pandemic year. 

# It is conceptually equivalent to the following, 
#     although the actual calculation is far more complicated:

# \begin{align*}
# y_{i,0} &= \textrm{Weekly GDP of the week i of THIS year, measured at PRE-pandemic price level}\\
# y_{i,pre} &= \textrm{Weekly GDP of the week i of PRE-pandemic year}\\
# \textrm{Change} &= \frac{y_{i,} - y_{i,pre}}{y_{i,pre}} \quad (\textrm{in percentage})
# \end{align*}

# Under the hood, the OECD tracker is trained with the real-GDP changes, 
# and thus it returns the real change, not the nominal change.

dynamic_data_link = \
    ("https://github.com/NicolasWoloszko" + 
     "/OECD-Weekly-Tracker/raw/main/Data/weekly_tracker.xlsx")
df_weekly_raw = pd.read_excel(dynamic_data_link)

# A helper function to return the `n_sundays` number of date strings 
#     of the beginning of the most recent weeks 
#     for which the data is available. 

def get_past_n_sundays(n_sundays = 5):
    date_today = datetime.datetime.now() 

    days_delta_list =  [1 + 7*(i+1) for i in range(n_sundays)]

    date_sunday_list = [(date_today - 
                         datetime.timedelta(
                             days = (each_delta + date_today.weekday())
                         )
                        )
                        for each_delta 
                        in days_delta_list]

    sunday_string_list = [each_sunday.strftime("%Y-%m-%d") 
                          for each_sunday 
                          in date_sunday_list]

    return sunday_string_list

# We have to filter only the relevant portion 
# of the original raw excel file, which is huge.

def dynamic_data_filter(n_sundays = 5):
    countries_list = ['Canada', 'France', 'Germany','Italy',
                      'Japan','United Kingdom','United States']
    weeks_list = get_past_n_sundays(n_sundays = n_sundays)
    
    df_weekly = df_weekly_raw[['region', 'date', 'Tracker (yo2y)']].copy()
    df_weekly = df_weekly.rename(columns = {"region": "Country", 
                                            "date": "Week", 
                                            "Tracker (yo2y)": "GDP_Change"})
    
    df_weekly = df_weekly[df_weekly["Week"] > '2021-10-01']
    df_weekly["Week"] = df_weekly["Week"].astype(str)
    
    df_weekly = df_weekly[df_weekly["Country"].apply(lambda x: x in countries_list)]
    df_weekly = df_weekly[df_weekly["Week"].apply(lambda x: x in weeks_list)]

    df_weekly = df_weekly.reset_index(drop = True)

    return df_weekly

df_weekly = dynamic_data_filter()
print(df_weekly.tail(8))

most_recent_week = np.flip(np.sort(df_weekly["Week"].unique()))[0]
filename_to_check = f"{most_recent_week}.parquet"
print(filename_to_check)


with os.scandir("../data") as entries:
    entry_list = list(entries)

filename_list = [each_file.name for each_file in entry_list]
print(filename_list)

if filename_to_check not in filename_list:
    df_weekly_raw.to_parquet(f"../data/{filename_to_check}")

### Dynamic Prediction 

df_estimate = pd.read_parquet("../results/df_estimate.parquet")
print('df_estimate')
print(df_estimate)

def estimate_weekly_emission(country_name, gas_name, change):
    amount = df_estimate.loc[country_name, gas_name]
    amount_week = amount*7/365
    
    coef = df_estimate.loc[country_name, f"{gas_name}_coef"]
    change_gh = change*coef

    amount_week = amount_week*(1 + change_gh/100)
    
    return amount_week, change_gh

gh_gases = ['GHG', 'CO2', 'CH4', 'N2O', 'HFC', 'PFC', 'SF6']

df_weekly = dynamic_data_filter()

for each_gas in gh_gases:
    df_weekly[f"{each_gas}_weekly"] = 0
    df_weekly[f"{each_gas}_change"] = 0


for each_gas in gh_gases:
    for index, row in df_weekly.iterrows():
        amount_week, change_gh = estimate_weekly_emission(row["Country"],
                                                          each_gas,
                                                          row["GDP_Change"])
        df_weekly.loc[index, f"{each_gas}_weekly"] = amount_week
        df_weekly.loc[index, f"{each_gas}_change"] = change_gh

print('df_weekly.tail(8)')
print(df_weekly.tail(8))

df_weekly_previous = pd.read_parquet("../results/df_weekly.parquet")
print('df_weekly_previous.tail(8)')
print(df_weekly_previous.tail(8))

most_recent_week_in_df = np.flip(np.sort(df_weekly_previous["Week"]))[0]
print('most_recent_week_in_df')
print(most_recent_week_in_df)

df_update = df_weekly[df_weekly["Week"] > most_recent_week_in_df].copy()
print('df_update')
print(df_update)

if not df_update.empty:
    df_weekly_new = pd.concat([df_weekly_previous, df_update], ignore_index = True)
    df_weekly_new.to_parquet("../results/df_weekly.parquet")
    
print('all done')