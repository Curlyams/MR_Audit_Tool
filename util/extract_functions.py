
import pandas as pd
import numpy as np





def load_export_df(export_path):
    return pd.read_csv(export_path, encoding='ISO-8859-1', low_memory=False)

def load_master_sheet(question_path):
    return pd.read_excel(question_path, sheet_name=None)

def get_investigating_list(master_sheet_dict):
    investigating_df = master_sheet_dict['questions'].astype(str)
    return investigating_df['Trip ID'].tolist()

def get_paid_list(master_sheet_dict):
    paid_df = master_sheet_dict["Paid Out"].astype(str)
    return paid_df.iloc[:, 0].tolist()

def load_second_payments(second_payment_path):
    second_payments_df = pd.read_csv(second_payment_path, encoding='ISO-8859-1', low_memory=False).astype(str)
    second_payments_df.replace({'None': ''}, inplace=True)
    second_payments_df.replace({'none': ''}, inplace=True)
    second_payments_df.replace({'NONE': ''}, inplace=True)
    second_payments_df.replace({np.nan: ''}, inplace=True)
    return second_payments_df['Trip ID'].tolist()

def remove_second_payments_from_investigating_list(investigating_lst, second_payments_lst):
    return [x for x in investigating_lst if x not in second_payments_lst]

def load_additional_data():
    modes_df = pd.read_csv('Modes.csv')
    county_df = pd.read_csv("service_areas.csv")
    purpose_df = pd.read_csv("purpose_summary.csv")
    return modes_df, county_df, purpose_df

def clean_export_df(export_df):
    export_df.replace({'None': ''}, inplace=True)
    export_df.replace({np.nan: ''}, inplace=True)
    return export_df