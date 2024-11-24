
### Steps to Build the Utility:

1. **Install required libraries** (optional: though we won't use external libraries here).
2. **Define the conversion functions**.
3. **Use `argparse` to parse command-line arguments**.
4. **Make the script executable** from the terminal.

### Step 1: Install Python

If you haven't already installed Python, download it from [python.org](https://www.python.org/) and follow the installation instructions.

### Step 2: Write the Python Code

```python
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
```

### Step 3: Explanation

-  **Imports:**
   -  `argparse`: This Python module helps parse command-line arguments.
-  **Conversion functions:**

   -  `celsius_to_fahrenheit()`: Converts a temperature in Celsius to Fahrenheit.
   -  `fahrenheit_to_celsius()`: Converts a temperature in Fahrenheit to Celsius.

-  **Command-line argument parsing:**
   -  We use `argparse.ArgumentParser()` to create a parser for the command-line arguments.
   -  Two optional arguments (`-c` or `--to-celsius` and `-f` or `--to-fahrenheit`) are used to determine which conversion to perform.
   -  The `temperature` argument is required and specifies the temperature to be converted.
-  **Main function logic:**
   -  Depending on the user input (`--to-celsius` or `--to-fahrenheit`), the utility will convert the temperature accordingly.
   -  If no conversion option is provided, it prints a helpful message.

### Step 4: Running the Script

1. Save the file as `temp_converter.py`.
2. Make the script executable (optional but useful on Linux/macOS):

   ```bash
   chmod +x temp_converter.py
   ```

3. Run the utility from the terminal:

   -  To convert from Celsius to Fahrenheit:

      ```bash
      python temp_converter.py 25 --to-fahrenheit
      ```

   -  To convert from Fahrenheit to Celsius:
      ```bash
      python temp_converter.py 77 --to-celsius
      ```

### Example Output

```bash
$ python temp_converter.py 25 --to-fahrenheit
25.0 Celsius is 77.00 Fahrenheit

$ python temp_converter.py 77 --to-celsius
77.0 Fahrenheit is 25.00 Celsius
```

### Key Concepts:

-  **Command-line arguments:** Allows you to pass parameters directly via the terminal to control program behavior.
-  **`argparse`:** A Python library that simplifies command-line argument parsing.
-  **Executable scripts:** You can make a Python script executable from the command line to make it behave like a regular system utility.
#
