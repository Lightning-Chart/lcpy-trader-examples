from lightningchart_trader import TAChart
from datetime import datetime

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Initialize the charts list
charts = []

# Chart for GannFan
trader_gann_fan = TAChart(license_key=license_key)
trader_gann_fan.load_csv(DATA_PATH)
trader_gann_fan.set_price_chart_type('CandleStick')
trader_gann_fan.set_chart_title('Gann Fan')

# Set time range
start_time = datetime(2012, 12, 17)
end_time = datetime(2013, 12, 16)
trader_gann_fan.set_time_range(start_time, end_time)

# Adding Gann Fan to this chart
gann_fan = trader_gann_fan.add_gann_fan(
    startX=81,
    startY=152,
    endX=103,
    endY=193,
    lineColor='#FF0000',
    lineWidth=2,  # Line width
)
gann_fan.set_magnetic(True)  # Enable snapping to OHLC data points

# Add the GannFan chart to charts
charts.append(trader_gann_fan)

# Chart for GannBox
trader_gann_box = TAChart(license_key=license_key)
trader_gann_box.load_csv(DATA_PATH)
trader_gann_box.set_price_chart_type('CandleStick')
trader_gann_box.set_chart_title('Gann Box')

# Set time range
start_time = datetime(2012, 12, 17)
end_time = datetime(2013, 12, 16)
trader_gann_box.set_time_range(start_time, end_time)

# Adding Gann Box to this chart
gann_box = trader_gann_box.add_gann_box(
    startX=81,
    startY=153.5,
    endX=137,
    endY=292,
    lineColor='#FF0000',
    lineWidth=2,
    areaColor='#FFD70088',
)
gann_box.set_magnetic(True)

# Add the GannBox chart to charts
charts.append(trader_gann_box)

# Open charts
for chart in charts:
    chart.open()
