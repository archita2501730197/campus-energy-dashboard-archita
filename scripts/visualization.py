import matplotlib.pyplot as plt

def plot_dashboard(daily, weekly):
    fig, axes = plt.subplots(2, 2, figsize=(14,10))

    for b in daily['building'].unique():
        df_b = daily[daily['building']==b]
        axes[0,0].plot(df_b['timestamp'], df_b['kwh'], label=b)
    axes[0,0].set_title("Daily Electricity Usage")
    axes[0,0].set_xlabel("Date")
    axes[0,0].set_ylabel("kWh")
    axes[0,0].legend()
    
    avg_weekly = weekly.groupby('building')['kwh'].mean()
    axes[0,1].bar(avg_weekly.index, avg_weekly.values, color='skyblue')
    axes[0,1].set_title("Average Weekly Usage")
    axes[0,1].set_xlabel("Building")
    axes[0,1].set_ylabel("kWh")
    
    axes[1,0].scatter(daily['timestamp'], daily['kwh'], color='red')
    axes[1,0].set_title("Daily Peak Consumption")
    axes[1,0].set_xlabel("Date")
    axes[1,0].set_ylabel("kWh")
    
    plt.tight_layout()
    plt.savefig('../output/dashboard.png')
    plt.show()
    print("Dashboard saved as ../output/dashboard.png")

if __name__ == "__main__":
    import pandas as pd

    # Sample daily and weekly data
    daily = pd.DataFrame({
        'timestamp': pd.date_range(start='2025-01-01', periods=3, freq='D'),
        'kwh': [120, 130, 125],
        'building': ['BuildingA']*3
    })

    weekly = pd.DataFrame({
        'timestamp': pd.date_range(start='2025-01-01', periods=3, freq='W'),
        'kwh': [375, 380, 390],
        'building': ['BuildingA']*3
    })

    plot_dashboard(daily, weekly)
