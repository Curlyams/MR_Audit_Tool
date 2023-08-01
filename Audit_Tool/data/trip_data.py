import pandas as pd
import os
# dict = {"A": "BLANK PROVIDER ", "B": "CANCEL with DISTRIBUTION DATE ", "C": "INCORRECT TD DATE", "D": "DUPLICATE TRIPS" ,  "E": "SINGLE LEG TRIPS", 
#         "F": "OOA", "G" : "TRIP PURPOSE ERROR", "H": "COMP w CANCEL", "I": "EXCESS APPOINTMENTS"}

"""
This contains the column names for the fiscal summary report. It also loads additional
data from csv files and helps format the exported data.
"""
fiscal_summary_cols = [
    "Client First Name",
    "Client Last Name",
    "Customer Number",
    "Trip ID",
    "Trip Date",
    "Trip Status",
    "Cancel Type",
    "Verification",
    "OSA or Negotiated Rate",
    "Distribution Date",
    "Pick-up County",
    "Pick-up Street Number",
    "Drop-off County",
    "Drop-off Street Number",
    "Purpose",
    "Funding Source",
    "Fare Distance Rounded Miles",
    "Transportation Provider",
    "Provider Rate",
]
flagged_cols = [
    "Flag",
    "Client First Name",
    "Client Last Name",
    "Customer Number",
    "Trip ID",
    "Trip Date",
    "Trip Status",
    "Cancel Type",
    "Verification",
    "OSA or Negotiated Rate",
    "Distribution Date",
    "Pick-up County",
    "Pick-up Street Number",
    "Drop-off County",
    "Drop-off Street Number",
    "Purpose",
    "Funding Source",
    "Fare Distance Rounded Miles",
    "Transportation Provider",
    "Provider Rate",
    "No Show Reason"
]
# List of counties in the area
tricounty = [
    "clackamas",
    "clackamas county",
    "multnomah",
    "multnomah county",
    "washington",
    "washington county",
]

# What to exclude when checking for cancel with distribution date
exclude_canc_dd = ["None", "", "OK SS", "OK BV"]
# What to exclude when checking comp with cancel
exclude_comp_cancel = ["Backdating Mileage", "", "Not Selected"]
exclude_excess_apps = ["Ride Connection"]
# Labels for flagged trips

flag_labels = [
    "BLANK PROVIDER",
    "CANCEL with DISTRIBUTION DATE",
    "INCORRECT TD DATE",
    "DUPLICATE TRIP",
    "SINGLE LEG TRIP",
    "OOA",
    "TRIP PURPOSE ERROR",
    "COMP with CANCEL",
    "EXCESS APPOINTMENTS",
    "Duplicate Trips (only within mileage)",
    "NO SHOW VALUE PRESENT",
    "CANCEL WITH QR VERIFICATION"
]

# module_dir = os.path.dirname(__file__)
# modes_path = os.path.join(module_dir, "modes.csv")
# service_areas_path = os.path.join(module_dir, "service_areas.csv")
# purpose_summary_path = os.path.join(module_dir, "purpose_summary.csv")
import sys

# Check if running in a frozen exe, allows for the compiled function to access the required data files
if getattr(sys, 'frozen', False):
    module_dir = sys._MEIPASS
else:
    module_dir = os.path.dirname(os.path.abspath(__file__))

modes_path = os.path.join(module_dir, "modes.csv")
service_areas_path = os.path.join(module_dir, "service_areas.csv")
purpose_summary_path = os.path.join(module_dir, "purpose_summary.csv")



# Function to load data from csv files used for xlookup function
def load_additional_data():
    modes_df = pd.read_csv(modes_path)
    county_df = pd.read_csv(service_areas_path)
    purpose_df = pd.read_csv(purpose_summary_path)
    cancel_types_df = pd.DataFrame(
        {
            "Trip Status": ["cancel", "noshow", "act", "alloc", "asg", "comb", "comp"],
            "Summary": [
                "cx/NS",
                "cx/NS",
                "comp etc.",
                "comp etc.",
                "comp etc.",
                "comp etc.",
                "comp etc.",
            ],
        }
    )

    return modes_df, county_df, purpose_df, cancel_types_df
