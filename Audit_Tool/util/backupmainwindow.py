# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import  (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_dialog_ui import Ui_Dialog
from ui_error_ui import Ui_Error
#from ui_function import UIFunction
from about import *

class dialogUi(QDialog):
    def __init__(self, parent=None):

        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # REMOVING WINDOWS TOP BAR AND MAKING IT FRAMELESS (AS WE HAVE AMDE A CUSTOME FRAME IN THE WINDOW ITSELF)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # MAKING THE WINDOW TRANSPARENT SO THAT TO GET A TRUE FLAT UI

        #############################################################################################                        -------(C1)
        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON OF DIALOGBOX
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.d.bn_close.clicked.connect(lambda: self.close())

        #-----> THIS FUNCTION WILL CHECKT WEATHER THE BUTRTON ON THE DIALOGBOX IS CLICKED, AND IF SO DIRECTS TO THE FUNCTINON : diag_return()
        self.d.bn_east.clicked.connect(lambda: self.close())
        self.d.bn_west.clicked.connect(lambda: self.close())
        ##############################################################################################

    ##################################################################################################                        ------(C2)
        #SINCE THERE I S NO TOP BAR TO MOVE THE DIALOGBOX OVER THE SCREEN WE HAVE TO DEFINE THE MOUSE EVENT THAT IS RESPONSIBLE FOR THE
        #MOVEMENT. THIS IS CARRIED BY THIS FUNCTION
        #---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER DIALOGBOX TOPBAR
        self.dragPos = self.pos()   #INITIAL POSOTION OF THE DIALOGBOX
        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.d.frame_top.mouseMoveEvent = movedialogWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG
        ################
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #################################################################################################

    #################################################################################################                        ------(C3)
    #THE DIALOG BOX IS DESIGNED TO BE CALLED FROM ANY WHERE IN THE UI WITH ABLE TO CHANGE THE STATRE OF THE TEXT SHOWN, BUTTON NAMES E.T.C
    #THIS IS MADE BY CALLING THIS FUNCTION WHICH TAKES: HEADING, MESSAGE, ICON, BUTTON NAME 1, BUTTON NAME 2 AS ARUMENT.
    #EMBED THE GIVEN PROPERT TO THE DIALOGBOX AND FINALLY DISPLAYS IT IN THE WINDOW.
    #-------> SETTING THE DIALOGBOX CONFIGRATION: TEXT IN BUTTON, LABEL, HEADING
    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)
    ##################################################################################################



#ERRORBOX CREATES A SAMLL WINDOW TO DISPLAY THAT SOMETHING THAT THE USER PERFORMED HAS WENT WRONG.
#THIS CLASS ALSO HAS THE SAME PROPERTY AS THE DIALOGBOX CLASS WITH THE EXCEPTION THAT BOTH HAVE DIFFERENT UI INTERFACE ANS DIFFERENT APPLICATION.
#------> ERROR BOX GIVING THE ERROR OCCURED IN THE PROCESS: TAKES THE HEADING, ICON AND BUTTON NAME
class errorUi(QDialog):
    def __init__(self, parent=None):

        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #-----> CLOSE APPLICATION FUNCTION BUTTON: CORRESPONDING TO THE bn_ok OF THE ERRORBOX
        self.e.bn_ok.clicked.connect(lambda: self.close())

#SAME AD DESCRIBED IN COMMEND (C2)
#---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER ERRORBOX TOPBAR
        self.dragPos = self.pos()   #INITIAL POSOTION OF THE ERRORBOX
        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.e.frame_top.mouseMoveEvent = moveWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE ERRORBOX DURING MOUSE DRAG
        ################
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
#############################################

    # SAME AS DESCRIBED IN COMMEND (C3)
    #-------> SETTING THE ERRORBOX CONFIGRATION: TEXT IN BUTTON, LABEL, HEADING
    def errorConstrict(self, heading, icon, btnOk):
        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(btnOk)
        pixmap2 = QtGui.QPixmap(icon)
        self.e.lab_icon.setPixmap(pixmap2)




# OUR APPLICATION MAIN WINDOW :
#-----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #----> SET WINDOW TITLE AND ICON
        applicationName = "Member Reimbursement Audit Tool"
        self.setWindowTitle(applicationName) #SETS THE APPLICATION NAME IN THE WINDOW TOPBAR                        ---------(C4)
        #EVENTHOW IT IS AVSENT THIS IS NECESSERY AS THE OPERATING SYSTEM RECOGNISES THE SOFTWARE SUING THIS NAME
        #SO YOU WILL SEE THE NAME ENTERED HERE IN THE TASKBAR, TITLEBAR, E.T.C
        UIFunction.labelTitle(self, applicationName) #PASSING THE CODE TO SET THE TITLE TO THE CUSTOME TOPBAR IN OUR UI
        #THIS UOFunction CLASS IS IN THE FILE: ui_function.py.
        ###############################


        #-----> INITIAL STACKED WIDGET PAGE WIDGET AND TAB
        #THIS MAKE THE INITIAL WINDOW OF OUR APPLICATION, I.E. THE FIRST PAGE OR THE WELCOME PAGE/SCREEN            ---------(C5)
        #IN OUR APPLICATION THIS IS THE MENU BAR, TOODLE SWITCH, MIN, MAX, CLOSE BUTTONS, AND THE HOME PAGE.
        #ALL THIS GET INITIALISED HERE.
        #SINCE ALL THE FUNCTION RELATED STUFF IS DONE IN THE ui_function.py FILE, IT GOES THERE
        #REMEMBER THIS FUNCTION CAN ALSO BE DONE HERE, BUT DUE TO CONVINENCE IT IS SHIFTD TO A NEW FILE.
        UIFunction.initStackTab(self)
        ############################################################

        
        #----> CERTAIN TOOLS LIKE DRAG, MAXIMISE, MINIMISE, CLOSE AND HIDING OF THE WINDOWS TOPBAR
        # THIS WINDOW INITIALISES THE BUTTONS NECESSERY FOR THE MAINWINDOW LIKE: CLOSE, MIN, MAX E.T.C.                ---------(C6)
        UIFunction.constantFunction(self)
        #############################################################


        #----> TOODLE THE MENU HERE
        #THIS CODE DETETS THE BUTTON IN THE RIGHT TOP IS PRESSED OR NOT AND IF PRESSED IT CONNECT  TO A FUNCTION IN THE ui_function.py                 ---------(C7)
        #FILE, WHICH EXPANDS THE MENU BAR TO DOUBLE ITS WIDTH MAKING ROOM FOR THE ABOUT PAGES.
        #THIS EFFECT CALLED AS TOODLE, CAN BE MADE USE IN MANY WAYS. CHECK THE FUNCTION: toodleMenu: IN THE ui_function.py
        #FILE FOR THE CLEAR WORKING
        self.ui.toodle.clicked.connect(lambda: UIFunction.toodleMenu(self, 160, True))
        #############################################################


        #----> MENU BUTTON PRESSED EVENTS
        #NOW SINCE OUR DEMO APPLICATION HAS ONLY 4 MENU BUTTONS: Home, Bug, Android, Cloud, WHEN USER PRESSES IT THE FOLLOWING CODE             ---------(C8)
        #REDIRECTS IT TO THE ui_function.py FILE buttonPressed() FUNCTION TO MAKE THE NECESSERY RESPONSES TO THE BUTTON PRESSED.
        #IT TAKES SELF AND THE BUTTON NAME AS THE RGUMENT, THIS IS ONLY TO RECOGNISE WHICH BUTTON IS PRESSED BY THE buttonPressed() FUNCTION.
        self.ui.bn_home.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_home'))
        self.ui.bn_bug.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_bug'))
        self.ui.bn_android.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_android'))
        self.ui.bn_cloud.clicked.connect(lambda: UIFunction.buttonPressed(self, 'bn_cloud'))
        #############################################################


        #-----> STACK PAGE FUNCTION
        #OUR APPLICATION CHANGES THE PAGES BY USING THE STACKED WIDGET, THIS CODE POINTS TO A FUNCTION IN ui_function.py FILE             ---------(C9)
        #WHICH GOES AND SETS THE DEFAULT IN THESE PAGES AND SEARCHES FOR THE RESPONSES MADE BY THE USER IN THE CORRSPONDING PAGES.
        UIFunction.stackPage(self)
        #############################################################


        #----> EXECUTING THE ERROR AND DIALOG BOX MENU : THIS HELP TO CALL THEM WITH THE FUNCTIONS.
        #THIS CODE INITIALISED THE DIALOGBOX AND THE ERRORBOX, MAKES AN OBJECT OF THE CORRESPONDING CLASS, SO THAT WE CAN CALL THEM         ---------(C10)
        #WHENEVER NECESSERY.
        self.diag = dialogUi()
        self.error = errorUi()
        #############################################################


        #############################################################

        #UNCOMMENT THE RESPECTIVE LINES OF CODE AS REQUIRED:
        #WARNING: MAKE SURE THAT YOU COMMENT OUT CODES THAT IS ENTERED IN THIS FILE AND FILE ui_function.py FOR THE SMAE
        #WIDGET PERFORMING THE SAME FUNCTION.

#--ADDING A NEW MENU BUTTON------------------:
#REFER THE DOCUMENTATION: Documentation.pdf FILE

#--CALLING A DIALOG BOX----------------------:
        #dialogexec("Heading", "Message", "icon", "Button1name", "button2name")

#--CALLING A ERROR BOX-----------------------:
        #errorexec("Message", "icon", "buttonname")

#--PAGE HOME---------------------------------:
    #--HEADING----------------------:
        #self.ui.lab_home_main_hed.setText("heading")
        #self.ui.lab_home_stat_hed.setText("Sata heading")

    #--LABEL------------------------:
        #self.ui.lab_home_main_disc.setText("-----------")
        #self.ui.lab_home_stat_disc.setText("--------------")

#--PAGE BUG----------------------------------:
    #--CHANGING THE HEADING---------:
        #self.ui.lab_bug.setText("your heading")

    #--USING PROGRESS BAR VALUE-----:
        #self.ui.progressBar_bug.setValue(% in int)

    #--USING COMBO BOX--------------:
        #self.ui.comboBox_bug.addItem("item") #TO ADD ITEMS IN THE COMBOBOX LIST
        #self.ui.comboBox_bug.setItemText() #INDEX YOUR ADDED ITEM
        #self.ui.comboBox_bug.currentIndex() #GIVES THE CURRENT INDEX OF THE LIST

    #--USING START BUTTON-----------:
        #self.ui.bn_bug_start.clicked.connect(some function to execute) #THE FUNCTION GET ACTIVATED WHEN YOU CLICK THE BUTTON

#--PAGE CLOUD--------------------------------:
    #--CHANGE HEADING---------------:
        #self.ui.lab_cloud_main.setText("heading")

    #--CHANGING LABELS--------------:
        #self.ui.label_2.setText("change: Clint ID")
        #self.ui.label_3.setText("change: Server Adress")
        #self.ui.label_4.setText("change: Proxy")

    #--USING LINE FILED-------------:
        #self.ui.line_cloud_id.setText("set the initial text")
        #text_get = self.ui.line_cloud_id.text() #GIVES THE TEXT ENTERED BY THE USER.
        #DO THE SAME CODE OFR THE RES OF THE LINE EDIT : line_cloud_adress and line_cloud_proxy

    #--USING THE PUSH BUTTONS-------:
        #self.ui.bn_cloud_clear.clicked.connect(function to execute)
        #self.ui.bn_cloud_connect.clikced.connect(function to execute)

#--PAGE ANDROID:CONTACT----------------------:
    #--CHANGING THE HEADING---------:
        #self.ui.lab_android_contact.setText("Heading")

    #--CHANGING LABELS--------------:
        #self.ui.label.setText("-----")
        #perform the same for the label with obeject tname: 'label_5', 'label_6', 'label_7', 'label_8'

    #--USING TEXT FIELD-------------:
        #sefl.ui.line_android_name.setText("---")
        #self.ui.lineandroid_name.text() #TO GET WHAT THE USER HAS ENTERED.
        #PERFORM THE SAME CODE FOR THE: OBJECT NAME: 'line_android_adress', 'line_android_eamil', 'line_android_ph', 'line_android_org'

    #--USING PUSH BUTTONS-----------:
        #self.ui.bn_adroid_contact_edit.clicked.connect("function goes here")
        #self.ui.bn_adroid_contact_share.clicked.connect("function goes here")
        #self.ui.bn_adroid_contact_delete.clicked.connect("function goes here")
        #self.ui.bn_adroid_contact_save.clicked.connect("function goes here")

        #self.ui.bn_android_contact_save.setEnable(True) #TO ENABLE THE BUTTON
        #DO THE SAME FOR THE REST OF THE BUTTON WHEREEVER NECESSERY.

#--PAGE ANDROID:GAME-------------------------:
    #--CHANGING THE HEADING---------:
        #self.ui.lab_gamepad.setText("-----")

    #--USING TEXT BROWSER-----------:
        #self.ui.textEdit_gamepad.setText("----")

#FOR REST OF THE WIDGET GOTO THE Documentation.pdf AND CHECK THE LAYOUT FOR MORE DETAILS.


        #---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER APPNAME LABEL
        #SAME TO SAY AS IN COMMENT (C2)
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
        self.ui.frame_appname.mouseMoveEvent = moveWindow  #CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG
        
    #----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    #############################################################


    #-----> FUNCTION WHICH OPENS THE DIALOG AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION dialogexec() WITH ALL THE PARAMETER
    #NOW WHENEVER YOU WANT A DIALOG BOX TO APPEAR IN THE APP LIKE IN PRESS OF CLODE BUTTON, THIS CAN BE DONE BY CALLING THIS FUNCTION.        ----------(C11)
    #IT TAKES DIALOG OBJECT(INITIALISED EARLIER), HEADER NAME OF DIALOG BOX, MESSAGE TO BE DISPLAYED, ICON, BUTTON NAMES.
    #THIS CODE EXECUTES THE DIALOGBOX AND SO WE CAN SEE THE DIALOG BOX IN THE SCREEN.
    #DURING THE APPEARENCE OF THIS WINDOW, YOU CANNOT USE THE MAINWINDOW, YOU SHPULD EITHER PRESS ANY ONE OFT HE PROVIDED BUTTONS
    #OR JUST CLODE THE DIALOG BOX.
    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()
    #############################################################


    #-----> FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION errorexec() WITH ALL THE PARAMETER
    #SAME AS COMMEND (C11), EXCEPT THIS IS FOR THE ERROR BOX.
    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()
    ##############################################################


GLOBAL_STATE = 0 #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = True #NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
init = False # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB  
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.
class UIFunction(MainWindow):

    #----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE 
    #INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init==False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True
    ################################################################################################


    #------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)
    ################################################################################################


    #----> MAXIMISE/RESTORE FUNCTION
    #THIS FUNCTION MAXIMISES OUR MAINWINDOW WHEN THE MAXIMISE BUTTON IS PRESSED OR IF DOUBLE MOUSE LEFT PRESS IS DOEN OVER THE TOPFRMAE.
    #THIS MAKE THE APPLICATION TO OCCUPY THE WHOLE MONITOR.
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.bn_max.setToolTip("Restore") 
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/restore.png")) #CHANGE THE MAXIMISE ICON TO RESTOR ICON
            self.ui.frame_drag.hide() #HIDE DRAG AS NOT NECESSERY
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.bn_max.setToolTip("Maximize")
            self.ui.bn_max.setIcon(QtGui.QIcon("icons/1x/max.png")) #CHANGE BACK TO MAXIMISE ICON
            self.ui.frame_drag.show()
    ################################################################################################


    #----> RETURN STATUS MAX OR RESTROE
    #NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE


    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status


    #------> TOODLE MENU FUNCTION
    #THIS FUNCTION TOODLES THE MENU BAR TO DOUBLE THE LENGTH OPENING A NEW ARE OF ABOUT TAB IN FRONT.
    #ASLO IT SETS THE ABOUT>HOME AS THE FIRST PAGE.
    #IF THE PAGE IS IN THE ABOUT PAGE THEN PRESSING AGAIN WILL RESULT IN UNDOING THE PROCESS AND COMMING BACK TO THE 
    #HOME PAGE.
    def toodleMenu(self, maxWidth, clicked):

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS : I.E. MAKING THEN NORMAL COLOR THAN LIGHTER COLOR.
        for each in self.ui.frame_bottom_west.findChildren(QFrame): 
            each.setStyleSheet("background:rgb(51,51,51)")

        if clicked:
            currentWidth = self.ui.frame_bottom_west.width() #Reads the current width of the frame
            minWidth = 80 #MINIMUN WITDTH OF THE BOTTOM_WEST FRAME
            if currentWidth==80:
                extend = maxWidth
                #----> MAKE THE STACKED WIDGET PAGE TO ABOUT HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            else:
                extend = minWidth
                #-----> REVERT THE ABOUT HOME PAGE TO NORMAL HOME PAGE
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            #THIS ANIMATION IS RESPONSIBLE FOR THE TOODLE TO MOVE IN A SOME FIXED STATE.
            self.animation = QPropertyAnimation(self.ui.frame_bottom_west, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(minWidth)
            self.animation.setEndValue(extend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    ################################################################################################


    #-----> DEFAULT ACTION FUNCTION
    def constantFunction(self):
        #-----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunction.maximize_restore(self))

        #----> REMOVE NORMAL TITLE BAR 
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick
        else:
            self.ui.frame_close.hide()
            self.ui.frame_max.hide()
            self.ui.frame_min.hide()
            self.ui.frame_drag.hide()

        #-----> RESIZE USING DRAG                                       THIS CODE TO DRAG AND RESIZE IS IN PROTOPYPE.
        #self.sizegrip = QSizeGrip(self.ui.frame_drag)
        #self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        #SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        #DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        #-----> MINIMIZE BUTTON FUNCTION 
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        #-----> MAXIMIZE/RESTORE BUTTON FUNCTION
        self.ui.bn_max.clicked.connect(lambda: UIFunction.maximize_restore(self))

        #-----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.close())
    ################################################################################################################


    #----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):

        index = self.ui.stackedWidget.currentIndex()

        #------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName=='bn_home':
            if self.ui.frame_bottom_west.width()==80  and index!=0:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
                self.ui.lab_tab.setText("Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST 

            elif self.ui.frame_bottom_west.width()==160  and index!=1:  # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_home)
                self.ui.lab_tab.setText("About > Home")
                self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_bug':
            if self.ui.frame_bottom_west.width()==80 and index!=5:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
                self.ui.lab_tab.setText("Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=4:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
                self.ui.lab_tab.setText("About > Bug")
                self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_android':
            if self.ui.frame_bottom_west.width()==80  and index!=7:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
                self.ui.lab_tab.setText("Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
                UIFunction.androidStackPages(self, "page_contact")

            elif self.ui.frame_bottom_west.width()==160  and index!=3:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_android)
                self.ui.lab_tab.setText("About > Android")
                self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName=='bn_cloud':
            if self.ui.frame_bottom_west.width()==80 and index!=6:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_cloud)
                self.ui.lab_tab.setText("Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

            elif self.ui.frame_bottom_west.width()==160 and index!=2:   # ABOUT PAGE STACKED WIDGET
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_cloud)
                self.ui.lab_tab.setText("About > Cloud")
                self.ui.frame_cloud.setStyleSheet("background:rgb(91,90,90)") # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        #ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.
    ########################################################################################################################


    #----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE 
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):

        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME
        self.ui.lab_home_main_hed.setText("Profile")
        self.ui.lab_home_stat_hed.setText("Stat")

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug
        self.ui.bn_bug_start.clicked.connect(lambda: APFunction.addNumbers(self, self.ui.comboBox_bug.currentText(), True))  

        # THIS CALLS A SIMPLE FUNCTION LOOPS THROW THE NUMBER FORWARDED BY THE COMBOBOX 'comboBox_bug' AND DISPLAY IN PROGRESS BAR
        #ALONGWITH MOVING THE PROGRESS CHUNK FROM 0 TO 100%

        #########PAGE CLOUD #############
        self.ui.bn_cloud_connect.clicked.connect(lambda: APFunction.cloudConnect(self))
        #self.ui.bn_cloud_clear.clicked.connect(lambda: self.dialogexec("Warning", "Do you want to save the file", "icons/1x/errorAsset 55.png", "Cancel", "Save"))
        self.ui.bn_cloud_clear.clicked.connect(lambda: APFunction.cloudClear(self))

        #########PAGE ANDROID WIDGET AND ITS STACKANDROID WIDGET PAGES
        self.ui.bn_android_contact.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_contact"))
        self.ui.bn_android_game.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_game"))
        self.ui.bn_android_clean.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_clean"))
        self.ui.bn_android_world.clicked.connect(lambda: UIFunction.androidStackPages(self, "page_world"))
        
        ######ANDROID > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        self.ui.bn_android_contact_delete.clicked.connect(lambda: self.dialogexec("Warning", "The Contact Infromtion will be Deleted, Do you want to continue.", "icons/1x/errorAsset 55.png", "Cancel", "Yes"))

        self.ui.bn_android_contact_edit.clicked.connect(lambda: APFunction.editable(self))

        self.ui.bn_android_contact_save.clicked.connect(lambda: APFunction.saveContact(self))

        #######ANDROID > PAGE GAMEPAD >>>>>>>>>>>>>>>>>>>
        self.ui.textEdit_gamepad.setVerticalScrollBar(self.ui.vsb_gamepad)   # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText("Type Here Something, or paste something here")

        ######ANDROID > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        #NOTHING HERE
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: print("Slider: Horizondal: ", self.ui.horizontalSlider_2.value())) #CHECK WEATHER THE SLIDER IS MOVED OR NOT
        self.ui.checkBox.stateChanged.connect(lambda: self.errorexec("Happy to Know you liked the UI", "icons/1x/smile2Asset 1.png", "Ok")) #WHEN THE CHECK BOX IS CHECKED IT ECECUTES THE ERROR BOX WITH MESSAGE.
        self.ui.checkBox_2.stateChanged.connect(lambda: self.errorexec("Even More Happy to hear this", "icons/1x/smileAsset 1.png", "Ok"))

        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)
        self.ui.text_about_home.setText(aboutHome)
    ################################################################################################################################


    #-----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE. 
    def androidStackPages(self, page):
        #------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_contact)
            self.ui.lab_tab.setText("Android > Contact")
            self.ui.frame_android_contact.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_game":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_game)
            self.ui.lab_tab.setText("Android > GamePad")
            self.ui.frame_android_game.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
            self.ui.lab_tab.setText("Android > Clean")
            self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_world)
            self.ui.lab_tab.setText("Android > World")
            self.ui.frame_android_world.setStyleSheet("background:rgb(91,90,90)")

        #ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE ANDROID STACK PAGE.
    ##############################################################################################################

    
#------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS 
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
#REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE    
class APFunction():
    #-----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    def addNumbers(self, number, enable):
        if enable:
            lastProgress = 0
            for x in range(0, int(number), 1):
                progress = int((x/int(number))*100)
                if progress!=lastProgress:
                    self.ui.progressBar_bug.setValue(progress)
                    lastProgress = progress
            self.ui.progressBar_bug.setValue(100)
    ###########################

    #---> FUNCTION TO CONNECT THE CLOUD USING ADRESS AND RETURN A ERROR STATEMENT
    def cloudConnect(self):
        self.ui.bn_cloud_clear.setEnabled(False)
        textID = self.ui.line_cloud_id.text()
        textADRESS = self.ui.line_cloud_adress.text()
        if textID=='asd' and textADRESS=='1234':
            self.ui.line_cloud_adress.setText("")
            self.ui.line_cloud_id.setText("")
            self.ui.line_cloud_proxy.setText("Connection established")
        else:
            self.errorexec("Incorrect Credentials", "icons/1x/errorAsset 55.png", "Retry")

    def cloudClear(self):
        self.ui.line_cloud_proxy.setText("")
        self.ui.line_cloud_adress.setText("")
        self.ui.line_cloud_id.setText("")

    #-----> FUNCTION IN ACCOUNT OF CONTACT PAGE IN ANDROID MENU
    def editable(self):
        self.ui.line_android_name.setEnabled(True)
        self.ui.line_android_adress.setEnabled(True)
        self.ui.line_android_org.setEnabled(True)
        self.ui.line_android_email.setEnabled(True)
        self.ui.line_android_ph.setEnabled(True)

        self.ui.bn_android_contact_save.setEnabled(True)
        self.ui.bn_android_contact_edit.setEnabled(False)
        self.ui.bn_android_contact_share.setEnabled(False)
        self.ui.bn_android_contact_delete.setEnabled(False)

#-----> FUNCTION TO SAVE THE MODOFOED TEXT FIELD
    def saveContact(self):
        self.ui.line_android_name.setEnabled(False)
        self.ui.line_android_adress.setEnabled(False)
        self.ui.line_android_org.setEnabled(False)
        self.ui.line_android_email.setEnabled(False)
        self.ui.line_android_ph.setEnabled(False)

        self.ui.bn_android_contact_save.setEnabled(False)
        self.ui.bn_android_contact_edit.setEnabled(True)
        self.ui.bn_android_contact_share.setEnabled(True)
        self.ui.bn_android_contact_delete.setEnabled(True)
###############################################################################################################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#######################