from lightningchart_trader import TAChart
from datetime import datetime

# Load the license key
LICENSE_KEY_PATH = "license_key.txt"
AAPL_DATA_PATH = "data/Apple Inc. (AAPL) - 10y.csv"
TESLA_DATA_PATH = "data/Tesla.csv"
NVDIA_DATA_PATH = "data/NVIDIA Corp (NVDA) - 10y.csv"

# Load the license key
license_key = open(LICENSE_KEY_PATH).read()

# Create four separate instances of TAChart for four different charts
aapl_trader = TAChart(license_key)
tesla_trader = TAChart(license_key)
nvidia_trader = TAChart(license_key)
patterns_trader = TAChart(license_key)

# Chart 1: AAPL - Cycle Lines, Sine Wave, and Elliot Wave Patterns
aapl_trader.load_csv(AAPL_DATA_PATH)
aapl_trader.set_chart_title('Cycle Lines, Sine Wave and Elliot Wave Patterns')
aapl_trader.set_color_theme('cyberSpace')

# Set time range
start_time = datetime(2018, 12, 31)
end_time = datetime(2019, 12, 30)
aapl_trader.set_time_range(start_time, end_time)

cycle_lines = aapl_trader.add_cycle_lines(83, 50.7, 105, 41.6)
cycle_lines.set_time_zone_count(5)
cycle_lines.set_line_color('#FFFF00')  # Yellow color
cycle_lines.set_line_width(2)
cycle_lines.set_fill_enabled(False)

sine_wave = aapl_trader.add_sine_wave(83, 54.6, 105, 50.0)
sine_wave.set_magnetic(True)
sine_wave.set_smoothness(5)
sine_wave.set_line_color('#F087FF')  # Light pink color
sine_wave.set_line_width(2)

elliot_wave = aapl_trader.add_elliot_wave(
    waveType=0,
    startX=2,
    startY=34.0,
    secondX=12,
    secondY=37.7,
    thirdX=16,
    thirdY=36.3,
    fourthX=25,
    fourthY=41.9,
    fifthX=27,
    fifthY=40.4,
    sixthX=42,
    sixthY=42.6,
    seventhX=46,
    seventhY=40.7,
    eighthX=56,
    eighthY=47.4,
    ninthX=58,
    ninthY=44.1,
)
elliot_wave.set_line_color('#00FF00')  # Green color
elliot_wave.set_line_width(2)

# Chart 2: Tesla - Head and Shoulders
tesla_trader.load_csv(TESLA_DATA_PATH)
tesla_trader.set_chart_title('Head and Shoulders')
tesla_trader.set_color_theme('cyberSpace')

# Set time range
start_time = datetime(2012, 12, 17)
end_time = datetime(2013, 12, 16)
tesla_trader.set_time_range(start_time, end_time)

head_and_shoulders = tesla_trader.add_head_and_shoulders(
    6, 109.1, 34, 216.3, 89, 158.4, 138, 295.5, 160, 216.9, 177, 274.8, 211, 201.1
)

# Chart 3: Tesla - Triangle and XABCD Patterns
tesla_trader2 = TAChart(license_key)
tesla_trader2.load_csv(TESLA_DATA_PATH)
tesla_trader2.set_chart_title('Triangle and XABCD Patterns')
tesla_trader2.set_color_theme('cyberSpace')

# Set time range
start_time = datetime(2012, 12, 17)
end_time = datetime(2013, 12, 16)
tesla_trader2.set_time_range(start_time, end_time)

xabcd_pattern = tesla_trader2.add_xabcd_pattern(
    84, 154.9, 138, 295.8, 160, 213.8, 178, 276.6, 210, 196.5
)
triangle = tesla_trader2.add_triangle(6, 106.5, 51, 172.7, 34, 212.4)
triangle.set_line_color('#FF99FF')
triangle.set_line_width(3)
triangle.set_magnetic(True)

# Chart 4: NVIDIA - Patterns and Shapes
nvidia_trader.load_csv(NVDIA_DATA_PATH)
nvidia_trader.set_chart_title('Patterns and Shapes')
nvidia_trader.set_color_theme('cyberSpace')

# Set time range
start_time = datetime(2018, 12, 31)
end_time = datetime(2019, 12, 31)
nvidia_trader.set_time_range(start_time, end_time)

elliot_wave_impulse = nvidia_trader.add_elliot_wave(
    waveType=1,
    startX=19,
    startY=32.6,
    secondX=25,
    secondY=38.7,
    thirdX=27,
    thirdY=35.8,
    fourthX=32,
    fourthY=40.5,
    fifthX=35,
    fifthY=38.3,
    sixthX=37,
    sixthY=40.9,
    seventhX=37,
    seventhY=40.9,
    eighthX=37,
    eighthY=40.9,
    ninthX=37,
    ninthY=40.9,
)
elliot_wave_impulse.set_line_color('#00FF00')
elliot_wave_impulse.set_line_width(2)

elliot_wave_Correction = nvidia_trader.add_elliot_wave(
    waveType=4,
    startX=78,
    startY=47.8,
    secondX=80,
    secondY=43.1,
    thirdX=84,
    thirdY=46.0,
    fourthX=105,
    fourthY=33.0,
    fifthX=105,
    fifthY=33.0,
    sixthX=105,
    sixthY=33.0,
    seventhX=105,
    seventhY=33.0,
    eighthX=105,
    eighthY=33.0,
    ninthX=105,
    ninthY=33.0,
)
elliot_wave_Correction.set_line_color('#22e225')
elliot_wave_Correction.set_line_width(2)

# Adding Triple Combo Wave
elliot_wave_TripleCombo = nvidia_trader.add_elliot_wave(
    waveType=3,
    startX=157,
    startY=36.6,
    secondX=161,
    secondY=43.2,
    thirdX=166,
    thirdY=39.5,
    fourthX=176,
    fourthY=46.8,
    fifthX=187,
    fifthY=42.2,
    sixthX=193,
    sixthY=46.8,
    seventhX=192,
    seventhY=46.8,
    eighthX=192,
    eighthY=46.8,
    ninthX=192,
    ninthY=46.8,
)
elliot_wave_TripleCombo.set_line_color('#da21f2')
elliot_wave_TripleCombo.set_line_width(2)

rectangle = nvidia_trader.add_rectangle(16, 31.7, 41, 42.8)
rectangle.set_line_color('#FF00FF')

triangle = nvidia_trader.add_triangle(61, 50, 106, 47, 106, 31)
triangle.set_line_color('#FF9933')

ellipse = nvidia_trader.add_ellipse(176, 41.6, 30, 7)
ellipse.set_line_color('#6600CC')

# Open the charts in separate tabs
aapl_trader.open()
tesla_trader.open()
tesla_trader2.open()
nvidia_trader.open()
