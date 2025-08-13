from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Initializing the main price chart with Ichimoku Cloud and Supertrend
ichimoku_chart = TAChart(license_key=license_key)
ichimoku_chart.load_csv(csv=DATA_PATH)
ichimoku_chart.set_price_chart_type("CandleStick")
ichimoku_chart.set_chart_title("Ichimoku Cloud and First Half Trend Indicators")
ichimoku_chart.add_ichimoku_cloud()

supertrend_chart = TAChart(license_key=license_key)
supertrend_chart.load_csv(csv=DATA_PATH)
supertrend_chart.set_price_chart_type("CandleStick")
supertrend_chart.set_chart_title("Supertrend and Second Half Trend Indicators")
supertrend_chart.add_super_trend(period_count=14)

# Defining trend indicators for each chart
trend_indicators_chart1 = [
    "asi",
    "adx",
    "aroon",
    "gapo",
    "linear_regression",
    "parabolic_sar",
    "random_walk_index",
]
trend_indicators_chart2 = [
    "ravi",
    "schaff_trend_cycle",
    "stc_signal",
    "sqn_trend",
    "swing_index",
    "trix",
    "vhf",
]

# Adding indicators to Chart 1
for indicator_name in trend_indicators_chart1:
    if indicator_name == "asi":
        ichimoku_chart.add_accumulative_swing_index()
    elif indicator_name == "adx":
        ichimoku_chart.add_average_directional_index(period_count=14)  #
    elif indicator_name == "aroon":
        ichimoku_chart.add_aroon(period_count=14)
    elif indicator_name == "gapo":
        ichimoku_chart.add_gopalakrishnan_range_index(period_count=14)
    elif indicator_name == "linear_regression":
        ichimoku_chart.add_linear_regression()
    elif indicator_name == "parabolic_sar":
        ichimoku_chart.add_parabolic_sar()
    elif indicator_name == "random_walk_index":
        ichimoku_chart.add_random_walk_index()

# Adding indicators to Chart 2
for indicator_name in trend_indicators_chart2:
    if indicator_name == "ravi":
        supertrend_chart.add_range_action_verification_index()
    elif indicator_name == "schaff_trend_cycle":
        supertrend_chart.add_schaff_trend_cycle()
    elif indicator_name == "stc_signal":
        supertrend_chart.add_schaff_trend_cycle_signal()
    elif indicator_name == "sqn_trend":
        supertrend_chart.add_sqn_trend()
    elif indicator_name == "swing_index":
        supertrend_chart.add_swing_index()
    elif indicator_name == "trix":
        supertrend_chart.add_triangular_moving_average(period_count=14)
    elif indicator_name == "vhf":
        supertrend_chart.add_vertical_horizontal_filter(period_count=14)

# Open charts
ichimoku_chart.open()
supertrend_chart.open()
