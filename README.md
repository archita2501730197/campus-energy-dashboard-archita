# Campus Energy Dashboard

## Objective

This project is about analyzing electricity usage in campus buildings.  
The goal is to help the campus facilities team save energy by understanding usage patterns.  
We read building meter data, calculate daily and weekly totals, create summaries, and make a dashboard with charts.

## Dataset

- The dataset contains CSV files for each building.
- Each CSV has columns: `timestamp` and `energy` (kWh).
- Example file names: `buildingA.csv`, `buildingB.csv`.
- Data is stored in `/data/` folder.

## Methodology

1. **Data Ingestion**:

   - All CSV files are read using Python `pandas`.
   - Missing columns like building or month are added automatically.

2. **Data Aggregation**:

   - Daily totals, weekly totals, and building summaries are calculated.
   - Functions are used to simplify calculations.

3. **Object-Oriented Modeling**:

   - `MeterReading` stores each reading.
   - `Building` stores all readings of one building and calculates totals.
   - `BuildingManager` manages all buildings and gives overall summaries.

4. **Visualization**:

   - Dashboard with 3 charts:
     - Line chart for daily consumption
     - Bar chart for average weekly usage
     - Scatter plot for daily peaks
   - Dashboard saved as `dashboard.png` in `/output/`.

5. **Outputs**:
   - Cleaned combined data: `cleaned_energy_data.csv`
   - Building summary: `building_summary.csv`
   - Text summary report: `summary.txt`

## Insights

- Shows which building consumes the most energy.
- Highlights peak hours of electricity usage.
- Helps plan energy saving actions for the campus.

## How to Run

1. Open terminal in `/scripts/` folder.
2. Run the main program:
