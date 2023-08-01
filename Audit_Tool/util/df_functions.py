import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def xlookup(lookup_value, lookup_array, return_array, if_not_found=""):
    """
    A function that performs an approximate match lookup in a return array based on a lookup value in a lookup array.

    Parameters:
    -----------
    lookup_value: Any
        The value to look up in the lookup array.
    lookup_array: list, array-like or Series
        The array or Series where the function looks up the lookup_value.
    return_array: list, array-like or Series
        The array or Series from which the function returns the matching value.
    if_not_found: str, optional
        The default value to return if no approximate match is found in the lookup_array.
        If not specified, the function returns "blank" if no match is found.

    Returns:
    --------
    Any
        The matching value in the return_array if a match is found.
        The default value specified by if_not_found argument otherwise.
        "blank" if no default value is specified and no match is found.
    """
    lookup_array = np.array(lookup_array)  # Convert lookup_array to numpy array
    return_array = np.array(return_array)  # Convert return_array to numpy array
    match_value = return_array[
        np.isin(lookup_array, lookup_value)
    ]  # Use numpy's isin() method to check for matches
    if (
        match_value.size == 0
    ):  # If no match is found, return either the default value or "blank" if no default value is specified
        return "N/A" if if_not_found == "" else if_not_found
    else:  # If a match is found, return the first match in the match_value array
        return match_value[0]


def add_present(df, check_col, present_col):
    # iterate over each row in the dataframe
    for index, row in df.iterrows():
        # check if the value in the specified check column for the current row is not empty
        if not pd.isna(row[check_col]) and str(row[check_col]).strip():
            # if the value is not empty, add "present" to the specified present column for the current row
            df.at[index, present_col] = "present"

    # return the updated dataframe
    return df


# adds flags to columns of dataframes


def add_flag_column_to_dataframes(dfs, values):
    for df, value in zip(dfs, values):
        try:
            if not df.empty:
                df.insert(0, "Flag", value)

        except:
            print(f"Error adding flag column to {df}")
    return dfs


def stack_dfs(df_lst):
    """
    A function that takes a list of dataframes and stacks them on eachother into a single dataframe

    Parameters:
    -----------
    df_lst: A list of dataframes that you want to stack

    Returns:
    --------
    stacked_df: A single dataframe consisting of the dataframes in df_lst, stacked on eachother.
    """
    stacked_df = pd.concat(df_lst, ignore_index=True)
    try:
        stacked_df = stacked_df.drop(
            columns=[
                "Backdating Process",
                "Mode",
                "Trip Status Summary",
                "Purpose Summary",
                "Mileage vs NOT-Mileage vs PR/BT",
            ]
        )
    except:
        pass

    return stacked_df


def add_yes_no(df, check_col, yes_no_col):
    # iterate over each row in the dataframe
    td_variations = ("td", "tD", "Td", "TD")
    for index, row in df.iterrows():
        # check if the value in the specified check column for the current row starts with "td"
        if str(row[check_col]).startswith(td_variations):
            # if the value starts with "td", add "yes" to the specified yes/no column for the current row
            df.at[index, yes_no_col] = "yes"
        else:
            # if the value does not start with "td", add "no" to the specified yes/no column for the current row
            df.at[index, yes_no_col] = "no"

    # return the updated dataframe
    return df


def remove_matching_rows(df1, df2, column_df1, column_df2):
    """
    Remove rows from df1 where the values of column_df1 exist in df2's column_df2.

    Args:
    df1 (pd.DataFrame): The DataFrame from which rows will be removed.
    df2 (pd.DataFrame): The DataFrame that contains values that need to be checked against df1.
    column_df1 (str): The column in df1 that will be checked against df2.
    column_df2 (str): The column in df2 that will be checked against df1.

    Returns:
    pd.DataFrame: A new DataFrame based on df1 but without the rows that match df2[column_df2].
    """
    # Create a set of unique values as strings in df2[column_df2]
    values_to_remove = set(str(val) for val in df2[column_df2])

    # Remove rows where df1[column_df1] matches values_to_remove
    df1_filtered = df1[~df1[column_df1].astype(str).isin(values_to_remove)]

    return df1_filtered



# Function to return a range of dates between start_date and end_date
def get_date_range(start_date, end_date):
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

def get_weekly_audit_date_range():
    delta = timedelta(days=67)
    today = datetime.today()
    audit_range_end = today - timedelta(days=today.weekday() + 1)
    audit_range_start = audit_range_end - delta
    audit_range_start_date = audit_range_start.strftime("%m/%d/%Y")
    audit_range_end_date = audit_range_end.strftime("%m/%d/%Y")
    return audit_range_end_date, audit_range_start_date

def iso_weekly_audit_date_range(df):
    audit_end_date, audit_start_date = get_weekly_audit_date_range()

    df = df[
        (df["Trip Date"] >= audit_start_date)
        & (df["Trip Date"] <= audit_end_date)
    ]
    return df

def iso_secondary_audit_date_range(df):
    _, audit_start_date = get_weekly_audit_date_range()
    df["Trip Date"] = pd.to_datetime(df["Trip Date"], format="%m/%d/%Y")
    df = df[df["Trip Date"] < audit_start_date]
    return df