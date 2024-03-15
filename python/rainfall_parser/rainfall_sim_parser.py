import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt


def plot(df, title="title", series_label="series1"):
    plt.figure(figsize=(12, 6))
    plt.plot(df.iloc[:, 0], df.iloc[:, 1], label=series_label)
    # plt.plot(df['DateTime'], df['Runoff (mm/hr)'], label='Runoff (mm/hr)')
    plt.xlabel('Date Time')
    plt.ylabel('Values')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def extract_raw_timeseries(df, site_id, year, plot_number, condition, column_name):
    """
    reads timeseries data from a subset of the input data
    The input data column 'Time' is fractional number of minutes
    that can reset to zero to represent 60.
    """
    print(df.dtypes['Year'])
    filtered_data = df[(df["Site ID"] == site_id) & (df["Year"] == year)
                       & (df["Plot number"] == plot_number)
                       & (df["Condition"].str.strip() == condition)
                       ]

    keeper_rows = []
    extra_t = 0  # used to accumulate minutes, when the fractional minutes 'Time' column resets with 0
    for index, row in filtered_data.iterrows():
        year = row['Year']
        month = row['Month']
        day = row['Day']
        time = row['Time']
        if time == 0:
            extra_t = extra_t + 60
        date = datetime(year=int(year), month=int(month), day=int(day))
        t = date + timedelta(minutes=time + extra_t)

        keeper_rows.append([t, row[column_name]])
        # print(f"{t},{row['Precipitation (mm/hr)']},{row['Runoff (mm/hr)']}")
    return pandas.DataFrame(keeper_rows, columns=['timestamp', column_name])


def filter_out_timesteps_less_than_1minute(df):
    # Calculate time difference between consecutive rows
    df['time_diff'] = df['timestamp'].diff()
    # Filter out rows with time steps less than 1 minute
    df_filtered = df[df['time_diff'] >= pandas.Timedelta(minutes=1)]
    # Drop the 'time_diff' column if not needed
    df_filtered = df_filtered.drop(columns=['time_diff'])
    return df_filtered


FILENAME = 'rainfall_sim.csv'
SITEID = "Ab"
PLOT_NUMBER = 2
YEAR = 2004
CONDITION = 'N'
SERIES_NAME = 'Precipitation (mm/hr)'

data = pandas.read_csv(FILENAME)
ts_raw = extract_raw_timeseries(data, SITEID, YEAR, PLOT_NUMBER, CONDITION, SERIES_NAME)
#print(ts_raw.to_string())

ts_filter = filter_out_timesteps_less_than_1minute(ts_raw)
#print(ts_filter.to_string())

ts_filter['2'] = ts_raw[SERIES_NAME]
print(ts_filter.to_string())
plt.figure(figsize=(16, 8), dpi=150)
ts_filter.plot(label='H', color=['orange', 'green'])
plt.title('Price Plot')
plt.xlabel('Years')
plt.legend()
plt.show()
#plot(ts_combined, title=f"{SITEID} {YEAR} plot:{PLOT_NUMBER}", series_label=SERIES_NAME)
#plot(ts_raw, title=f"{SITEID} {YEAR} plot:{PLOT_NUMBER}", series_label=SERIES_NAME)
#plot(ts_filter, title=f"{SITEID} {YEAR} plot:{PLOT_NUMBER}", series_label=SERIES_NAME)
