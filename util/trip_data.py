import pandas as pd
import os

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
exclude_comp_cancel = ['Backdating Mileage','','Not Selected']

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
]

module_dir = os.path.dirname(__file__)
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
