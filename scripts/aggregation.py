# Functions to calculate daily, weekly totals and building summaries

import pandas as pd

def daily_totals(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    daily = df.groupby('building').resample('D', on='timestamp')['kwh'].sum().reset_index()
    return daily

def weekly_totals(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    weekly = df.groupby('building').resample('W', on='timestamp')['kwh'].sum().reset_index()
    return weekly

def building_summary(df):
    summary = df.groupby('building')['kwh'].agg(['mean', 'min', 'max', 'sum']).reset_index()
    return summary

if __name__ == "__main__":
    print("aggregation.py is running correctly")
