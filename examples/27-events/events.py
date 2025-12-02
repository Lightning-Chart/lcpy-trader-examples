from lightningchart_trader import TAChart
from datetime import datetime

LICENSE_KEY_PATH = "license_key.txt"
DATA_PATH = "data/Alphabet Inc - Class A (GOOGL) - 10y.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

trader = TAChart(license_key)
dashboard = trader.create_dashboard(rows=3, cols=40)

main_chart = dashboard.add_chart(
    chart_type='CandleStick',
    title='Line Drawing Tools',
    row_index=0,
    column_index=0,
    row_span=3,
    column_span=40,
).load_csv(csv=DATA_PATH)

overlay_chart = dashboard.add_chart(
    chart_type='Line',
    title='Overlay Chart',
    row_index=0,
    column_index=28,
    column_span=10,
).load_csv(csv=DATA_PATH)

main_chart.change_time_range(4)
overlay_chart.change_time_range(4)

# Extended line
extended_line = main_chart.add_extended_line(124, 54, 105, 52)
extended_line.set_extend_lines(True, True)
extended_line.set_line_color('#a302ed')
extended_line.set_line_width(2)

# Green horizontal line
horizontal_line_2 = main_chart.add_horizontal_line(64.85)
horizontal_line_2.set_line_color('#0AFC22')
horizontal_line_2.set_line_width(2)

# Red horizontal line
horizontal_line_1 = main_chart.add_horizontal_line(51.9)
horizontal_line_1.set_line_color('#f70844')
horizontal_line_1.set_line_width(2)

# Trend line
trend_line = main_chart.add_trend_line(79, 63.8, 1.6, 51.2)
trend_line.set_line_width(2)

# Vertical line
vertical_line = main_chart.add_vertical_line(81)
vertical_line.set_line_color('#0AFC22')
vertical_line.set_line_width(2)

# Horizontal ray
horizontal_ray_line = main_chart.add_horizontal_ray(142.9, 62.2)
horizontal_ray_line.set_line_color('#0A22FC')
horizontal_ray_line.set_line_width(2)

def on_extended_line_click(e):
    sma10 = overlay_chart.add_simple_moving_average(10)
    sma10.set_line_color('#FF0000')

def on_trend_line_click(e):
    sma20 = overlay_chart.add_simple_moving_average(20)
    sma20.set_line_color('#00FFFF')

def on_green_horizontal_click(e):
    start_time = datetime(2018, 6, 1)
    end_time   = datetime(2018, 12, 31)

    overlay_chart.set_time_range(start_time, end_time)

# Attach callbacks
extended_line.on_pointer_down(on_extended_line_click)
trend_line.on_pointer_down(on_trend_line_click)
horizontal_line_2.on_pointer_down(on_green_horizontal_click)

# Open dashboard
trader.open()
