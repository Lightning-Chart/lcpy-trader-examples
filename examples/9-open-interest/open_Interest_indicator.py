from datetime import datetime
from lightningchart_trader import TAChart
import csv

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Tesla_with_open_interest.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# # Create the trader chart
open_interest_chart = TAChart(license_key=license_key)
open_interest_chart.set_chart_title('Microsoft Data - Open Interest')

# Read the data from the CSV file
data = []
with open(DATA_PATH, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(
            {
                'open': float(row['Open']),
                'high': float(row['High']),
                'low': float(row['Low']),
                'close': float(row['Close']),
                'dateTime': datetime.strptime(row['Date'], '%m/%d/%Y'),
                'volume': int(row['Volume']),
                'openInterest': int(row['Open Interest']),
            }
        )

# Set the data
open_interest_chart.set_data(data)

# Add the Open Interest indicator
open_interest = open_interest_chart.add_open_interest()
open_interest.set_line_color('#FF4500')
open_interest.set_line_width(1)

# Open the chart
open_interest_chart.open()
