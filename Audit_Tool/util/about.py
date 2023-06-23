

# THIS FILE IS DEDICATED FOR THE ABOUT PAGE IN THE APPLICATION WHICH ACTS AS A OR AS A HELP TAB OF THE SOFTWARE APPLICATION
#KEEP ALL YOUR ABOUT IN ONE PLACE, ASSIGN IT TO A VARIABLE AND THEN IMPORT THIS FILE TO MAIN.PY FILE, AN DUSE THIS VARIABLE FOR THE DOCUMENT.
aboutHome = """
WEEKLY AUDIT SETUP:

1. Create a folder for the current weeks audit and name it "YYYY.MM.DD-YYYY.MM.DD MR Audit" Calculate the date range
totalling 67 days, ending with the Sunday of the current week.

2. Copy the yyyyy.mm.dd Summary for Fiscal ($00.00) from the Audit Templates folder to the newly created folder.


EXPORT DOWNLOAD: 

1. Go to ecolane and navigate to the tab Tools > Archive Trip Export

2. Under "Export Profile", select "Reimbursement Audit"

3. Under "Time Period", selct desired data range. The tool will automatically isolate the trips within 67 days and the trips outside the 67 days.

4. Click "Export" then "View export files" at the bottom of the screen.

5. When the list of export files loads, yours will be at the top; click "download" and open the file.

6. Save the file as "YYYY.MM.DD-YYYY.MM.DD MR Export.csv" in the desired location. Use this file to run the audit. 
Make sure the file is in CSV format.

SECOND PAYMENTS:

1. Isolate the trip IDs of the second payment trips. Store them in a place where you can easily copy and paste them.

2. When you paste them, make sure they are in the right format. They must be pasted from a column or a row. Just make sure they have spaces between
each other. 

3. Go to the settings tab and select one of the second payment options. Then paste the isolated trip IDs into the text box below.
To undo the second payment, click the "clear all" radio button at the bottom. 

FISCAL SUMMARY, FLAGGED TRIPS, AND TAXI QUESTIONS:

1. The tool will output three different files. First will be the Fiscal Summary file, second will be the Flagged Trips file, and thrird will be the Taxi Questions file.

2. Using the fiscal summary template file, copy the results from the tool and paste them into the fiscal summary file. Submit this file to payments, via the MR Audit Form on the teams channel.

3. Take the flagged trips file and paste the results into the QUESTION IMPORT file found in the sharepoint folder.

4. Email the taxi question files to whoever is in charge of Taxi Reimbursement. 

5. Once payments has approved the fiscal summary. Update ecolane via the comtrans tool. 

 """


aboutAudit = """
AUDIT INSTRUCTIONS:

1. You can either copy the path of the audit Export file or use the browse button to select the file. Makes sure the file is in csv format. Also make sure that you have all the correct columns to perform the audit.

    "Client First Name", "Client Last Name", "Customer Number", "Trip ID", "Trip Date", "Trip Status",
    "Cancel Type", "Verification", "OSA or Negotiated Rate", "Distribution Date",
    "Pick-up County", "Pick-up Street Number", "Drop-off County", "Drop-off Street Number",
    "Purpose", "Funding Source", "Fare Distance Rounded Miles", "Transportation Provider",
    "Provider Rate".

    If you don't have these columns, the tool will not work!

2. If you want to customize the outputs or to add second payments, you can do so by clicking on the "Settings" tab.

3. After you are ready click the "Start" button to the right of the screen. If everything is done correctly, the progress bar will starting increasing.
the bar will stop for a few seconds at 11% this is normal, this part of the process is pretty intensive. 

4. The audit is finished when the progress bar reaches 100%. By default you will find the results in your Desktop labeled as "<Today's Date> Audit Results".
You can change the output location in the settings tab. 

"""

aboutSettings = """
AUDIT SETTINGS:

1. On the left side of the window, you will find checkboxes under the label "Audit Flags" you can select any number of these and the tool will only check for those flags. 
Be sure to select at least one flag. The tool will not work otherwise. 

2. In the middle of the window, you will find Radio buttons. The "Secondary Audit Only" when selected will only return the results of the trips that was pasted in the box below. 
If the "Include Secondary Audit With Weekly" is selected, the tool will include the second payment trips with the weekly audit. Only one can be selected at a time, use the clear selection button at the bottom
to unselect both.

3. Under "Choose What Folders To Output", you can select any number of the the folders and you will output the results to the desired folder. 

4. Under "Audit Output" you can select the destination for the audit results. By default it will be the Desktop folder. Either click browse to browse or paste the path to desired location. 

5. Once you have selected your settings, click the "Start" button in the "Audit" tab. 

"""

















































