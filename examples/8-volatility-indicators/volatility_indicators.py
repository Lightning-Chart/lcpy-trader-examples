from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Initializing
volatility_chart = TAChart(license_key=license_key)
volatility_chart.load_csv(csv=DATA_PATH)
volatility_chart.set_price_chart_type('CandleStick')
volatility_chart.set_chart_title('Tesla Data - Volatility Indicators')

# Add volatility indicators to the chart
volatility_chart.add_average_true_range(period_count=14)
volatility_chart.add_chaikin_volatility()
volatility_chart.add_ehler_fisher_transform()
volatility_chart.add_high_minus_low()
volatility_chart.add_historical_volatility_index()
volatility_chart.add_mass_index(period_count=25)
volatility_chart.add_z_value(period_count=20)

# Open chart
volatility_chart.open()
