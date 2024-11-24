#!/usr/bin/env python3
import argparse

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Convert temperatures between Celsius and Fahrenheit.')
    
    # Add arguments for the utility
    parser.add_argument('temperature', type=float, help='Temperature value to convert.')
    parser.add_argument('-c', '--to-celsius', action='store_true', help='Convert from Fahrenheit to Celsius.')
    parser.add_argument('-f', '--to-fahrenheit', action='store_true', help='Convert from Celsius to Fahrenheit.')
    
    # Parse the arguments
    args = parser.parse_args()

    if args.to_celsius:
        converted_temp = fahrenheit_to_celsius(args.temperature)
        print(f"{args.temperature} Fahrenheit is {converted_temp:.2f} Celsius")
    elif args.to_fahrenheit:
        converted_temp = celsius_to_fahrenheit(args.temperature)
        print(f"{args.temperature} Celsius is {converted_temp:.2f} Fahrenheit")
    else:
        print("Please specify a conversion option: --to-celsius or --to-fahrenheit")

if __name__ == '__main__':
    main()
