from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Defining a list of envelope indicators
envelope_indicators = [
    'BollingerBand',
    'DonchianChannels',
    'FractalChaosBands',
    'HighLowBands',
    'KeltnerChannels',
    'MovingAverageEnvelopes',
    'PrimeNumberBands',
    'StandardErrorBands',
    'StollerAverageRangeChannel',
]

# List to hold chart instances for each chart
charts = []

# Open all charts and store them in variables
for indicator_name in envelope_indicators:
    chart = TAChart(license_key=license_key)

    # Load the CSV data
    chart.load_csv(csv=DATA_PATH, dataset_name='Tesla Data')

    # Defining chart type
    chart.set_price_chart_type('CandleStick')

    # Set the chart title as the indicator name
    chart.set_chart_title(indicator_name)

    # Add the indicators to chart
    if indicator_name == 'MovingAverageEnvelopes':
        chart.add_moving_average_envelopes(period_count=20)
    elif indicator_name == 'KeltnerChannels':
        chart.add_keltner_channels()
    elif indicator_name == 'StollerAverageRangeChannel':
        chart.add_stoller_average_range_channel()
    elif indicator_name == 'BollingerBand':
        chart.add_bollinger_band(period_count=20)
    elif indicator_name == 'DonchianChannels':
        chart.add_donchian_channels(period_count=20)
    elif indicator_name == 'FractalChaosBands':
        chart.add_fractal_chaos_bands()
    elif indicator_name == 'HighLowBands':
        chart.add_high_low_bands()
    elif indicator_name == 'PrimeNumberBands':
        chart.add_prime_number_bands()
    elif indicator_name == 'StandardErrorBands':
        chart.add_standard_error_bands()

    # Add chart instances to the list to prepare for display
    charts.append(chart)

# Open charts
for chart in charts:
    chart.open()