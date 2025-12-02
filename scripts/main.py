import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# combine CSV files
def load_data():
    print("Reading data from CSV files...")
    folder = Path("../data")
    all_files = folder.glob("*.csv")
    dataframes = []

    for file in all_files:
        try:
            df = pd.read_csv(file)
            if "timestamp" in df.columns and "energy" in df.columns:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
                df["building"] = file.stem
                dataframes.append(df)
            else:
                print(f"Column mismatch in {file.name}. Expected ['timestamp', 'energy']")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if dataframes:
        print("Data loaded successfully")
        return pd.concat(dataframes, ignore_index=True)
    else:
        print("No data found, please check the /data/ folder")
        return None


# Calculations
def daily_totals(df):
    return df.resample("D", on="timestamp")["energy"].sum()

def weekly_totals(df):
    return df.resample("W", on="timestamp")["energy"].sum()

def building_summary(df):
    return df.groupby("building")["energy"].agg(["mean", "min", "max", "sum"])


# Save files
def save_output(df, summary):
    output = Path("../output")
    output.mkdir(exist_ok=True)
    df.to_csv(output / "cleaned_energy_data.csv", index=False)
    summary.to_csv(output / "building_summary.csv")

    with open(output / "summary.txt", "w") as f:
        total = df["energy"].sum()
        highest = summary["sum"].idxmax()
        peak = df.loc[df["energy"].idxmax(), "timestamp"]

        f.write("Campus Energy Dashboard Summary Report\n")
        f.write(f"Total Energy Used: {total} kWh\n")
        f.write(f"Top Consuming Building: {highest}\n")
        f.write(f"Peak Usage Time: {peak}\n")

    print("Output files saved in /output folder")


# Graph 
def create_dashboard(df):
    print("Creating dashboard...")

    daily = daily_totals(df)
    summ = building_summary(df)

    fig, ax = plt.subplots(3, 1, figsize=(10, 12))

    ax[0].plot(daily.index, daily.values)
    ax[0].set_title("Daily Consumption")

    ax[1].bar(summ.index, summ["mean"])
    ax[1].set_title("Average Usage")

    ax[2].scatter(df["timestamp"], df["energy"])
    ax[2].set_title("Hourly Readings")

    plt.tight_layout()
    plt.savefig("../output/dashboard.png")
    print("Dashboard saved")


# Main function
def main():
    df = load_data()
    if df is not None:
        summary = building_summary(df)
        save_output(df, summary)
        create_dashboard(df)


if __name__ == "__main__":
    main()
