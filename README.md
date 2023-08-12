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


3. Convert decimal data to binary and save to an output file when input from file:    
Enter input format (HEX, BINARY, DECIMAL, UTF8): hex    
Enter output format (HEX, BINARY, DECIMAL, UTF8): binary    
Enter file name in single quotes ('') for file input or data(separated by spaces) to convert: 'input.txt'    
Converted data:    
00001010    
1010101110111011    
Data written to '20230812094022_output.txt'.    

4. Terminate by type "quit"    
Enter input format (HEX, BINARY, DECIMAL, UTF8): hex    
Enter output format (HEX, BINARY, DECIMAL, UTF8): quit    
Terminating the program.    

## Running via Docker

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

1. Docker: Install Docker from the official website by following the instructions for your operating system: [Docker Installation Guide](https://docs.docker.com/get-docker/).

### Setup and Usage

Follow the steps below to set up and run the tool using Docker:

#### 1. Clone the Repository

Clone the repository containing the Data Conversion Tool to your local machine:

```bash
git clone git@github.com:moguloulou/data_format_conversion.git
cd data_format_conversion
```

#### 2. Build the Docker Image

Navigate to the repository directory and build the Docker image using the provided `Dockerfile`:

```bash
make build
```

#### 3. Run the Docker Container

Once the Docker image is built, you can run the tool in a Docker container. Use the following command to start the container:

```bash
make run
```

#### 4. Follow the Interactive Prompts

Once the container is running, you'll be prompted to provide input and output formats, as well as the data you want to convert. Follow the prompts and provide the required information.

#### 5. Exit the Container

You can exit the Docker container by typing `quit` when prompted for input. Alternatively, you can press `Ctrl + C` to terminate the container.

## License

This tool is provided under the [MIT License](LICENSE).
