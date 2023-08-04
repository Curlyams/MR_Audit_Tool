
# Audit Tool

This project is a GUI-based audit tool, designed to process and analyze different types of data. The tool is divided into six main Python scripts:

1. `Audit_Tool.py`, which provides the graphical user interface (GUI) and controls the flow of the program.
2. `auditclasses.py`, which contains the classes that perform the main data processing and analysis tasks.
3. `df_functions.py`, which contains a collection of helper functions used for data manipulation and processing.
4. `extract_functions.py`, which contains a collection of helper functions used for loading and cleaning data.
5. `trip_data.py`, which defines and manipulates various constants and global variables used across the other scripts, as well as a function to load additional data from CSV files.
6. `gui_data.py`, which defines the names of checkboxes and associated functions in the GUI.

## Features

The Audit Tool has the following features:

1. An interactive GUI for easy use.
2. Different modes of operation based on the selected audit type.
3. Data processing and analysis for:
   - Flagged, payable, and taxi trips.
   - Trips with trip purpose errors.
   - Trips with cancel type.
   - Excessive trips based on certain conditions.
   - Duplicate trips.
   - Single leg trips.
   - Out of area (ooa) data.
   - Trips with a no show Reason
   - Trips with a QR Verification and cancel type.

4. Custom helper functions to perform operations like:
   - Data lookup.
   - Adding columns to dataframes.
   - Stacking dataframes.
   - Filtering data based on certain conditions.
   - Loading data from CSV and Excel files.
   - Extracting specific data from the loaded files.
   - Removing certain entries from lists.
   - Cleaning up dataframes.

5. Predefined column names, flagged trip labels, and lists of counties in a specific area for data processing and analysis.
6. Definitions of GUI checkbox names and associated function names for different data processing and analysis tasks.
7. Export of processed and analyzed data to CSV files.
8. The tool supports custom settings and outputs.
9. Error handling capabilities with pop-up error messages.

## Dependencies

This project uses the following libraries:

altgraph==0.17.3
numpy==1.25.0
pandas==1.4.4
pefile==2023.2.7
PySide6==6.5.1.1
PySide6-Addons==6.5.1.1
PySide6-Essentials==6.5.1.1
python-dateutil==2.8.2
pytz==2023.3
pywin32-ctypes==0.2.1
shiboken6==6.5.1.1
six==1.16.0
xlrd==2.0.1
python==3.9.13

Make sure to install these dependencies before running the project.

## How to run

Run the `Audit_Tool.py` file in your Python environment. Make sure all the dependencies are installed in your environment. Or you can run the Audit_Tool.exe located in the dist folder.

## How to compile

You can compile the `Audit_Tool.py` file in your Python environment using Pyinstaller and with the following command:

pyinstaller --onefile --noconsole --add-data "icons/1x/*;icons/1x" --add-data "images/Layout/*;images/Layout" --add-data <PATH to modes.csv> --add-data <PATH to private_providers.csv>;." --add-data "<PATH to purpose_summary.csv>;." --add-data "<PATH to service_areas.csv>;." --icon "<PATH to auditing-icon-9.ico>" Audit_Tool.py


## Usage

Navigate through the GUI to use the application. Use the settings page to adjust application settings and select the audit type from the available options. The tool will process the data and provide a summary which can be exported to CSV files.

## Known Limitations

The tool is built to use the formatted export from ecolane, so you must export the right profile in order for it to work correctly. 
