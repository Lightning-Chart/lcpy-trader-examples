from datetime import datetime
from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Apple Inc. (AAPL) - 10y.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

chart = TAChart(license_key=license_key)

# Set chart title and theme
chart.set_chart_title('Channels')
chart.set_color_theme('turquoiseHexagon')

# Load CSV data
chart.load_csv(DATA_PATH)

# Set time range
start_time = datetime(2018, 12, 31)
end_time = datetime(2019, 12, 30)
chart.set_time_range(start_time, end_time)

# Adding Linear Regression Channel
linear_regression_channel = chart.add_linear_regression_channel(84, 51.8, 46, 39.8)
linear_regression_channel.set_channel_type(1)
linear_regression_channel.set_fill_enabled(True)
linear_regression_channel.set_line_color('#FF00FF')
linear_regression_channel.set_line_width(3)
linear_regression_channel.set_number_of_standard_deviations(2)

# Adding Parallel Channel
parallel_channel = chart.add_parallel_channel(3, 35.5, 25, 40.8, 1.7)
parallel_channel.set_fill_enabled(True)
parallel_channel.set_line_color('#7B31E9')
parallel_channel.set_line_width(3)

# Adding Pitchfork
pitchfork = chart.add_pitchfork(104, 42, 147, 46, 147, 53)

# Open Chart
chart.open()
