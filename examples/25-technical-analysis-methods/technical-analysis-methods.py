import csv
from lightningchart_trader import TAChart

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Alphabet Inc (GOOGL).csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Initialize chart
trader = TAChart(license_key=license_key)
trader.set_chart_title("TechnicalAnalysisMethods")

# Load CSV data
trader.load_csv(DATA_PATH)

# Read CSV data into arrays
closes = []
highs = []
lows = []
volumes = []

with open(DATA_PATH, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        closes.append(float(row['Close']))
        highs.append(float(row['High']))
        lows.append(float(row['Low']))
        volumes.append(int(row['Volume']))

trader.open()

# Create TechnicalAnalysisMethods instance
ta_methods = trader.technical_analysis_methods()

# Add custom overlay 
overlay = trader.add_custom_overlay()
overlay.set_line_color('#30EE50')
overlay.set_name('WWS + Z-Value')
overlay.set_offset(13)

# Calculate individual values
wws_values = ta_methods.calculate_welles_wilder_smoothing(closes, n=14)
zv_values = ta_methods.calculate_z_value(closes, n=14, movingAverageType=0)

# Combine with manual calculation
co_values = []
min_length = min(len(wws_values), len(zv_values))
for i in range(min_length):
    co_values.append(wws_values[i] + zv_values[i])

# Set data to overlay
overlay.set_data(co_values)

# Add custom study
study = trader.add_custom_study()
study.set_line_color('#EE3050')
study.set_name('WAD / SD')
study.set_offset(13)

# Calculate individual values for study
wad_values = ta_methods.calculate_williams_accumulation_distribution(
    close_values=closes,
    high_values=highs,
    low_values=lows,
    volumes=volumes,
    use_volume=True,
)
sd_values = ta_methods.calculate_standard_deviation(closes, n=14, movingAverageType=0)

# Combine with manual calculation
cs_values = []
max_offset = 12
for i in range(len(sd_values)):
    if i + max_offset < len(wad_values):
        cs_values.append(wad_values[i + max_offset] / sd_values[i])

# Set data to study
study.set_data(cs_values)