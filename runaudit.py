import pandas as pd
import os
from util.auditclasses import WeeklyAudit , SecondPaymentsAudit
from datetime import datetime


file_path = input("Enter file path: ").strip('"')
export_df = pd.read_csv(file_path, encoding="ISO-8859-1", low_memory=False)
#audit = WeeklyAudit(data=export_df)

# fiscal_summary, flagged_trips, taxi_questions = audit.run_audit()


# current_date = datetime.now().date()
# formatted_date = current_date.strftime("%Y.%m.%d")

# # Specify the folder name
# folder_name = f"{formatted_date} MR Audit Results"

# # Get the desktop path
# desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# # Create the full path to the folder on the desktop
# folder_path = os.path.join(desktop_path, folder_name)

# # Create the folder on the desktop
# os.makedirs(folder_path, exist_ok=True)

# # Specify the file paths within the created folder
# payable_trips = os.path.join(folder_path, f"{formatted_date} Payable Trips.csv")
# flagged = os.path.join(folder_path, f"{formatted_date} Flagged Trips.csv")
# taxi_trips = os.path.join(folder_path, f"{formatted_date} Taxi Questions.csv")

# # Save flagged trips, fiscal summary, and taxi questions to CSV files
# flagged_trips.to_csv(flagged, index=False)
# fiscal_summary.to_csv(payable_trips, index=False)
# taxi_questions.to_csv(taxi_trips, index=False)

secondary = SecondPaymentsAudit(data=export_df)

sp_payments, sp_flagged_trips = secondary.run_secondary_audit()

sp_payments.to_csv("sp_payments.csv", index=False)
sp_flagged_trips.to_csv("sp_flagged.csv", index=False)
