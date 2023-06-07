import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import xlrd
from trip_data import *
from df_functions import *





class AuditDataFrame:
    def __init__(self, data=None, columns=None, modes_df=None, county_df=None, purpose_df=None,
                  cancel_types_df=None):
        if data is None:
            self.df = pd.DataFrame()
        else:
            self.df = pd.DataFrame(data, columns=columns)
            self.add_backdating_column()
            self.add_columns()
            self.lower_case_counties()
            self.replace_none_and_nan()
            self.change_value('',.65, 'Provider Rate')
            self.change_value('',1, 'Fare Distance Rounded Miles')
            self.change_value(0,1, 'Fare Distance Rounded Miles')
            self.update_trip_dates()
        
        self.modes_df,self.county_df,self.purpose_df, self.cancel_types_df = load_additional_data()



    def __getitem__(self, column_name):
        return self.df[column_name].values
    
    def add_backdating_column(self):
        self.df = add_yes_no(self.df, 'Distribution Date', 'Backdating Process')
    
    def add_columns(self):
        new_col_names = ['Mode', "Trip Status Summary"]
        self.df = self.df.reindex(columns=self.df.columns.tolist() + new_col_names)

    def lower_case_counties(self):
        try:
            self.df['Pick-up County'] = self.df['Pick-up County'].str.lower()
            self.df['Drop-off County'] = self.df['Drop-off County'].str.lower()
        except:
            pass

    def replace_none_and_nan(self):
        self.df = self.df.replace({'none': '',np.nan: ''}, regex=True, inplace=False)


    
    def load_mr_export(self, file_path):
        self.df = pd.read_csv(file_path, encoding='ISO-8859-1', low_memory=False)
        self.add_backdating_column()
        self.add_columns()
        self.lower_case_counties()
        self.replace_none_and_nan()
        self.change_value('',.65, 'Provider Rate')
        self.change_value('',1, 'Fare Distance Rounded Miles')
        self.change_value(0,1, 'Fare Distance Rounded Miles')
        self.update_trip_dates()
        



    def create_array(self,*args):
        return np.concatenate(args)
    
    def save_csv(self, file_path):
        self.df.to_csv(file_path, index=False)

        


            
    def concat_dataframes(self, *args):
        return pd.concat([self.df, *args], ignore_index=True)
    
    def change_dtype(self, column_name, dtype):
        self.df[column_name] = self.df[column_name].astype(dtype)

    def date_formatter(self, excel_date):
        try:
            formatted_date = excel_date.strftime("%m/%d/%Y")
            return formatted_date
        except:
            date_tuple = xlrd.xldate_as_tuple(excel_date, 0)
            year, month, day, _, _, _ = date_tuple
            date = datetime(year, month, day).date()
            formatted_date = date.strftime("%m/%d/%Y")
            return formatted_date

    def get_weekly_audit_date_range(self):
        delta = timedelta(days=67)
        today = datetime.today()
        audit_range_end= today - timedelta(days=today.weekday() + 1 )
        audit_range_start = audit_range_end - delta
        audit_range_start_date = audit_range_start.strftime("%m/%d/%Y")
        audit_range_end_date = audit_range_end.strftime("%m/%d/%Y")
        return audit_range_end_date , audit_range_start_date

    def get_date_range(self, start_date, end_date):


        if isinstance(start_date, str):
            formatted_start_date = pd.to_datetime(start_date)
        else:
            formatted_start_date = start_date

        if isinstance(end_date, str):
            formatted_end_date = pd.to_datetime(end_date)
        else:
            formatted_end_date = end_date

        date_range = pd.date_range(start=formatted_start_date, end=formatted_end_date)

        formatted_date_range = [date.strftime("%m/%d/%Y") for date in date_range]

        return formatted_date_range

    def iso_weekly_audit_date_range(self):
        audit_end_date, audit_start_date = self.get_weekly_audit_date_range()
        
        date_range = self.get_date_range(audit_start_date, audit_end_date)
        trips_in_range_df = pd.DataFrame()
        for date in date_range:
           trip_in_range = self.df[self.df["Trip Date"] == date]
           trips_in_range_df = trips_in_range_df.append(trip_in_range, ignore_index=True)
        self.df = trips_in_range_df
           

    def add_data(self):
        
        self.df["Mode"] = self.xlookup_columns(self.df['Transportation Provider'], self.modes_df['Transportation Provider'], self.modes_df['Mode'])
        self.df["Trip Status Summary"] = self.xlookup_columns(self.df['Trip Status'], self.cancel_types_df['Trip Status'], self.cancel_types_df['Summary'])
        self.df["Purpose Summary"] = self.xlookup_columns(self.df['Purpose'], self.purpose_df['Purpose'], self.purpose_df['Purpose Summary'])
        self.df["Mileage vs NOT-Mileage vs PR/BT"] = self.xlookup_columns(self.df['Transportation Provider'], self.modes_df['Transportation Provider'], self.modes_df['Mileage vs NOT-Mileage vs PR/BT'])

    def xlookup_columns(self, search_column, target_column, result_column):
        return search_column.map(dict(zip(target_column, result_column)))
    def update_provider_rate(self, multiplier, start_date, end_date):

        new_df = self.df.copy()
        date_range = self.get_date_range(start_date, end_date)
        new_col_name = f"FDRM * {multiplier}"
        for date in date_range:
            new_df.loc[new_df["Trip Date"] == date, new_col_name] = new_df.loc[new_df["Trip Date"] == date, 'Fare Distance Rounded Miles'] * multiplier
        new_df = new_df.dropna(subset=[new_col_name])

        return new_df        

    def update_trip_dates(self):
        self.df["Trip Date"] = self.df["Trip Date"].apply(self.date_formatter)

    def drop_nan_values(self,column_name):
        self.df = self.df.dropna(subset=[column_name])

    def nan_to_value(self, value, column_name):
        self.df[column_name] = self.df[column_name].fillna(value)

    def change_value(self, old_value,new_value, column_name):
        self.df[column_name] = self.df[column_name].replace(old_value, new_value)

    def drop_rows_starts_with(self, column_name, starts_with):
        self.df = self.df[~self.df[column_name].str.startswith(starts_with)]
    

    def subtract_features(self,first_feature, second_feature,column_name):
        self.df[column_name] = self.df[first_feature] - self.df[second_feature]

    def display_data(self):
        df = self.df.copy()
        print(df)


    
class SecondPaymentsAudit(AuditDataFrame):
    def __init__(self, data=None, columns=None, modes_df=None, county_df=None, purpose_df=None,
                cancel_types_df=None):
        super().__init__(data=data, columns=columns, modes_df=modes_df, county_df=county_df,
                            purpose_df=purpose_df, cancel_types_df=cancel_types_df)
        
class WeeklyAudit(AuditDataFrame):
    def __init__(self, data=None, columns=None, modes_df=None, county_df=None, purpose_df=None,
                 cancel_types_df=None):
    
        super().__init__(data=data, columns=columns, modes_df=modes_df, county_df=county_df,
                         purpose_df=purpose_df, cancel_types_df=cancel_types_df)
        

        self.iso_weekly_audit_date_range()
        self.update_rate()
        

    def update_rate(self):
        #df = pd.DataFrame()
        for index, row in self.df.iterrows():
            self.df.at[index, 'Provider Rate'] = round((0.65 * row['Fare Distance Rounded Miles']),2)


    def incorrect_provider_rate(self):
        df = self.df.copy()       
        df = df.query(
        "`Trip Status Summary` == 'comp etc.' and `Distribution Date` == '' and `Backdating Process` == 'no' and `Transportation Provider` == 'Reimbursement Mileage'"
    )
        #incorrect_65_rate = (df['Provider Rate'] != df['Fare Distance Rounded Miles'] * 0.65)
        incorrect_25_rate = (df['Provider Rate']!= df['Fare Distance Rounded Miles'] * 0.25)
        df = df[incorrect_25_rate]
        return df


    def cancel_with_distribution_date(self):
        df = self.df.copy()
        df = df.query( #and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty add this to remove OOA from flag
        "`Trip Status Summary` == 'cx/NS' and `Distribution Date` not in @exclude and `Backdating Process` == 'no'"
        )
        return df


    def blank_provider_iso(self):
        df = self.df.copy()
        df = df.query(
        "`Transportation Provider` == '' and `Trip Status Summary` == 'comp etc.' and `Backdating Process` == 'no'"
        )
        return df
        

    def incorrect_td_date(self):
        df = self.df.copy()
        df = df.query(
            "`Backdating Process` == 'yes'"
        )
        return df

    def duplicate_trips(self):
        #tricounty = ['clackamas', 'clackamas county', 'multnomah', 'multnomah county', 'washington', 'washington county']
        df = self.df.copy()
        df = df.query(
            "`Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty"
            ).astype(str)
        # Combine data in columns into one column named 'Date at PU + DO for Member'
        df['Date at PU + DO for Member'] = df['Trip Date'] + ' at ' + df['Pick-up Street Number'] + \
            ' + ' + df['Drop-off Street Number'] + ' for ' + df['Customer Number']
         # Count occurrences of non-reimbursement trips and mileage for members on the same date, pick-up, and drop-off
        not_reimbursements = df.loc[
            df['Mileage vs NOT-Mileage vs PR/BT'] == 'Private Rides or Bus Ticket', 'Date at PU + DO for Member'].value_counts()
        mileage_reimbursements = df.loc[
            df['Mileage vs NOT-Mileage vs PR/BT'] == 'Mileage', 'Date at PU + DO for Member'].value_counts()
        # Add counts to ther respective rip rows
        df['Not Reimbursement'] = df['Date at PU + DO for Member'].map(not_reimbursements)
        df['Mileage Reimbursements'] = df['Date at PU + DO for Member'].map(mileage_reimbursements)

         # Replace NaN values with 0 so we can sum up the columns
        df[['Not Reimbursement', 'Mileage Reimbursements']] = df[['Not Reimbursement', 'Mileage Reimbursements']].fillna(0)

        df['Mileage Count + Not Reimbursement'] = df['Not Reimbursement'] + df['Mileage Reimbursements']

         # Create a DataFrame for all trips flagged as DUPLICATES ACROSS MODES
        duplicate_trips = df[
        ((df['Mileage Reimbursements'] >= 1) & (df['Mileage Count + Not Reimbursement'] > df['Mileage Reimbursements'])) |
        (df['Mileage Reimbursements'] >= 2)
        ]


        return duplicate_trips

    def pass_duplicate_trips(self):
        duplicate_trips = self.duplicate_trips()
        duplicate_trips = duplicate_trips.query("`Transportation Provider` == 'Reimbursement Mileage'")
        payable_duplicate_trips = duplicate_trips['Date at PU + DO for Member'].drop_duplicates(keep = 'first')
        payable_duplicate_trips_df = duplicate_trips.loc[payable_duplicate_trips.index]
        return payable_duplicate_trips_df

    def single_leg_trips(self):
        df = self.df.copy()
        df = df.query("`Mileage vs NOT-Mileage vs PR/BT` in ['Private Rides or Bus Ticket', 'Mileage'] and `Trip Status Summary` == 'comp etc.' and `Pick-up County` in @tricounty and `Drop-off County` in @tricounty").astype(str)
        df['Date for Member'] = df['Trip Date'] + ' ' + df['Customer Number']
        not_reimbursements = df.loc[df['Mileage vs NOT-Mileage vs PR/BT'] == 'Private Rides or Bus Ticket', 'Date for Member'].value_counts()
        mileage_reimbursements = df.loc[df['Mileage vs NOT-Mileage vs PR/BT'] == 'Mileage', 'Date for Member'].value_counts()
        df['Not Reimbursement'] = df['Date for Member'].map(not_reimbursements)
        df['Mileage Reimbursements'] = df['Date for Member'].map(mileage_reimbursements)
        df[['Not Reimbursement', 'Mileage Reimbursements']] = df[['Not Reimbursement', 'Mileage Reimbursements']].fillna(0)
        df['Mileage Count + Not Reimbursement'] = df['Not Reimbursement'] + df['Mileage Reimbursements']
        single_across_modes = df[(df['Mileage Reimbursements'] == 1) & (df['Mileage Count + Not Reimbursement'] == 1)]
        return single_across_modes , df

    def excessive_trips(self):
        _, df = self.single_leg_trips()
        df['Mileage Reimbursements'] = df['Mileage Reimbursements'].astype(int)
        excessive_trips = df.query(
            "`Mileage Reimbursements` > 4 and `Transportation Provider` == 'Reimbursement Mileage'"
        )

        return excessive_trips
     
    
    def single_legs_within_one_day(self):
        single_legs_within_one_day_df = pd.DataFrame()
        prev_row = None
        single_trips,_= self.single_leg_trips()
        single_trips = single_trips.sort_values(['Customer Number', 'Trip Date'])  # Sort by Customer Number and Trip Date
        for index, row in single_trips.iterrows():
            if prev_row is None or row['Customer Number'] != prev_row['Customer Number']:
                prev_row = row
            else:
                current_date = datetime.strptime(row['Trip Date'], '%m/%d/%Y')
                prev_date = datetime.strptime(prev_row['Trip Date'], '%m/%d/%Y')
                date_difference = (current_date - prev_date).days
                if abs(date_difference) <= 1:
                    single_legs_within_one_day_df = single_legs_within_one_day_df.append(row, ignore_index=True)
                    single_legs_within_one_day_df = single_legs_within_one_day_df.append(prev_row, ignore_index=True)

                prev_row = row

        return single_legs_within_one_day_df 

    def taxi_export(self):
        df = self.df.copy()

        df = df.query(
            "`Mode` == 'Reimbursement'"
        )
        df = df.query(
            "`Transportation Provider` != '' and `Trip Status Summary` == 'comp etc.' and `Backdating Process` == 'no' and `Distribution Date` == '' "
        )
        df = df.query(
            "`Trip Status` == 'comp' and `Transportation Provider` == 'Reimbursement Taxi'"  
        )
        return df

    def ooa_export(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement' "
            )
        df = df.query(
            "`Pick-up County` not in @tricounty or `Drop-off County` not in @tricounty"
            )

        return df
    
    def trip_purpose_error(self):
        df = self.df.copy()
        df = df.query(
        "`Mode` == 'Reimbursement' "
        )
        df = df.query(
            "`Funding Source` == 'Ride to Care' and `Purpose Summary` == 'Non-covered service'"

            )
        return df

    def comp_with_cancel(self):
        df = self.df.copy()
        df = df.query(
            "`Mode` == 'Reimbursement'"
        )
        df = df.query(
            " `Transportation Provider` != '' and `Trip Status` == 'comp' and `Mileage vs NOT-Mileage vs PR/BT` == 'Mileage' and `Distribution Date` == '' and `Cancel Type` not in ('','Not Selected')"
            )
        return df

# file_path = "C:\\Users\\bcurl\\Desktop\\Audit_Tool_2.0\\util\\2023.03.23-2023.05.28 MR Export.csv"
# export_df = pd.read_csv(file_path)
# test = WeeklyAudit(export_df)
# #test.load_mr_export(file_path)
# test.add_data()
# test.cancel_with_distribution_date()
# test.display_data()
