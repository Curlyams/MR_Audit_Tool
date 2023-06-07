import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import xlrd
from trip_data import *
from df_functions import *


# Define a class named AuditDataFrame
class AuditDataFrame:
    # The constructor (__init__) for the class
    def __init__(
        self,
        data=None,
        columns=None,
        modes_df=None,
        county_df=None,
        purpose_df=None,
        cancel_types_df=None,
    ):
        # If data is None, create an empty DataFrame, else create a DataFrame with provided data and columns
        if data is None:
            self.df = pd.DataFrame()
        else:
            self.df = pd.DataFrame(data, columns=columns)
            # Add a backdating column and additional columns
            self.add_backdating_column()
            self.add_columns()
            # Convert counties to lower case
            self.lower_case_counties()
            # Replace 'none' and nan with an empty string
            self.replace_none_and_nan()
            # Change specific column values
            self.change_value("", 0.65, "Provider Rate")
            self.change_value("", 1, "Fare Distance Rounded Miles")
            self.change_value(0, 1, "Fare Distance Rounded Miles")
            # Update trip dates
            self.update_trip_dates()

        # Load additional data
        (
            self.modes_df,
            self.county_df,
            self.purpose_df,
            self.cancel_types_df,
        ) = load_additional_data()

    # Special method to get column values when accessed using square brackets ([])
    def __getitem__(self, column_name):
        return self.df[column_name].values

    # Function to add a backdating column
    def add_backdating_column(self):
        self.df = add_yes_no(self.df, "Distribution Date", "Backdating Process")

    # Function to add new columns 'Mode', "Trip Status Summary"
    def add_columns(self):
        new_col_names = ["Mode", "Trip Status Summary"]
        self.df = self.df.reindex(columns=self.df.columns.tolist() + new_col_names)

    # Function to convert county names to lower case
    def lower_case_counties(self):
        try:
            self.df["Pick-up County"] = self.df["Pick-up County"].str.lower()
            self.df["Drop-off County"] = self.df["Drop-off County"].str.lower()
        except:
            pass

    # Function to replace 'none' and NaN values with an empty string
    def replace_none_and_nan(self):
        self.df = self.df.replace({"none": "", np.nan: ""}, regex=True, inplace=False)

    # Function to load data from a csv file and perform initial transformations
    def load_mr_export(self, file_path):
        self.df = pd.read_csv(file_path, encoding="ISO-8859-1", low_memory=False)
        self.add_backdating_column()
        self.add_columns()
        self.lower_case_counties()
        self.replace_none_and_nan()
        self.change_value("", 0.65, "Provider Rate")
        self.change_value("", 1, "Fare Distance Rounded Miles")
        self.change_value(0, 1, "Fare Distance Rounded Miles")
        self.update_trip_dates()

    # Function to create and return a numpy array by concatenating arguments
    def create_array(self, *args):
        return np.concatenate(args)

    # Function to save the DataFrame to a csv file
    def save_csv(self, file_path):
        self.df.to_csv(file_path, index=False)

    # Function to concatenate DataFrames
    def concat_dataframes(self, *args):
        return pd.concat([self.df, *args], ignore_index=True)

    # Function to change the data type of a DataFrame column
    def change_dtype(self, column_name, dtype):
        self.df[column_name] = self.df[column_name].astype(dtype)

    # Function to format an excel date to "mm/dd/yyyy" format
    def date_formatter(self, excel_date):
        if isinstance(excel_date, str):

            _date = datetime.strptime(excel_date, "%m/%d/%Y").date()
            formatted_date = _date.strftime("%m/%d/%Y")
            return formatted_date
        elif isinstance(excel_date, float):

            date_tuple = xlrd.xldate_as_tuple(excel_date, 0)
            year, month, day, _, _, _ = date_tuple
            if year < 1900:
                year += 1900
            _date = date(year, month, day)
            formatted_date = _date.strftime("%m/%d/%Y")
            return formatted_date
        elif isinstance(excel_date, int):
            excel_date = float(excel_date)
            date_tuple = xlrd.xldate_as_tuple(excel_date, 0)
            year, month, day, _, _, _ = date_tuple
            if year < 1900:
                year += 1900
            _date = date(year, month, day)
            formatted_date = _date.strftime("%m/%d/%Y")
            return formatted_date
        else:
            print("Unsupported date format:", excel_date)

    # Function to return a weekly audit date range
    def get_weekly_audit_date_range(self):
        delta = timedelta(days=67)
        today = datetime.today()
        audit_range_end = today - timedelta(days=today.weekday() + 1)
        audit_range_start = audit_range_end - delta
        audit_range_start_date = audit_range_start.strftime("%m/%d/%Y")
        audit_range_end_date = audit_range_end.strftime("%m/%d/%Y")
        return audit_range_end_date, audit_range_start_date

    # Function to return a range of dates between start_date and end_date
    def get_date_range(self, start_date, end_date):
        # If start_date and end_date are strings, convert them to datetime objects
        if isinstance(start_date, str):
            formatted_start_date = pd.to_datetime(start_date)
        else:
            formatted_start_date = start_date

        if isinstance(end_date, str):
            formatted_end_date = pd.to_datetime(end_date)
        else:
            formatted_end_date = end_date

        date_range = pd.date_range(start=formatted_start_date, end=formatted_end_date)

        # Format the date_range in "mm/dd/yyyy" format
        formatted_date_range = [date.strftime("%m/%d/%Y") for date in date_range]

        return formatted_date_range

    # # Function to filter the DataFrame based on a weekly audit date range
    # def iso_weekly_audit_date_range(self):
    #     audit_end_date, audit_start_date = self.get_weekly_audit_date_range()

    #     date_range = self.get_date_range(audit_start_date, audit_end_date)
    #     trips_in_range_df = pd.DataFrame()
    #     for date in date_range:
    #         trip_in_range = self.df[self.df["Trip Date"] == date]
    #         trips_in_range_df = trips_in_range_df.append(
    #             trip_in_range, ignore_index=True
    #         )
    #     self.df = trips_in_range_df

    def iso_weekly_audit_date_range(self):
        audit_end_date, audit_start_date = self.get_weekly_audit_date_range()

        self.df["Trip Date"] = pd.to_datetime(
            self.df["Trip Date"],format= "%m/%d/%Y"
            )
        self.df = self.df[
            (self.df["Trip Date"] >= audit_start_date) &
            (self.df["Trip Date"] <= audit_end_date)
        ]
        
    def iso_secondary_audit_date_range(self):
        _, audit_start_date = self.get_weekly_audit_date_range()
        self.df["Trip Date"] = pd.to_datetime(self.df["Trip Date"], format = "%m/%d/%Y")
        self.df = self.df[
            self.df["Trip Date"] < audit_start_date
            ]


    # Function to add additional data to the DataFrame
    def add_data(self):
        # Using xlookup_columns function to add data to new columns
        self.df["Mode"] = self.xlookup_columns(
            self.df["Transportation Provider"],
            self.modes_df["Transportation Provider"],
            self.modes_df["Mode"],
        )
        self.df["Trip Status Summary"] = self.xlookup_columns(
            self.df["Trip Status"],
            self.cancel_types_df["Trip Status"],
            self.cancel_types_df["Summary"],
        )
        self.df["Purpose Summary"] = self.xlookup_columns(
            self.df["Purpose"],
            self.purpose_df["Purpose"],
            self.purpose_df["Purpose Summary"],
        )
        self.df["Mileage vs NOT-Mileage vs PR/BT"] = self.xlookup_columns(
            self.df["Transportation Provider"],
            self.modes_df["Transportation Provider"],
            self.modes_df["Mileage vs NOT-Mileage vs PR/BT"],
        )

    # Function to implement xlookup-like functionality, mapping values from result_column corresponding to matched values in search_column and target_column
    def xlookup_columns(self, search_column, target_column, result_column):
        return search_column.map(dict(zip(target_column, result_column)))

    # Function to update the 'Provider Rate' for a given date range with a new value calculated by multiplying the 'Fare Distance Rounded Miles' with a multiplier
    def update_provider_rate(self, multiplier, start_date, end_date):
        new_df = self.df.copy()
        date_range = self.get_date_range(start_date, end_date)
        new_col_name = f"FDRM * {multiplier}"
        for date in date_range:
            new_df.loc[new_df["Trip Date"] == date, new_col_name] = (
                new_df.loc[new_df["Trip Date"] == date, "Fare Distance Rounded Miles"]
                * multiplier
            )
        new_df = new_df.dropna(subset=[new_col_name])

        return new_df

    # Function to format the 'Trip Date' column to "mm/dd/yyyy"
    def update_trip_dates(self):
        self.df["Trip Date"] = self.df["Trip Date"].apply(self.date_formatter)

    # Function to drop rows with NaN values in a given column
    def drop_nan_values(self, column_name):
        self.df = self.df.dropna(subset=[column_name])

    # Function to replace NaN values in a given column with a specific value
    def nan_to_value(self, value, column_name):
        self.df[column_name] = self.df[column_name].fillna(value)

    # Function to replace a specific old_value in a given column with a new_value
    def change_value(self, old_value, new_value, column_name):
        self.df[column_name] = self.df[column_name].replace(old_value, new_value)

    # Function to drop rows where values in a given column start with a specific string
    def drop_rows_starts_with(self, column_name, starts_with):
        self.df = self.df[~self.df[column_name].str.startswith(starts_with)]

    # Function to subtract one feature from another and store the result in a new column
    def subtract_features(self, first_feature, second_feature, column_name):
        self.df[column_name] = self.df[first_feature] - self.df[second_feature]

    # Function to display the DataFrame
    def display_data(self):
        df = self.df.copy()
        print(df)


class WeeklyAudit(AuditDataFrame):
    def __init__(
        self,
        data=None,
        columns=None,
        modes_df=None,
        county_df=None,
        purpose_df=None,
        cancel_types_df=None,
    ):
        # Initialize WeeklyAudit with input parameters and call parent class (AuditDataFrame) constructor
        super().__init__(
            data=data,
            columns=columns,
            modes_df=modes_df,
            county_df=county_df,
            purpose_df=purpose_df,
            cancel_types_df=cancel_types_df,
        )
        # Apply the weekly audit date range and update rate functions
        self.iso_weekly_audit_date_range()
        self.update_rate()

    # Function to update the 'Provider Rate' column by applying a specific formula
    # def update_rate(self):
    #     date_rate_change = datetime.strptime("06/01/2023", "%m/%d/%Y")
    #     for index, row in self.df.iterrows():
    #         date_of_trip = datetime.strptime(self.df.at[index, "Trip Date"], "%m/%d/%Y")
    #         if self.df.at[index, "Transportation Provider" ] == "Reimbursement Mileage" and  date_of_trip < date_rate_change:
    #             self.df.at[index, "Provider Rate"] = round(
    #                 (0.25 * row["Fare Distance Rounded Miles"]), 2
    #             )
    #         elif self.df.at[index, "Transportation Provider" ] == "Reimbursement Mileage" and  date_of_trip > date_rate_change:
    #             self.df.at[index, "Provider Rate"] = round(
    #                 (0.65 * row["Fare Distance Rounded Miles"]), 2
    #             )
    def update_rate(self):
        date_rate_change = datetime.strptime("06/01/2023", "%m/%d/%Y")
        self.df["Trip Date"] = pd.to_datetime(self.df["Trip Date"], format="%m/%d/%Y")
        
        for index, row in self.df.iterrows():
            date_of_trip = self.df.at[index, "Trip Date"]
            if (
                self.df.at[index, "Transportation Provider"] == "Reimbursement Mileage"
                and date_of_trip < date_rate_change
            ):
                self.df.at[index, "Provider Rate"] = round(
                    (0.25 * row["Fare Distance Rounded Miles"]), 2
                )
            elif (
                self.df.at[index, "Transportation Provider"] == "Reimbursement Mileage"
                and date_of_trip > date_rate_change
            ):
                self.df.at[index, "Provider Rate"] = round(
                    (0.65 * row["Fare Distance Rounded Miles"]), 2
                )


    # Function to find rows where the trip status summary is 'cx/NS', distribution date is not excluded, and backdating process is 'no'
    def cancel_with_distribution_date(self):
        df = self.df.copy()
        df = df.query(
            "`Trip Status Summary` == 'cx/NS' and `Distribution Date` not in @exclude and `Backdating Process` == 'no'"
        )
        return df

    # Function to find rows where the transportation provider is blank, the trip status summary is 'comp etc.', and the backdating process is 'no'
    def blank_provider_iso(self):
        df = self.df.copy()
        df = df.query(
            "`Transportation Provider` == '' and `Trip Status Summary` == 'comp etc.' and `Backdating Process` == 'no'"
        )
        return df

    # Function to find rows where the backdating process is 'yes'
    def incorrect_td_date(self):
        df = self.df.copy()
        df = df.query("`Backdating Process` == 'yes'")
        return df

    # Function to identify duplicate trips based on certain conditions
    def duplicate_trips(self):
        df = self.df.copy()
        df = df.query(
            "`Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty"
        ).astype(str)
        df["Date at PU + DO for Member"] = (
            df["Trip Date"]
            + " at "
            + df["Pick-up Street Number"]
            + " + "
            + df["Drop-off Street Number"]
            + " for "
            + df["Customer Number"]
        )
        not_reimbursements = df.loc[
            df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket",
            "Date at PU + DO for Member",
        ].value_counts()
        mileage_reimbursements = df.loc[
            df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage",
            "Date at PU + DO for Member",
        ].value_counts()
        df["Not Reimbursement"] = df["Date at PU + DO for Member"].map(
            not_reimbursements
        )
        df["Mileage Reimbursements"] = df["Date at PU + DO for Member"].map(
            mileage_reimbursements
        )
        df[["Not Reimbursement", "Mileage Reimbursements"]] = df[
            ["Not Reimbursement", "Mileage Reimbursements"]
        ].fillna(0)
        df["Mileage Count + Not Reimbursement"] = (
            df["Not Reimbursement"] + df["Mileage Reimbursements"]
        )
        duplicate_trips = df[
            (
                (df["Mileage Reimbursements"] >= 1)
                & (
                    df["Mileage Count + Not Reimbursement"]
                    > df["Mileage Reimbursements"]
                )
            )
            | (df["Mileage Reimbursements"] >= 2)
        ]
        excessive_trips = self.excessive_trips()
        filtered_duplicate_trips = remove_matching_rows(duplicate_trips,excessive_trips,"Trip ID","Trip ID")
        return filtered_duplicate_trips

    # Function to process duplicate trips filtering by `Transportation Provider`
    def pass_duplicate_trips(self):
        duplicate_trips = self.duplicate_trips()
        duplicate_trips_non_mileage = duplicate_trips.query(
            "`Transportation Provider`!= 'Reimbursement Mileage'"
        )
        
        duplicate_trips = duplicate_trips.query(
            "`Transportation Provider` == 'Reimbursement Mileage'"
        )
        payable_duplicate_trips = duplicate_trips[
            "Date at PU + DO for Member"
        ].drop_duplicates(keep="first")

        duplicate_trips_df = duplicate_trips.loc[payable_duplicate_trips.index]
        payable_duplicate_trips_df = remove_matching_rows(duplicate_trips_df, duplicate_trips_non_mileage,"Date at PU + DO for Member","Date at PU + DO for Member")
        return payable_duplicate_trips_df

    # Function to identify single leg trips within the specified areas and conditions
    def single_leg_trips(self):
        df = self.df.copy()
        df = df.query(
            "`Mileage vs NOT-Mileage vs PR/BT` in ['Private Rides or Bus Ticket', 'Mileage'] and `Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty"
        ).astype(str)
        df["Date for Member"] = df["Trip Date"] + " " + df["Customer Number"]
        not_reimbursements = df.loc[
            df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket",
            "Date for Member",
        ].value_counts()
        mileage_reimbursements = df.loc[
            df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage", "Date for Member"
        ].value_counts()
        df["Not Reimbursement"] = df["Date for Member"].map(not_reimbursements)
        df["Mileage Reimbursements"] = df["Date for Member"].map(mileage_reimbursements)
        df[["Not Reimbursement", "Mileage Reimbursements"]] = df[
            ["Not Reimbursement", "Mileage Reimbursements"]
        ].fillna(0)
        df["Mileage Count + Not Reimbursement"] = (
            df["Not Reimbursement"] + df["Mileage Reimbursements"]
        )
        single_across_modes = df[
            (df["Mileage Reimbursements"] == 1)
            & (df["Mileage Count + Not Reimbursement"] == 1)
        ]
        return single_across_modes, df

    # Function to identify excessive trips based on certain conditions
    def excessive_trips(self):
        _, df = self.single_leg_trips()
        df["Mileage Reimbursements"] = df["Mileage Reimbursements"].astype(int)
        excessive_trips = df.query(
            "`Mileage Reimbursements` > 4 and `Transportation Provider` == 'Reimbursement Mileage'"
        )
        return excessive_trips

    # Function to identify single legs within one day
    def single_legs_within_one_day(self):
        single_legs_within_one_day_df = pd.DataFrame()
        prev_row = None
        single_trips, _ = self.single_leg_trips()
        single_trips = single_trips.sort_values(
            ["Customer Number", "Trip Date"]
        )  # Sort by Customer Number and Trip Date
        for index, row in single_trips.iterrows():
            if (
                prev_row is None
                or row["Customer Number"] != prev_row["Customer Number"]
            ):
                prev_row = row
            else:
                current_date = datetime.strptime(row["Trip Date"], "%m/%d/%Y")
                prev_date = datetime.strptime(prev_row["Trip Date"], "%m/%d/%Y")
                date_difference = (current_date - prev_date).days
                if abs(date_difference) <= 1:
                    single_legs_within_one_day_df = (
                        single_legs_within_one_day_df.append(row, ignore_index=True)
                    )
                    single_legs_within_one_day_df = (
                        single_legs_within_one_day_df.append(
                            prev_row, ignore_index=True
                        )
                    )
                prev_row = row
        return single_legs_within_one_day_df

    # Function to export taxi-related data
    def taxi_export(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement' and `Transportation Provider` != '' and `Trip Status Summary` == 'comp etc.' and `Backdating Process` == 'no' and `Distribution Date` == '' and `Trip Status` == 'comp' and `Transportation Provider` == 'Reimbursement Taxi'"
        )
        return df

    # Function to export out of area (ooa) data
    def ooa_export(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement' and (`Pick-up County` not in @tricounty or `Drop-off County` not in @tricounty)"
        )
        return df

    # Function to identify trip purpose errors
    def trip_purpose_error(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement' and `Funding Source` == 'Ride to Care' and `Purpose Summary` == 'Non-covered service'"
        )
        return df

    # Function to identify completed trips with cancel type
    def comp_with_cancel(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement' and `Transportation Provider` != '' and `Trip Status` == 'comp' and `Mileage vs NOT-Mileage vs PR/BT` == 'Mileage' and `Distribution Date` == '' and `Cancel Type` not in ('','Not Selected')"
        )
        return df
    # Function that takes values from one dataframe and removes the rows in the other dataframe that are duplicates


    
class SecondPaymentsAudit(AuditDataFrame):
    def __init__(self, data=None, columns=None, modes_df=None, county_df=None, purpose_df=None,
                cancel_types_df=None):
        super().__init__(data=data, columns=columns, modes_df=modes_df, county_df=county_df,
                            purpose_df=purpose_df, cancel_types_df=cancel_types_df)
        
        self.iso_secondary_audit_date_range()


    def update_rate_secondary_payments(self):
        date_rate_change_ = datetime.strptime("06/01/2023", "%m/%d/%Y")
        self.df["Trip Date"] = pd.to_datetime(self.df["Trip Date"], format="%m/%d/%Y")
        
        for index, row in self.df.iterrows():
            date_of_trip = self.df.at[index, "Trip Date"]
            if (
                self.df.at[index, "Transportation Provider"] == "Reimbursement Mileage"
                and date_of_trip < date_rate_change
            ):
                self.df.at[index, "Provider Rate"] = round(
                    (0.25 * row["Fare Distance Rounded Miles"]), 2
                )
            elif (
                self.df.at[index, "Transportation Provider"] == "Reimbursement Mileage"
                and date_of_trip > date_rate_change
            ):
                self.df.at[index, "Provider Rate"] = round(
                    (0.65 * row["Fare Distance Rounded Miles"]), 2
                )



file_path = "C:\\Users\\bcurl\\Desktop\\Audit_Tool_2.0\\util\\2023.03.23-2023.05.28 MR Export.csv"
file_path_2 = "C:\\Users\\bcurl\\Desktop\\Audit_Tool_2.0\\util\\2023.03.23-2023.05.28 MR Export _with_new_dates.csv"
file_path_3 = "C:\\Users\\bcurl\\Desktop\\Audit_Tool_2.0\\test_data\\export_2022_short.csv"
export_df = pd.read_csv(file_path_3)
test = WeeklyAudit(export_df)
test.add_data()
test.save_csv("Testooooo.csv")
# tt = test.duplicate_trips()
# #ex = test.excessive_trips()
# #print(ex)
#test.display_data([rom]
#test.save_csv("jkdajk.csv")

