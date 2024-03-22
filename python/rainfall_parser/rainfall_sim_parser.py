import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from datetime import datetime, timedelta
import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_data_frames(data_frames, labels, markers, title):
    # Plot the data frames
    for df, label, marker in zip(data_frames, labels, markers):
        for column in df.columns:
            plt.plot(df.index, df[column], label=label, marker=marker)

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(title)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.legend()
    plt.show()


def extract_raw_timeseries(df, site_id, year, plot_number, condition, column_name):
    """
    reads timeseries data from a subset of the input data
    The input data column 'Time' is fractional number of minutes
    that can reset to zero to represent 60.
    """
    filtered_data = df[(df["Site ID"] == site_id) & (df["Year"] == year)
                       & (df["Plot number"] == plot_number)
                       & (df["Condition"].str.strip() == condition)
                       ].reset_index(drop=True)

    rows = []
    extra_t = 0  # used to accumulate minutes, when the fractional minutes 'Time' column resets with 0
    for index, row in filtered_data.iterrows():
        year = row['Year']
        month = row['Month']
        day = row['Day']
        time = row['Time']
        if time == 0 and index != 0:
            extra_t = extra_t + 60
        date = datetime(year=int(year), month=int(month), day=int(day))
        t = date + timedelta(minutes=time + extra_t)

        rows.append([t, row[column_name]])
        # print(f"{t},{row['Precipitation (mm/hr)']},{row['Runoff (mm/hr)']}")
    out = pandas.DataFrame(rows, columns=['timestamp', column_name])
    out.set_index('timestamp', inplace=True)
    return out


def filter_out_timesteps_less_than_1minute(df):
    # Calculate time difference between consecutive rows
    df['time_diff'] = df['timestamp'].diff()
    # Filter out rows with time steps less than 1 minute
    df_filtered = df[df['time_diff'] >= pandas.Timedelta(minutes=1)]
    # Drop the 'time_diff' column if not needed
    df_filtered = df_filtered.drop(columns=['time_diff'])
    return df_filtered


def condition_timeseries_to_precip(df):
    data_column = df.columns[0]
    modified_df = df.copy()  # Create a copy of the input DataFrame
    prev_row = None

    for t, row in df.iterrows():

        have_prev_precip = prev_row is not None and prev_row[data_column] != 0
        precip_stopped = row[data_column] == 0 and have_prev_precip
        precip_started = prev_row is not None and row[data_column] != 0 and prev_row[data_column] == 0
        more_than_1minute_gap = prev_row is not None and t - prev_row.name > timedelta(minutes=1)

        if precip_started:
            print("precip started")

        if precip_stopped and more_than_1minute_gap:
            print(f"Found value 0 at time: {t}, previous precip = {prev_row[data_column]}")
            new_time = t - timedelta(minutes=1)
            new_entry = prev_row.copy()
            modified_df.loc[new_time] = new_entry
        elif precip_started and more_than_1minute_gap:
            print(f"precip started with {row[data_column]}, at time: {t}, previous precip = {prev_row[data_column]}")
            new_time = t - timedelta(seconds=15)
            modified_df.loc[new_time] = 0

        prev_row = row

    modified_df.sort_index(inplace=True)
    return modified_df

def interpolate_1minute_timeseries(df):
    s = df.resample('1min').ffill()
    return s

FILENAME = 'rainfall_sim.csv'
OUTPUT_FILENAME = 'out.csv'
SITEID = "Ab"
PLOT_NUMBER = 1
YEAR = 2004
CONDITION = 'N'
SERIES_NAME = 'Precipitation (mm/hr)'

data = pandas.read_csv(FILENAME)
raw_ts = extract_raw_timeseries(data, SITEID, YEAR, PLOT_NUMBER, CONDITION, SERIES_NAME)
# print(raw_ts.to_string())
print(f"raw data has {raw_ts.size} rows")
# detect precipitation going off - (use previous precipitation one minute prior to zero )
# insert values to enhance interpolation
ts_conditioned = condition_timeseries_to_precip(raw_ts)
ts_1minute = interpolate_1minute_timeseries(ts_conditioned)
#print(ts_1minute.to_string())

ts_1minute.to_csv(OUTPUT_FILENAME)
combined_df = pandas.concat([raw_ts, ts_conditioned, ts_1minute], axis=1)
combined_df.to_csv('combined_data.csv')

title = f"{SITEID} {YEAR} plot number:{PLOT_NUMBER} condition:{CONDITION} "
plot_data_frames([raw_ts, ts_conditioned,ts_1minute],["raw","conditioned","1minute"],['o','x','*'],title)

# ts_filter = filter_out_timesteps_less_than_1minute(ts_raw)
# print(ts_filter.to_string())
