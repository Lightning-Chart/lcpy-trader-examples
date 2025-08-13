from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Defining chart types
chart_types = [
    "CandleStick",
    "Bar",
    "Line",
    "Mountain",
    "Kagi",
    "Renko",
    "HeikinAshi",
    "PointAndFigure",
]

# List to hold chart instances for each chart
charts = []

# Open all charts and store them in variables
for chart_type in chart_types:
    chart = TAChart(license_key=license_key)
    chart.load_csv(csv=DATA_PATH, dataset_name="Tesla Data")
    chart.set_price_chart_type(chart_type)
    chart.set_chart_title(chart_type)
    charts.append(chart)

# Open charts
for chart in charts:
    chart.open()
