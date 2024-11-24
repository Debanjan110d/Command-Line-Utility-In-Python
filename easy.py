import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Process some integers.')

# Add an argument
parser.add_argument('--input', type=str, help='Input file path')

# Parse the arguments
args = parser.parse_args()

# Use the argument
print(f'Input file path is: {args.input}')