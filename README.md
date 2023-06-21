# AuroraExpress

AuroraExpress is a Python-based application that helps users generate an Aurora oneliner based on a few inputs. The application has a simple and intuitive GUI, which allows users to enter the required parameters and generate the oneliner command quickly.

## Features

* User-friendly GUI: The application features an easy-to-use graphical user interface designed with tkinter.
* Dynamic input fields: Depending on the hand side selection, the application dynamically adjusts the input fields.
* Automated command generation: By entering the required parameters, users can automatically generate an Aurora oneliner.

## Installation

Follow these steps to install the AuroraExpress application:

1. Clone the GitHub repository:
git clone https://github.com/Athen-Player1/AuroraExpress.git

2. Navigate to the cloned directory:
cd AuroraExpress

3. Make sure that you have Python installed on your machine. This application requires Python 3.6 or later. You can download Python from the [official website](https://www.python.org/downloads/).

4. The application uses tkinter for the GUI. If tkinter is not already installed with your Python version, you can install it using your package manager. For Debian-based systems, you can use:
sudo apt-get install python3-tk

## Usage

To use the application, follow these steps:

1. Run the `genorator.py` script:
python genorator.py

2. Enter the required parameters in the input fields, such as the customer key, branch, tag, product, hand side, etc.
3. Click on the 'Generate Oneliner' button.
4. The generated oneliner command will appear in the output field.

## Code Structure

* `genorator.py` - This is the main script that contains the GUI and the logic for generating the Aurora oneliner.

## License

The project is licensed under the GPL-3.0 license.

## Contribution

Contributions to the project are welcome. Please ensure that any pull requests or issues are clearly described.

For major changes, please open an issue first to discuss what you would like to change.

## Contact

If you have any questions, issues, or suggestions, please open an issue on GitHub.
Please note that the installation instructions for tkinter are for Debian-based systems. If your users are using a different operating system, they might need to install tkinter in a different way.
