from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Defining oscillator groups
oscillator_groups = [
    [
        'accumulation_distribution',
        'chaikin_money_flow',
        'chaikin_oscillator',
        'ease_of_movement',
    ],
    [
        'elders_force_index',
        'klinger_volume_oscillator',
        'market_facilitation_index',
        'money_flow_index',
    ],
    [
        'negative_volume_index',
        'on_balance_volume',
        'positive_volume_index',
        'price_volume_trend',
    ],
    ['trade_volume_index', 'twiggs_money_flow', 'volume', 'volume_oscillator'],
    ['volume_rate_of_change', 'williams_accumulation_distribution', 'wvad'],
]

# Step 4: Create each oscillator group in a separated sub-charts
charts = []

# Loop through each oscillator group
for i, indicators in enumerate(oscillator_groups, start=1):
    chart = TAChart(license_key=license_key)
    chart.load_csv(
        csv=DATA_PATH, dataset_name=f'Tesla Data - Oscillator Group {i}'
    )
    chart.set_price_chart_type('CandleStick')

    # Configure indicators
    for indicator_name in indicators:
        if indicator_name == 'accumulation_distribution':
            chart.add_accumulation_distribution()
        elif indicator_name == 'chaikin_money_flow':
            chart.add_chaikin_money_flow(period_count=21)
        elif indicator_name == 'chaikin_oscillator':
            chart.add_chaikin_oscillator(fast_period_count=3, slow_period_count=10)
        elif indicator_name == 'ease_of_movement':
            chart.add_ease_of_movement()
        elif indicator_name == 'elders_force_index':
            chart.add_elders_force_index(period_count=13)
        elif indicator_name == 'klinger_volume_oscillator':
            chart.add_klinger_volume_oscillator()
        elif indicator_name == 'market_facilitation_index':
            chart.add_market_facilitation_index()
        elif indicator_name == 'money_flow_index':
            chart.add_money_flow_index(period_count=14)
        elif indicator_name == 'negative_volume_index':
            chart.add_negative_volume_index()
        elif indicator_name == 'on_balance_volume':
            chart.add_on_balance_volume()
        elif indicator_name == 'positive_volume_index':
            chart.add_positive_volume_index()
        elif indicator_name == 'price_volume_trend':
            chart.add_price_volume_trend()
        elif indicator_name == 'trade_volume_index':
            chart.add_trade_volume_index()
        elif indicator_name == 'twiggs_money_flow':
            chart.add_twiggs_money_flow()
        elif indicator_name == 'volume':
            chart.add_volume()
        elif indicator_name == 'volume_oscillator':
            chart.add_volume_oscillator()
        elif indicator_name == 'volume_rate_of_change':
            chart.add_volume_rate_of_change()
        elif indicator_name == 'williams_accumulation_distribution':
            chart.add_williams_accumulation_distribution()
        elif indicator_name == 'wvad':
            chart.add_williams_variable_accumulation_distribution()

    # Add chart instances to the list to prepare for display
    charts.append(chart)

# Open charts
for chart in charts:
    chart.open()
