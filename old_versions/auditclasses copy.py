import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import xlrd
from util.trip_data import *
from util.df_functions import *



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
            self.replace_none_and_nan()
            self.add_backdating_column()
            self.add_columns()
            # Convert counties to lower case
            self.lower_case_counties()
            # Replace 'none' and nan with an empty string
            
            # Change specific column values
            self.change_value("", 0.65, "Provider Rate")
            self.change_value("", 1, "Fare Distance Rounded Miles")
            self.change_value(0, 1, "Fare Distance Rounded Miles")


            # Update trip dates
            
            

            

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

    # Function to drop columns added for audit process

    def drop_columns(self, df):
        columns = [
            "Backdating Process",
            "Mode",
            "Trip Status Summary",
            "Purpose Summary",
            "Mileage vs NOT-Mileage vs PR/BT"
        ]
        try:
            df = df.drop(columns=columns, axis=1)
        except:
            pass

        return df

    # Function to convert county names to lower case
    def lower_case_counties(self):
        try:
            self.df["Pick-up County"] = self.df["Pick-up County"].str.lower()
            self.df["Drop-off County"] = self.df["Drop-off County"].str.lower()
        except:
            pass

    # Function to replace 'none' and NaN values with an empty string
    def replace_none_and_nan(self):
        self.df = self.df.replace({"None": "", np.nan: ""}, regex=True, inplace=False)

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
        

    # Function to create and return a numpy array by concatenating arguments
    def create_array(self, *args):
        return np.concatenate(args)

    # Function to save the DataFrame to a csv file
    def save_csv(self, file_path):
        self.drop_columns(self.df)
        self.df.to_csv(file_path, index=False)

    # Function to concatenate DataFrames
    def concat_dataframes(self, *args):
        return pd.concat([self.df, *args], ignore_index=True)

    # Function to change the data type of a DataFrame column
    def change_dtype(self, column_name, dtype):
        self.df[column_name] = self.df[column_name].astype(dtype)

    # Function to format an excel date to "mm/dd/yyyy" format
    #def date_formatter(self, excel_date):
        # try:
        #     if isinstance(excel_date, str):

        #         _date = datetime.strptime(excel_date, "%m/%d/%Y").date()
        #         formatted_date = _date.strftime("%m/%d/%Y")
        #         return formatted_date
        #     elif isinstance(excel_date, float):

        #         date_tuple = xlrd.xldate_as_tuple(excel_date, 0)
        #         year, month, day, _, _, _ = date_tuple
        #         if year < 1900:
        #             year += 1900
        #         _date = date(year, month, day)
        #         formatted_date = _date.strftime("%m/%d/%Y")
        #         return formatted_date
        #     elif isinstance(excel_date, int):
        #         excel_date = float(excel_date)
        #         date_tuple = xlrd.xldate_as_tuple(excel_date, 0)
        #         year, month, day, _, _, _ = date_tuple
        #         if year < 1900:
        #             year += 1900
        #         _date = date(year, month, day)
        #         formatted_date = _date.strftime("%m/%d/%Y")
        #         return formatted_date
        # except:
        #     _date = pd.to_datetime(excel_date, format = "%m/%d/%Y")
        #     _date = _date.strftime("%m/%d/%Y")
        #     return _date

            #print("Unsupported date format:", excel_date)

    # def date_formatter(self, excel_date):
    #     try:
    #         if isinstance(excel_date, str):
    #             formats = ["%m/%d/%Y", "%d/%m/%Y","%Y-%m-%d"]  # Add more formats as needed

    #             for fmt in formats:
    #                 try:
    #                     _date = datetime.strptime(excel_date, fmt).date()
    #                     formatted_date = _date.strftime("%m/%d/%Y")
    #                     return formatted_date
    #                 except ValueError:
    #                     pass

    #         elif isinstance(excel_date, float) or isinstance(excel_date, int):
    #             date_tuple = xlrd.xldate_as_tuple(float(excel_date), 0)
    #             year, month, day, _, _, _ = date_tuple
    #             if year < 1900:
    #                 year += 1900
    #             _date = date(year, month, day)
    #             formatted_date = _date.strftime("%m/%d/%Y")
    #             return formatted_date

    #     except Exception as e:
    #         _date = pd.to_datetime(excel_date, format="%m/%d/%Y")
    #         _date = _date.strftime("%m/%d/%Y")
    #         return _date
        


    def date_formatter(self, excel_date):
        try:
            if isinstance(excel_date, str):
                formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d"]  # Add more formats as needed

                for fmt in formats:
                    try:
                        _date = datetime.strptime(excel_date, fmt).date()
                        formatted_date = _date.strftime("%m/%d/%Y")
                        return formatted_date
                    except ValueError:
                        pass

            elif isinstance(excel_date, float) or isinstance(excel_date, int):
                date_tuple = xlrd.xldate_as_tuple(float(excel_date), 0)
                year, month, day, _, _, _ = date_tuple
                if year < 1900:
                    year += 1900
                _date = date(year, month, day)
                formatted_date = _date.strftime("%m/%d/%Y")
                return formatted_date

        except Exception as e:
            _date = pd.to_datetime(excel_date, format="%m/%d/%Y")
            _date = _date.date()  # Extract only the date component
            formatted_date = _date.strftime("%m/%d/%Y")
            return formatted_date


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

    # Function to format the 'Trip Date' column to "mm/dd/yyyy"
    def update_trip_dates(self):
        self.df["Trip Date"] = self.df["Trip Date"].apply(self.date_formatter)

    # Function to replace a specific old_value in a given column with a new_value
    def change_value(self, old_value, new_value, column_name):
        self.df[column_name] = self.df[column_name].replace(old_value, new_value)
    # Function to display the DataFrame
    def display_data(self):
        df = self.df.copy()
        print(df)

    def update_rate(self):
        # date_range_change_62 = datetime.strptime("12/31/2022", "%m/%d/%Y")
        # date_range_change_58 = datetime.strptime("06/30/2022", "%m/%d/%Y")
        # rate_change_start = datetime.strptime("01/01/2022", "%m/%d/%Y")
        date_rate_change_65 = datetime.strptime("06/01/2023", "%m/%d/%Y")

        #self.df["Trip Date"] = pd.to_datetime(self.df["Trip Date"], format="%m/%d/%Y")
        
        reimbursement_mileage = self.df["Transportation Provider"] == "Reimbursement Mileage"
        date_of_trip = self.df["Trip Date"]
        distance = self.df["Fare Distance Rounded Miles"]
        
        # mask_58 = reimbursement_mileage & (date_of_trip <= date_range_change_58) & (date_of_trip >= rate_change_start)
        # self.df.loc[mask_58, "Provider Rate"] = round(0.58 * distance[mask_58], 2)

        # mask_62 = reimbursement_mileage & (date_of_trip <= date_range_change_62) & (date_of_trip > date_range_change_58)
        # self.df.loc[mask_62, "Provider Rate"] = round(0.62 * distance[mask_62], 2)

        mask_65 = reimbursement_mileage & (date_of_trip >= date_rate_change_65)
        self.df.loc[mask_65, "Provider Rate"] = round(0.65 * distance[mask_65], 2)

        mask_other = reimbursement_mileage & (date_of_trip < date_rate_change_65)
        self.df.loc[mask_other, "Provider Rate"] = round(0.25 * distance[mask_other], 2)



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
    # def duplicate_trips(self):
    #     df = self.df.copy()
    #     df = df.query(
    #         "`Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty"
    #     ).astype(str)
    #     df["Date at PU + DO for Member"] = (
    #         df["Trip Date"]
    #         + " at "
    #         + df["Pick-up Street Number"]
    #         + " + "
    #         + df["Drop-off Street Number"]
    #         + " for "
    #         + df["Customer Number"]
    #     )
    #     not_reimbursements = df.loc[
    #         df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket",
    #         "Date at PU + DO for Member",
    #     ].value_counts()
    #     mileage_reimbursements = df.loc[
    #         df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage",
    #         "Date at PU + DO for Member",
    #     ].value_counts()
    #     df["Not Reimbursement"] = df["Date at PU + DO for Member"].map(
    #         not_reimbursements
    #     )
    #     df["Mileage Reimbursements"] = df["Date at PU + DO for Member"].map(
    #         mileage_reimbursements
    #     )
    #     df[["Not Reimbursement", "Mileage Reimbursements"]] = df[
    #         ["Not Reimbursement", "Mileage Reimbursements"]
    #     ].fillna(0)
    #     df["Mileage Count + Not Reimbursement"] = (
    #         df["Not Reimbursement"] + df["Mileage Reimbursements"]
    #     )
    #     df.to_csv("duplicate_trips.csv", index=False)
    #     duplicate_trips = df[
    #         (
    #             (df["Mileage Reimbursements"] >= 1)
    #             & (
    #                 df["Mileage Count + Not Reimbursement"]
    #                 > df["Mileage Reimbursements"]
    #             )
    #         )
    #         | (df["Mileage Reimbursements"] >= 2)
    #     ]
    #     excessive_trips = self.excessive_trips()
    #     filtered_duplicate_trips = remove_matching_rows(duplicate_trips,excessive_trips,"Trip ID","Trip ID")
    #     return filtered_duplicate_trips


    def duplicate_trips(self):
        df = self.df.copy()
        

        df = df.query("`Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty").astype(str)
        
        df["Date at PU + DO for Member"] = (
            df["Trip Date"]
            + " at "
            + df["Pick-up Street Number"]
            + " + "
            + df["Drop-off Street Number"]
            + " for "
            + df["Customer Number"]
        )
        
        reimbursements = df[df["Mileage vs NOT-Mileage vs PR/BT"].isin(["Private Rides or Bus Ticket", "Mileage"])]
        not_reimbursements = reimbursements[reimbursements["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket"].groupby("Date at PU + DO for Member").size()
        mileage_reimbursements = reimbursements[reimbursements["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage"].groupby("Date at PU + DO for Member").size()
        
        df["Not Reimbursement"] = df["Date at PU + DO for Member"].map(not_reimbursements).fillna(0)
        df["Mileage Reimbursements"] = df["Date at PU + DO for Member"].map(mileage_reimbursements).fillna(0)
        
        df["Mileage Count + Not Reimbursement"] = df["Not Reimbursement"] + df["Mileage Reimbursements"]

        duplicate_trips = df[
            ((df["Mileage Reimbursements"] >= 1) & (df["Mileage Count + Not Reimbursement"] > df["Mileage Reimbursements"]))
            | (df["Mileage Reimbursements"] >= 2)
        ]
        
        excessive_trips = self.excessive_trips()
        filtered_duplicate_trips = remove_matching_rows(duplicate_trips, excessive_trips, "Trip ID", "Trip ID")
        
        return filtered_duplicate_trips

    #Function to process duplicate trips filtering by `Transportation Provider`
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
    # def single_leg_trips(self):
    #     df = self.df.copy()
    #     df = df.query(
    #         "`Mileage vs NOT-Mileage vs PR/BT` in ['Private Rides or Bus Ticket', 'Mileage'] and `Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty"
    #     ).astype(str)
    #     df["Date for Member"] = df["Trip Date"] + " " + df["Customer Number"]
    #     not_reimbursements = df.loc[
    #         df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket",
    #         "Date for Member",
    #     ].value_counts()
    #     mileage_reimbursements = df.loc[
    #         df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage", "Date for Member"
    #     ].value_counts()
    #     df["Not Reimbursement"] = df["Date for Member"].map(not_reimbursements)
    #     df["Mileage Reimbursements"] = df["Date for Member"].map(mileage_reimbursements)
    #     df[["Not Reimbursement", "Mileage Reimbursements"]] = df[
    #         ["Not Reimbursement", "Mileage Reimbursements"]
    #     ].fillna(0)
    #     df["Mileage Count + Not Reimbursement"] = (
    #         df["Not Reimbursement"] + df["Mileage Reimbursements"]
    #     )
    #     single_across_modes = df[
    #         (df["Mileage Reimbursements"] == 1)
    #         & (df["Mileage Count + Not Reimbursement"] == 1)
    #     ]
    #     return single_across_modes, df



    def single_leg_trips(self):
        df = self.df.copy()
        

        df = df.query("`Mileage vs NOT-Mileage vs PR/BT`.isin(['Private Rides or Bus Ticket', 'Mileage']) and `Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty").astype(str)
        
        df["Date for Member"] = df["Trip Date"] + " " + df["Customer Number"]
        
        not_reimbursements = df[df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket"].groupby("Date for Member").size()
        mileage_reimbursements = df[df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage"].groupby("Date for Member").size()
        
        df["Not Reimbursement"] = np.where(df["Mileage vs NOT-Mileage vs PR/BT"] == "Private Rides or Bus Ticket", df["Date for Member"].map(not_reimbursements), 0)
        df["Mileage Reimbursements"] = np.where(df["Mileage vs NOT-Mileage vs PR/BT"] == "Mileage", df["Date for Member"].map(mileage_reimbursements), 0)
        
        df[["Not Reimbursement", "Mileage Reimbursements"]] = df[["Not Reimbursement", "Mileage Reimbursements"]].fillna(0)
        
        df["Mileage Count + Not Reimbursement"] = df["Not Reimbursement"] + df["Mileage Reimbursements"]
        
        single_across_modes = df[(df["Mileage Reimbursements"] == 1) & (df["Mileage Count + Not Reimbursement"] == 1)]
        
        return single_across_modes, df

    # Function to identify excessive trips based on certain conditions
    def excessive_trips(self):
        _, df = self.single_leg_trips()
        #df["Mileage Reimbursements"] = df["Mileage Reimbursements"].astype(int)
        excessive_trips = df.query(
            "`Mileage Reimbursements` > 4 and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty and `Distribution Date` == '' and `Trip Status Summary` == 'comp etc.'"
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
    def in_area_mileage_reimbursement(self):
        df = self.df.copy()
        df = df.query(
           "`Pick-up County` in @tricounty and `Drop-off County` in @tricounty and `Distribution Date` == '' and `Trip Status Summary` == 'comp etc.' and `Transportation Provider` == 'Reimbursement Mileage'"
        )
        return df

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
        
        self.update_trip_dates()
        
        self.iso_weekly_audit_date_range()
        self.add_data()
        self.update_rate()

    def run_audit(self):

        df = self.in_area_mileage_reimbursement()
        
        
        blank_provider = self.blank_provider_iso()
        cancel_with_dd = self.cancel_with_distribution_date()
        incorrect_td_date = self.incorrect_td_date()
        duplicate_trips = self.duplicate_trips()
        single_legs, _ = self.single_leg_trips()
        ooa_trips = self.ooa_export()
        purpose_error_trips = self.trip_purpose_error()
        comp_w_cancel = self.comp_with_cancel()    
        excessive_trips = self.excessive_trips()
        taxi_questions = self.taxi_export()
        
        flagged_dfs = [blank_provider, cancel_with_dd, incorrect_td_date, duplicate_trips, single_legs,
                        ooa_trips, purpose_error_trips, comp_w_cancel, excessive_trips]
        
        

        
        add_flag_column_to_dataframes(flagged_dfs,flag_labels)
        flagged_trips= stack_dfs(flagged_dfs)

        flagged_lst = flagged_trips['Trip ID'].tolist()
        flagged_lst = [str(item) for item in flagged_lst]
        df['Trip ID'] = df['Trip ID'].astype(str)
        fiscal_summary = df.query("`Trip ID` not in @flagged_lst")
        self.drop_columns(fiscal_summary)
        #fiscal_summary = remove_matching_rows(df,flagged_trips,"Trip ID","Trip ID")
        
        #payable_dupes = self.pass_duplicate_trips()
        #payable_singles = self.single_legs_within_one_day()
        #payable_list = [payable_dupes, payable_trips]# payable_singles]
        #mr_payable_trips = stack_dfs(payable_list)
        
        return fiscal_summary, flagged_trips, taxi_questions
    
class SecondPaymentsAudit(AuditDataFrame):
    def __init__(self, data=None, columns=None, modes_df=None, county_df=None, purpose_df=None,
                cancel_types_df=None,second_payment_trip_id = None):
        super().__init__(data=data, columns=columns, modes_df=modes_df, county_df=county_df,
                            purpose_df=purpose_df, cancel_types_df=cancel_types_df)
        
        if second_payment_trip_id is None:
            self.second_payment_trip_id = self.format_second_payment_trip_id()
        else:
            self.second_payment_trip_id = second_payment_trip_id


        
        self.update_trip_dates()
        self.iso_secondary_audit_date_range()
        self.add_data()
        self.update_rate()



        
        
        

    def format_second_payment_trip_id(self):
       
        
        trip_id_df = pd.read_clipboard()
        trip_id_list = trip_id_df.iloc[:, 0].tolist()
        trip_id_list = [str(item) for item in trip_id_list]
        return trip_id_list
                    


    def run_secondary_audit(self):

        df = self.in_area_mileage_reimbursement()
        
        
        blank_provider = self.blank_provider_iso()
        cancel_with_dd = self.cancel_with_distribution_date()
        incorrect_td_date = self.incorrect_td_date()
        duplicate_trips = self.duplicate_trips()
        single_legs, _ = self.single_leg_trips()
        ooa_trips = self.ooa_export()
        purpose_error_trips = self.trip_purpose_error()
        comp_w_cancel = self.comp_with_cancel()    
        excessive_trips = self.excessive_trips()
        
        
        flagged_dfs = [blank_provider, cancel_with_dd, incorrect_td_date, duplicate_trips, single_legs,
                        ooa_trips, purpose_error_trips, comp_w_cancel, excessive_trips]
        
        sp_trip_id = self.second_payment_trip_id

        
        add_flag_column_to_dataframes(flagged_dfs,flag_labels)
        flagged_trips= stack_dfs(flagged_dfs)

        flagged_trips['Trip ID'] = flagged_trips['Trip ID'].astype(str) 
        
        sp_flagged_trips = flagged_trips.query("`Trip ID` in @sp_trip_id")

        df['Trip ID'] = df['Trip ID'].astype(str)
        sp_fiscal_summary = df.query("`Trip ID` in @sp_trip_id")
        self.drop_columns(sp_fiscal_summary)

        return sp_fiscal_summary, sp_flagged_trips

