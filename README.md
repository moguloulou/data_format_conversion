# Data Format Conversion Tool

This is a simple tool for converting data between different formats using Python. The tool supports conversion between the following formats:

- HEX
- BINARY
- DECIMAL
- UTF8

## Usage

1. Run the script `data_format_conversion.py`.
2. Choose the input and output formats by entering the corresponding format names (HEX, BINARY, DECIMAL, UTF8).
3. Enter the data to convert or specify a file name (enclosed in single quotes '') for file input. The script will process the data and display the converted output.

## Features

- Supports manual data input or input from a file.
- Supports conversions between different formats.
- Supports multiple input(separated by spaces) or input through file(one data per line)
- Outputs converted data to a timestamped output file when input through file.

## Examples

1. Convert a hexadecimal number to decimal:

Enter input format (HEX, BINARY, DECIMAL, UTF8): hex
Enter output format (HEX, BINARY, DECIMAL, UTF8): decimal
Enter file name in single quotes ('') for file input or data(separated by spaces) to convert: 1 a3 3
Converted data:
1
163
3

2. Convert decimal data to binary and save to an output file when input from file:
Enter input format (HEX, BINARY, DECIMAL, UTF8): hex
Enter output format (HEX, BINARY, DECIMAL, UTF8): binary
Enter file name in single quotes ('') for file input or data(separated by spaces) to convert: 'input.txt'
Converted data:
00001010
1010101110111011
Data written to '20230812094022_output.txt'.

3. Terminate by type "quit"
Enter input format (HEX, BINARY, DECIMAL, UTF8): hex
Enter output format (HEX, BINARY, DECIMAL, UTF8): quit
Terminating the program.


## License

This tool is provided under the [MIT License](LICENSE).
