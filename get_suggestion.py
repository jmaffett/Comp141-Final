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
    print(f"It feels like {temp}F")
    if temp <= 32:
        print('You should wear a coat')
        if temp < 0:
            print('also wear a cap and gloves')
    elif 32 < temp <= 50:
        print('You should wear long pants')
    elif temp > 50:
        print('You should wear shorts')
        if temp > 90:
            print('You should also wear a tank top')



main()
