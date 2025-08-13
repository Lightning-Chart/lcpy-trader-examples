from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
AAPL_DATA_PATH = "data/Apple Inc. (AAPL) - 10y.csv"
NVDIA_DATA_PATH = "data/NVIDIA Corp (NVDA) - 10y.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Create two separate instances of TAChart for two different charts
aapl_trader = TAChart(license_key)
nvidia_trader = TAChart(license_key)

# Read data from CSV files
aapl_trader.load_csv(AAPL_DATA_PATH)
aapl_trader.change_time_range(3)
aapl_trader.set_chart_title(
    'Fibonacci Fan, Fibonacci Retracements, Fibonacci Time Zones'
)

nvidia_trader.load_csv(NVDIA_DATA_PATH)
nvidia_trader.change_time_range(4)
nvidia_trader.set_chart_title('Fibonacci Arc, Fibonacci Extension')

# AAPL Chart - Fibonacci Fan, Retracements, and Time Zones

# Add Fibonacci Fan
fibonacci_fan = aapl_trader.add_fibonacci_fan(500, 35.5, 555, 52)
fibonacci_fan.set_fill_enabled(True)
fibonacci_fan.set_line_color('#0000FF')
fibonacci_fan.set_line_width(2)
fibonacci_fan.update_position(505, 34, 585, 51.5)

# Add Fibonacci Retracements with fill disabled
fibonacci_retracements = aapl_trader.add_fibonacci_retracements(50, 100, 150, 200)
fibonacci_retracements.set_fill_enabled(False)
fibonacci_retracements.set_line_color('#FF00FF')
fibonacci_retracements.set_line_width(2)
fibonacci_retracements.update_position(335, 38, 442, 56)

# # Add Fibonacci Time Zones with fill disabled
fibonacci_time_zones = aapl_trader.add_fibonacci_time_zones(50, 100, 150, 200)
fibonacci_time_zones.set_fill_enabled(False)
fibonacci_time_zones.set_line_color('#FFFF00')
fibonacci_time_zones.set_line_width(2)
fibonacci_time_zones.set_time_zone_count(10)
fibonacci_time_zones.update_position(4, 27, 95, 36.5)

# Add Fibonacci Arc
fibonacci_arc = nvidia_trader.add_fibonacci_arc(50, 100, 150, 200)
fibonacci_arc.set_fill_enabled(True)
fibonacci_arc.set_line_color('#FF0000')
fibonacci_arc.set_line_width(2)
fibonacci_arc.update_position(19, 32.5, 36, 39.4)

# Add Fibonacci Extension
fibonacci_extension = nvidia_trader.add_fibonacci_extension(
    105, 33, 141, 44.4, 157, 36.5
)
fibonacci_extension.set_extend_lines(True)
fibonacci_extension.set_fill_enabled(True)
fibonacci_extension.set_line_color('#00FF00')
fibonacci_extension.set_line_width(1)
fibonacci_extension.update_position(105, 33, 141, 44.4, 300, 36.5)

# Open the AAPL chart
aapl_chart = aapl_trader.open()
nvidia_chart = nvidia_trader.open()
