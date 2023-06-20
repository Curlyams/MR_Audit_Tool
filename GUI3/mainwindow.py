# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (
    QCoreApplication,
    QPropertyAnimation,
    QDate,
    QDateTime,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
    QEvent,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide6.QtWidgets import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_dialog_ui import Ui_Dialog
from ui_error_ui import Ui_Error

# from ui_function import UIFunction
from about import *
from auditclasses import *
import gui_data as gd
from df_functions import *




from PySide6.QtCore import QThread, Signal


class WeeklyAuditWorker(QThread):
    progressUpdated = Signal(int)
    flags = Signal(list)
    payable = Signal(pd.DataFrame)
    taxi = Signal(pd.DataFrame)
    error = Signal(str)

    def __init__(self, checkboxes, function_lst, export_path, onlysec_audit, secweek_audit, parent=None):
        super().__init__(parent)
        self.checkboxes = checkboxes
        self.function_lst = function_lst
        self.export_path = export_path
        self.onlysec_audit = onlysec_audit
        self.secweek_audit = secweek_audit

    def run(self):
        # Define total number of steps
        total_steps = 9
        # Define step size
        step_size = 100 / total_steps
        progress = 0

        # Step 1: Reading CSV
        try:
            filename, file_extension = os.path.splitext(self.export_path)
            if file_extension != ".csv":
                raise ValueError(f"Unsupported file type: {file_extension}")

            with open(self.export_path, "r", encoding="ISO-8859-1") as file:
                export_df = pd.read_csv(file, low_memory=False)
        except FileNotFoundError:
            self.error.emit("File not found.")
            return
        except ValueError as ve:
            self.error.emit(str(ve))
            return
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 2: Creating WeeklyAudit object
        try:
            self.class_object = WeeklyAudit(export_df)
            self.class_object.update_trip_dates()
        except Exception as e:
            self.error.emit("Make sure you have the correct Columns in the Export: " + str(e))   
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 3: second payments or not 
        try:
            if not (self.onlysec_audit.isChecked() or self.secweek_audit.isChecked()):
                self.class_object.iso_weekly_audit_date_range()
            elif self.onlysec_audit.isChecked():
                self.class_object.iso_secondary_audit_date_range()
            elif self.secweek_audit.isChecked():
                self.error.emit("Second week audit is checked but no operation is defined for it.")
        except Exception as e:
            self.error.emit(f"Possible Date Range Error: {str(e)}")
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 4: Xlookups
        self.class_object.add_data()
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 5: Update provider rates
        self.class_object.update_rate()
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 6: in_area_mileage_reimbursement
        payable_df = self.class_object.in_area_mileage_reimbursement()
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 7: taxi_export
        taxi_df = self.class_object.taxi_export()
        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 8: Processing selected functions
        selected_functions = []
        flags = []

        for checkbox_name, function, label in zip(
            self.checkboxes, self.function_lst, flag_labels
        ):
            checkbox = getattr(self.parent().ui, checkbox_name)
            if checkbox.isChecked():
                selected_functions.append(function)
                flags.append(label)

        total = len(selected_functions)
        flag_lst = []

        for selected_function, flag in zip(selected_functions, flags):
            function_object = getattr(self.class_object, selected_function)
            result = function_object()
            try:
                if not result.empty:
                    result.insert(0, "Flag", flag)
            except Exception as e:
                self.error.emit(f"Error adding flag column to result:{str(e)}")

            flag_lst.append(result)

        progress += step_size
        self.progressUpdated.emit(int(progress))

        # Step 9: Emitting the results
        self.payable.emit(payable_df)
        self.taxi.emit(taxi_df)
        self.flags.emit(flag_lst)

        progress += step_size
        self.progressUpdated.emit(int(progress))



# OUR APPLICATION MAIN WINDOW :
# -----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ----> SET WINDOW TITLE AND ICON
        applicationName = " Member Reimbursement Audit Tool"
        self.setWindowTitle(
            applicationName
        )  # SETS THE APPLICATION NAME IN THE WINDOW TOPBAR                        ---------(C4)
        # EVENTHOW IT IS AVSENT THIS IS NECESSERY AS THE OPERATING SYSTEM RECOGNISES THE SOFTWARE SUING THIS NAME
        # SO YOU WILL SEE THE NAME ENTERED HERE IN THE TASKBAR, TITLEBAR, E.T.C
        UIFunction.labelTitle(
            self, applicationName
        )  # PASSING THE CODE TO SET THE TITLE TO THE CUSTOME TOPBAR IN OUR UI
        # THIS UOFunction CLASS IS IN THE FILE: ui_function.py.
        ###############################

        # -----> INITIAL STACKED WIDGET PAGE WIDGET AND TAB
        # THIS MAKE THE INITIAL WINDOW OF OUR APPLICATION, I.E. THE FIRST PAGE OR THE WELCOME PAGE/SCREEN            ---------(C5)
        # IN OUR APPLICATION THIS IS THE MENU BAR, TOODLE SWITCH, MIN, MAX, CLOSE BUTTONS, AND THE HOME PAGE.
        # ALL THIS GET INITIALISED HERE.
        # SINCE ALL THE FUNCTION RELATED STUFF IS DONE IN THE ui_function.py FILE, IT GOES THERE
        # REMEMBER THIS FUNCTION CAN ALSO BE DONE HERE, BUT DUE TO CONVINENCE IT IS SHIFTD TO A NEW FILE.
        UIFunction.initStackTab(self)
        ############################################################

        # ----> CERTAIN TOOLS LIKE DRAG, MAXIMISE, MINIMISE, CLOSE AND HIDING OF THE WINDOWS TOPBAR
        # THIS WINDOW INITIALISES THE BUTTONS NECESSERY FOR THE MAINWINDOW LIKE: CLOSE, MIN, MAX E.T.C.                ---------(C6)
        UIFunction.constantFunction(self)
        #############################################################

        # ----> TOODLE THE MENU HERE
        # THIS CODE DETETS THE BUTTON IN THE RIGHT TOP IS PRESSED OR NOT AND IF PRESSED IT CONNECT  TO A FUNCTION IN THE ui_function.py                 ---------(C7)
        # FILE, WHICH EXPANDS THE MENU BAR TO DOUBLE ITS WIDTH MAKING ROOM FOR THE ABOUT PAGES.
        # THIS EFFECT CALLED AS TOODLE, CAN BE MADE USE IN MANY WAYS. CHECK THE FUNCTION: toodleMenu: IN THE ui_function.py
        # FILE FOR THE CLEAR WORKING
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        #############################################################

        # ----> MENU BUTTON PRESSED EVENTS
        # NOW SINCE OUR DEMO APPLICATION HAS ONLY 4 MENU BUTTONS: Home, Bug, Android, Cloud, WHEN USER PRESSES IT THE FOLLOWING CODE             ---------(C8)
        # REDIRECTS IT TO THE ui_function.py FILE buttonPressed() FUNCTION TO MAKE THE NECESSERY RESPONSES TO THE BUTTON PRESSED.
        # IT TAKES SELF AND THE BUTTON NAME AS THE RGUMENT, THIS IS ONLY TO RECOGNISE WHICH BUTTON IS PRESSED BY THE buttonPressed() FUNCTION.
        self.ui.bn_home.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_home")
        )
        self.ui.bn_audit.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_audit")
        )
        self.ui.bn_settings.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_settings")
        )
        #############################################################

        # -----> STACK PAGE FUNCTION
        # OUR APPLICATION CHANGES THE PAGES BY USING THE STACKED WIDGET, THIS CODE POINTS TO A FUNCTION IN ui_function.py FILE             ---------(C9)
        # WHICH GOES AND SETS THE DEFAULT IN THESE PAGES AND SEARCHES FOR THE RESPONSES MADE BY THE USER IN THE CORRSPONDING PAGES.
        UIFunction.stackPage(self)
        #############################################################

        # ----> Getting the Paths the Export file
        self.ui.browseButton.clicked.connect(self.select_file)
        # ---> Run Audit Button
        self.ui.bn_audit_start.clicked.connect(self.run_audit)
        # ---> Connect SP Radio Buttons
        self.onlysec_audit = self.findChild(QRadioButton, "onlysec_audit")
        self.secweek_audit = self.findChild(QRadioButton, "secweek_audit")
        self.onlysec_audit.clicked.connect(self.radio_button_clicked)
        self.secweek_audit.clicked.connect(self.radio_button_clicked)

        # ---> initialising the output path for the export folder
        self.button_was_clicked = False
        self.ui.browseButton_output.clicked.connect(self.select_output_path)
        self.ui.browseButton_output.clicked.connect(self.custom_export_path)
        # ----> Initialising all potential outputs as None 
        self.flagged_trips = None
        self.payable_trips = None
        self.taxi_trips = None

        # ---> Creating an empty worker object
        self.worker = None
        #############################################################

        #############################################################
        # ---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER APPNAME LABEL
        # SAME TO SAY AS IN COMMENT (C2)
        self.dragPos = self.pos()

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE: WE CHOOSE THE TOPMOST FRAME WHERE THE APPLICATION NAME IS PRESENT AS THE AREA TO MOVE THE WINDOW.
        self.ui.frame_appname.mouseMoveEvent = moveWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG

    def radio_button_clicked(self):
        option1_selected = self.is_sp_only_selected()
        option2_selected = self.is_sp_selected()

    def is_sp_only_selected(self):
        return self.onlysec_audit.isChecked()

    def is_sp_selected(self):
        return self.secweek_audit.isChecked()

    def handle_text_changed(self, text):
        # process the pasted text as a list
        values_list = text.split(",")  # split by comma

        # Remove leading/trailing whitespace from each value
        values_list = [value.strip() for value in values_list]
        return values_list
    def select_output_path(self):
        #open a file dialog and get the selected path
        output_path = QFileDialog.getExistingDirectory(self, "Select Output Path")

        self.ui.lineEdit_resultOutput_path.setText(output_path)
    def select_file(self):
        # Open a file dialog and get the selected file path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")

        # Update the file path in the form
        self.ui.export_path.setText(file_path)

    def set_file_path(self, file_path):
        # Update the text of the QLineEdit widget
        self.ui.export_path.setText(file_path)


    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #----> Audit functions start here ----->
    ##############################################################
    #How we update the progress bar
    def update_progress(self, progress):
        self.ui.progressBar_audit.setValue(progress)
    #Function to select what to output
    def output_options(self):
        options = {
        "all_out": self.ui.checkBox_alloutputs.isChecked(),
        "payable_out": self.ui.checkBox_payableout.isChecked(),
        "flag_out": self.ui.checkBox_flagout.isChecked(),
        "taxi_out": self.ui.checkBox_taxiout.isChecked()
        }

        return options


#----> Audit worker this is the function that runs when you push start
#### it works in a separate thread to avoid blocking the GUI
### It will check what setting are selected and then run the audit


    def run_audit(self):
        # If the worker is not None and is still running, return to avoid starting another one simultaneously
        if self.worker is not None and self.worker.isRunning():
            return

        # Get the export path from the UI
        export_path = self.ui.export_path.text()
        
        # Instantiate a WeeklyAuditWorker with the appropriate checkboxes, functions, export path, and audit type
        self.worker = WeeklyAuditWorker(
            gd.flag_checkboxes_names, gd.function_names, export_path,
            self.onlysec_audit, self.secweek_audit, parent=self,
        )

        # Connect signals from the worker to their respective slots in this class.
        # When the worker updates its progress, we want to update the progress in the UI as well
        self.worker.progressUpdated.connect(self.update_progress)
        
        # When the worker emits flags, we want to process the flagged trips
        self.worker.flags.connect(self.process_flagged_trips)
        
        # When the worker emits taxi trips, we want to process the taxi trips
        self.worker.taxi.connect(self.process_taxi_trips)
        
        # When the worker emits payable trips, we want to process the payable trips
        self.worker.payable.connect(self.process_payable_trips)
        
        # When the worker emits an error, we want to handle the error
        self.worker.error.connect(self.handle_error)

        # Start the worker thread
        self.worker.start()

                
            
    
    def handle_error(self, error_message):
        # Display an error message box when an error occurs
        QMessageBox.critical(self, "Error", error_message, QMessageBox.Ok)
            
    def custom_export_path(self):
        # Set a flag to indicate that the custom export path button was clicked
        self.button_was_clicked = True

    def process_flagged_trips(self, flags):
        # Concatenate the flagged trips and if all data is ready, run the weekly audit
        self.flagged_trips = WeeklyAudit.concat_flagged_trips(flags)
        if self.is_data_ready():
            self.run_weekly_audit()

    def process_payable_trips(self, payable):
        # Assign payable trips and if all data is ready, run the weekly audit
        self.payable_trips = payable
        if self.is_data_ready():
            self.run_weekly_audit()

    def process_taxi_trips(self, taxi):
        # Assign taxi trips and if all data is ready, run the weekly audit
        self.taxi_trips = taxi
        if self.is_data_ready():
            self.run_weekly_audit()

    def is_data_ready(self):
        # Check if all data (flagged trips, payable trips, and taxi trips) is not None
        return all([self.flagged_trips is not None, self.payable_trips is not None, self.taxi_trips is not None])

    def folder_name(self):
        # Get current date and format it, then create a folder name using the formatted date
        current_date = datetime.now().date()
        formatted_date = current_date.strftime("%Y.%m.%d")
        folder_name = f"{formatted_date} MR Audit Results"
        return folder_name, formatted_date

    def iso_sp_trip_id(self):
        # Get the text from the lineEdit_sptripid and process it
        sp_trip_id = self.ui.lineEdit_sptripid.text()
        processed_trip_id = self.handle_text_changed(sp_trip_id)
        return processed_trip_id

    

            

    def run_weekly_audit(self):
        # Determine the type of audit to run based on the checks in the interface
        if not (self.onlysec_audit.isChecked() or self.secweek_audit.isChecked()):
            # If no specific audit type is checked, run a standard Weekly Audit
            flagged_trip_id = WeeklyAudit.get_flagged_trip_ids(self.flagged_trips)
            fiscal_summary = WeeklyAudit.get_fiscal_summary(self.payable_trips, flagged_trip_id)
        elif self.onlysec_audit.isChecked():
            # If only secondary audit is checked, run a Secondary Payments Audit
            try:
                sp_trip_id = self.iso_sp_trip_id()
                sp_flagged_trips = SecondPaymentsAudit.get_sp_flagged_trips(self.flagged_trips, sp_trip_id)
                fiscal_summary = SecondPaymentsAudit.get_sp_fiscal_summary(self.payable_trips, sp_trip_id)
                self.flagged_trips = sp_flagged_trips
            except Exception as e:
                self.handle_error(str(e))
        elif self.secweek_audit.isChecked():
            # If secondary week audit is checked, run a Second Week Payments Audit
            try:
                sp_trip_id = self.iso_sp_trip_id()
                flagged_trip_id = WeeklyAudit.get_flagged_trip_ids(self.flagged_trips)
                sp_flagged_trips = SecondPaymentsAudit.get_sp_flagged_trips(self.flagged_trips, sp_trip_id)
                sp_flagged_trip_ids = WeeklyAudit.get_flagged_trip_ids(sp_flagged_trips)
                all_flag_trip_id = flagged_trip_id + sp_flagged_trip_ids
                fiscal_summary = WeeklyAudit.get_fiscal_summary(self.payable_trips, all_flag_trip_id)
                all_flagged_trips = SecondPaymentsAudit.get_sp_flagged_trips(self.flagged_trips, all_flag_trip_id)
                self.flagged_trips = all_flagged_trips
            except Exception as e:
                self.handle_error(str(e))

        # Get the output options and the folder name
        options = self.output_options()
        folder_name, formatted_date = self.folder_name()

        # Determine the base output path, defaulting to the desktop
        if self.button_was_clicked:
            base_path = self.ui.lineEdit_resultOutput_path.text()
        else:
            base_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Create the output folder
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Save outputs to the chosen folder based on options
        if options["payable_out"]:
            payable_trips = os.path.join(folder_path, f"{formatted_date} Payable Trips.csv")
            fiscal_summary.to_csv(payable_trips, index=False)
        if options["flag_out"]:
            flagged = os.path.join(folder_path, f"{formatted_date} Flagged Trips.csv")
            self.flagged_trips.to_csv(flagged, index=False)
        if options["taxi_out"]:
            taxi_trips = os.path.join(folder_path, f"{formatted_date} Taxi Questions.csv")
            self.taxi_trips.to_csv(taxi_trips, index=False)


GLOBAL_STATE = 0  # NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = (
    True  # NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
)
init = False  # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE


# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):
    # ----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE
    # INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init == False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True

    ################################################################################################

    # ------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)

    ################################################################################################

    # ----> MAXIMISE/RESTORE FUNCTION
    # THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    # THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore")
            self.ui.bn_max.setIcon(
                QtGui.QIcon("icons/1x/restore.png")
            )  # CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide()  # HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(
                QtGui.QIcon("icons/1x/max.png")
            )  # CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()

    ################################################################################################

    # ----> RETURN STATUS MAX OR RESTROE
    # NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # ------> TOODLE MENU FUNCTION
    # THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    # ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    # IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE
    # HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):
        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = (
                self.ui.frame_bottom_west.width()
            )  # Reads the current width of the frame
            minWidth = 80  # MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth == 80:
                extend = maxWidth
                # ----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                # -----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            # THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(
                self.ui.frame_bottom_west, b"minimumWidth"
            )
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ################################################################################################

    # -----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        # -----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        # ----> REMOVE NORMAL TITLE BAR
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()


        # SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        # DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        # -----> MINIMIZE BUTTON FUNCTION
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())

    ################################################################################################################

    # ----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):
        index = self.ui.stackedWidget.currentIndex()

        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName == "bn_home":
            if self.ui.frame_bottom_west.width() == 80 and index != 0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif (
                self.ui.frame_bottom_west.width() == 160 and index != 1
            ):  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == "bn_audit":
            if self.ui.frame_bottom_west.width() == 80 and index != 5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_audit)
                self.ui.lab_tab.setText("Audit")
                self.ui.frame_audit.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif (
                self.ui.frame_bottom_west.width() == 160 and index != 4
            ):  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_audit)
                self.ui.lab_tab.setText("About > Audit")
                self.ui.frame_audit.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == "bn_settings":
            if self.ui.frame_bottom_west.width() == 80 and index != 7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
                self.ui.lab_tab.setText("Audit Settings")
                self.ui.frame_settings.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                UIFunction.settingsStackPages(self, "page_clean")

            elif (
                self.ui.frame_bottom_west.width() == 160 and index != 3
            ):  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_settings)
                self.ui.lab_tab.setText("About > Audit Settings")
                self.ui.frame_settings.setStyleSheet(
                    "background:rgb(91,90,90)"
                )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST


    ########################################################################################################################

    # ----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):
        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        self.ui.lab_home_main_hed.setText("Profile")
        self.ui.lab_home_stat_hed.setText("Stat")

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug
        # self.ui.bn_audit_start.clicked.connect(lambda: APFunction.addNumbers(self, 100000, True))

        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        # ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        self.ui.bn_settings_clean.clicked.connect(
            lambda: UIFunction.settingsStackPages(self, "page_clean")
        )
        self.ui.bn_settings_world.clicked.connect(
            lambda: UIFunction.settingsStackPages(self, "page_world")
        )

        ######ANDROID > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        self.ui.bn_android_contact_delete.clicked.connect(
            lambda: self.dialogexec(
                "Warning",
                "The Contact Infromtion will be Deleted, Do you want to continue.",
                "icons/1x/errorAsset 55.png",
                "Cancel",
                "Yes",
            )
        )

        self.ui.bn_android_contact_edit.clicked.connect(
            lambda: APFunction.editable(self)
        )

        self.ui.bn_android_contact_save.clicked.connect(
            lambda: APFunction.saveContact(self)
        )

        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        self.ui.text_about_home.setText(aboutHome)

    ################################################################################################################################

    # -----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE.
    def settingsStackPages(self, page):
        # ------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_settings_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_clean":
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_settings_clean)
            self.ui.lab_tab.setText("Android > Clean")
            self.ui.frame_settings_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_settings.setCurrentWidget(self.ui.page_android_world)
            self.ui.lab_tab.setText("Android > World")
            self.ui.frame_settings_world.setStyleSheet("background:rgb(91,90,90)")

        # ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE ANDROID STACK PAGE.

    ##############################################################################################################


# ------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
# REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE
class APFunction:
    def __init__(self):
        super().__init__()

    # -----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    def addNumbers(self, number, enable):
        if enable:
            lastProgress = 0
            for x in range(0, int(number), 1):
                progress = int((x / int(number)) * 100)
                if progress != lastProgress:
                    self.ui.progressBar_audit.setValue(progress)
                    lastProgress = progress
            self.ui.progressBar_audit.setValue(100)



###############################################################################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

#######################
