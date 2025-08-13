from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Apple Inc. (AAPL) - 10y.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

chart = TAChart(license_key=license_key)

# Set chart title and theme
chart.set_chart_title('Watermark Example')
chart.set_color_theme('cyberSpace')

# Load CSV data for Apple Inc.
chart.load_csv(DATA_PATH)

# Enabling watermark using the symbol name "AAPL"
chart.show_symbol_watermark(True)
chart.set_watermark_text('AAPL')

# Open the chart
chart.open()
