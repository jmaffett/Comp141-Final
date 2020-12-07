import json
import sys


def main():
    weather_file = sys.argv[1]
    print(f'Reading data from: {weather_file}')
    with open(weather_file, 'r') as f:
        data = json.load(f)
    print(f'API response: {data}')
    print()

    # convert Kelvin to Fahrenheit
    temp = round((data['main']['feels_like'] - 273.15) * 9 / 5 + 32)
    should_wear_coat = '' if temp < 32 else "don't"
    print(f"It feels like {temp}F so {should_wear_coat} wear a coat.")

main()

