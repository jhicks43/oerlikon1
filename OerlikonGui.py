import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QDoubleSpinBox, QCheckBox
from PySide6.QtGui import QIcon, QFont, QPixmap, QPalette


#thermal camera screen
class window8(QMainWindow):
    def _init_(self):
        super()._init_()

#air leak test screen
class window7(QMainWindow):
    def _init_(self):
        super()._init_()

#two fluid window screen displaying instructions to set up test
class window6(QMainWindow):
    def _init_(self):
        super()._init_()

#one fluid window screen displaying instructions to set up test
class window5(QMainWindow):
    def _init_(self):
        super()._init_()

#forth screen/flow rate paramters
class window4(QMainWindow):
    def _init_(self):
        super()._init_()

#third screen/air leak paramters
class window3(QMainWindow):
    def _init_(self):
        super()._init_()

#second screen/test screen
class window2(QMainWindow):
    def _init_(self):
        super()._init_()


#main window/intro screen
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    #defining window title
        self.setWindowTitle("OER-Heat UNCC")

    #creating the background
        self.setGeometry(100,100,600,350)
        self.container = QWidget()

        self.frameLayout = QVBoxLayout()
        self.container.setLayout(self.frameLayout)

        self.button = QPushButton(text = 'Start')
        self.frameLayout.addWidget(self.button)

        self.init_style()

    #creating the button
        self.button = QPushButton("Start", self)
        self.button.setFont(QFont("Ariel", 10))
        self.button.setGeometry(230,250,150,25)
        self.button.setStyleSheet("background-color:white;")      

    #pushing the button sends you to the fluid type window (window2)
        self.button.clicked.connect(self.window2)

    #showing window
        self.show()


#creating the logo
    def init_style(self):
        newPalette = QPalette()
        self.setPalette(newPalette)
        self.setStyleSheet("background-color: rgb(238, 29, 35);") #oerlikon red
        
    #creating oerlikon logo and resizing
        label = QLabel(self)
        pixmap = QPixmap("images/oerlikonLogo.png")
        pixmap = pixmap.scaled(300, 250, Qt.KeepAspectRatio)
        label.setGeometry(150,-125,400,500)
        label.setPixmap(pixmap)
        

#opening window2 (Test Screen)###########################################################################################################################################
    def window2(self):
        self.w2 = window2()
        self.w2.setWindowTitle("OER-Heat UNCC")

        #creating the background of window2
        self.w2.setGeometry(100,100,600,350)
        self.label2 = QLabel("Test Menu", self.w2)
        self.label2.setFont(QFont("Ariel", 15))
        self.label2.setGeometry(0, 30, 600, 50)
        self.label2.setStyleSheet("background-color: white;")
        self.label2.setAlignment(Qt.AlignCenter)

    #creating the buttons
        self.flowRateTestButton = QPushButton("Flow Rate Test", self.w2)
        self.flowRateTestButton.setFont(QFont("Ariel", 15))
        self.flowRateTestButton.setStyleSheet("background-color: white;")
        self.flowRateTestButton.setGeometry(70, 160, 200, 50)

        self.airLeakTestButton = QPushButton("Air Leak Test", self.w2)
        self.airLeakTestButton.setFont(QFont("Ariel", 15))
        self.airLeakTestButton.setStyleSheet("background-color: white;")
        self.airLeakTestButton.setGeometry(340, 160, 200, 50)

        self.thermalCameraButton = QPushButton("Thermal Camera", self.w2)
        self.thermalCameraButton.setFont(QFont("Ariel", 15))
        self.thermalCameraButton.setStyleSheet("background-color: white;")
        self.thermalCameraButton.setGeometry(200, 230, 200, 50)

#button pushes
        
    #pushing air leak test sends you to window 3 (air leak parameters)
        self.airLeakTestButton.clicked.connect(self.window3)
        self.flowRateTestButton.clicked.connect(self.window4)
        self.thermalCameraButton.clicked.connect(self.window8)

    #closing intro screen (window1)
        self.w2.show()
        self.hide()




#opening window3 (air leak parameters)###########################################################################################################################################
    def window3(self):
        self.w3 = window3()


    #creating the background of window3
        self.w3.setGeometry(100,100,600,350)
        self.w3.setWindowTitle("OER-Heat UNCC")

        self.label3 = QLabel("Air Leak Test Parameters", self.w3)
        self.label3.setFont(QFont("Ariel", 15))
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setGeometry(25, 25, 550, 50)
        self.label3.setStyleSheet("background-color: white;")

        #creating save button for parameters
        self.saveButton = QPushButton("Save", self.w3)
        self.saveButton.setFont(QFont("Ariel", 11))
        self.saveButton.setStyleSheet("background-color: lightblue;")
        self.saveButton.setGeometry(100, 320, 110, 20)
        self.saveButton.clicked.connect(self.airLeakParameters)  #saves the inputs to dictionaries

    #creating checkbox for submerge
        self.submerge = QCheckBox("Submerge", self.w3)
        self.submerge.setGeometry(100, 120, 500, 20)
        self.submerge.setFont(QFont("Ariel", 13))

    #creating input for test pressure
        self.testPressureLabel = QLabel("Test Pressure", self.w3)
        self.testPressureLabel.setFont(QFont("Ariel", 13))
        self.testPressureLabel.setGeometry(100, 170, 100, 20)

        self.tpUnitLabel = QLabel("psi", self.w3)
        self.tpUnitLabel.setFont(QFont("Ariel", 11))
        self.tpUnitLabel.setGeometry(280, 171, 60, 20)


        self.testPressure = QDoubleSpinBox(self.w3)
        self.testPressure.setMaximum(130)                   #setting maximum value of testPressure
        self.testPressure.setMinimum(0)                     #setting minimum value of testPressure
        self.testPressure.setGeometry(210, 171, 60, 20)

    #creating input for hold period
        self.holdPeriodLabelA = QLabel("Hold Period", self.w3)
        self.holdPeriodLabelA.setFont(QFont("Ariel", 13))
        self.holdPeriodLabelA.setGeometry(100, 220, 100, 20)

        self.holdPeriodA = QDoubleSpinBox(self.w3)
        self.holdPeriodA.setMaximum(900)                    #setting maximum value of holdPeriod
        self.holdPeriodA.setMinimum(0)                     #setting minimum value of holdPeriod
        self.holdPeriodA.setGeometry(210, 221, 60, 20)

        self.hpUnitLabelA = QLabel("s", self.w3)
        self.hpUnitLabelA.setFont(QFont("Ariel", 11))
        self.hpUnitLabelA.setGeometry(280, 221, 60, 20)

    #creating input for pressure drop
        self.pressureDropLabel = QLabel("Pressure Drop", self.w3)
        self.pressureDropLabel.setFont(QFont("Ariel", 13))
        self.pressureDropLabel.setGeometry(100, 270, 110, 20)

        self.pressureDrop = QDoubleSpinBox(self.w3)
        self.pressureDrop.setMaximum(300)                   #setting maximum value of pressure drop
        self.pressureDrop.setGeometry(210, 271, 60, 20)

        self.pdUnitLabel = QLabel("psi", self.w3)
        self.pdUnitLabel.setFont(QFont("Ariel", 11))
        self.pdUnitLabel.setGeometry(280, 271, 60, 20)

    #creating button to go to next page
        self.continueButton = QPushButton("Continue", self.w3)
        self.continueButton.setFont(QFont("Ariel", 11))
        self.continueButton.setStyleSheet("background-color: lightgrey;")
        self.continueButton.setGeometry(440, 320, 150, 20)
        self.continueButton.clicked.connect(self.window7)

        self.init_style()



    #opening air leak parameters and closing all other windows
        self.w3.show()
        self.w2.hide()

#saving all of the paramters into a dictionary to send to arduino
    def airLeakParameters(self):
        # Saving user input into a dictionary
        alParameters["TestParameters"] = "100"
        alParameters["submerge"] = self.submerge.isChecked()
        alParameters["testPressure"] = self.testPressure.value()
        alParameters["pressureDrop"] = self.pressureDrop.value()
        alParameters["holdPeriod"] = self.holdPeriodA.value()
        print(alParameters)




#opening window4 (flow rate parameters)###########################################################################################################################################
    def window4(self):
        self.w4 = window4()

    #creating the background of window3
        self.w4.setWindowTitle("OER-Heat UNCC")

        self.w4.setGeometry(100,100,600,350)
        self.container = QWidget()

        self.frameLayout = QVBoxLayout()
        self.container.setLayout(self.frameLayout)

        #creating save button for parameters
        self.saveButton2 = QPushButton("Save", self.w4)
        self.saveButton2.setFont(QFont("Ariel", 11))
        self.saveButton2.setStyleSheet("background-color: lightblue;")
        self.saveButton2.setGeometry(100, 320, 100, 20)
        self.saveButton2.clicked.connect(self.flowRateParameters)  #saves the inputs to dictionaries

        self.label4 = QLabel("Flow Rate Test Parameters", self.w4)
        self.label4.setFont(QFont("Ariel", 15))
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setGeometry(25, 25, 550, 50)
        self.label4.setStyleSheet("background-color: white;")

    #creating label and buttons for fluid type
        self.fluidTypeLabel = QLabel("Fluid Type", self.w4)
        self.fluidTypeLabel.setFont(QFont("Ariel", 13))
        self.fluidTypeLabel.setGeometry(100, 80, 500, 20)
 
        self.fluidOneButton = QPushButton("1", self.w4)     #1 button 
        self.fluidOneButton.setFont(QFont("Ariel", 10))
        self.fluidOneButton.setGeometry(210, 80, 30, 20)

        self.fluidTwoButton = QPushButton("2", self.w4)     #2 button 
        self.fluidTwoButton.setFont(QFont("Ariel", 10))
        self.fluidTwoButton.setGeometry(250, 80, 30, 20)

    #creating input for flush period
        flushPeriodLabel = QLabel("Flush Period", self.w4)
        flushPeriodLabel.setFont(QFont("Ariel", 13))
        flushPeriodLabel.setGeometry(100, 130, 100, 20)

        self.flushPeriod = QDoubleSpinBox(self.w4)
        self.flushPeriod.setMaximum(600)                   #setting maximum value of flushPeriod
        self.flushPeriod.setMinimum(0)                    #setting minimum value of flushPeriod
        self.flushPeriod.setGeometry(210, 131, 60, 20)

        self.fpUnitLabel = QLabel("s", self.w4)
        self.fpUnitLabel.setFont(QFont("Airel", 11))
        self.fpUnitLabel.setGeometry(280, 131, 60, 20)


    #creating input for hold period
        holdPeriodLabelF = QLabel("Hold Period", self.w4)
        holdPeriodLabelF.setFont(QFont("Ariel", 13))
        holdPeriodLabelF.setGeometry(100, 180, 100, 20)

        self.holdPeriodF = QDoubleSpinBox(self.w4)
        self.holdPeriodF.setMaximum(600)                   #setting maximum value of TestingPeriod
        self.holdPeriodF.setMinimum(0)                    #setting minimum value of TestingPeriod
        self.holdPeriodF.setGeometry(210, 181, 60, 20)

        self.hp2UnitLabel = QLabel("s", self.w4)
        self.hp2UnitLabel.setFont(QFont("Airel", 11))
        self.hp2UnitLabel.setGeometry(280, 181, 60, 20)

    #creating input for heating option
        self.heatLabel = QLabel("Heat the System", self.w4)
        self.heatLabel.setGeometry(100, 230, 150, 20)
        self.heatLabel.setFont(QFont("Ariel", 13))

        self.heatYes = QPushButton("Yes", self.w4)
        self.heatYes.setFont(QFont("Ariel", 10))        #yes button
        self.heatYes.setGeometry(230, 230, 30, 20)
        self.heatYes.clicked.connect(self.enable_temp) #connects to enable temp option

        self.heatNo = QPushButton("No", self.w4)
        self.heatNo.setFont(QFont("Ariel", 10))         #no button
        self.heatNo.setGeometry(270, 230, 30, 20)
        self.heatNo.clicked.connect(self.disable_temp) #connects to disable temp option


    #creating input for temperature
        tempLabel = QLabel("Temperature", self.w4)
        tempLabel.setFont(QFont("Ariel", 13))
        tempLabel.setGeometry(100, 280, 100, 20)

        self.tUnitLabel = QLabel("F", self.w4)
        self.tUnitLabel.setFont(QFont("Airel", 11))
        self.tUnitLabel.setGeometry(280, 281, 60, 20)

        self.temp = QDoubleSpinBox(self.w4)
        self.temp.setMaximum(150)                        #setting maximum value of temp
        self.temp.setMinimum(32)                         #setting minimum value of temp
        self.temp.setGeometry(210, 281, 60, 20)

        self.temp.setEnabled(False)         #sets the inital value to disabled

    #creating button to go to next page
        self.continueButton2 = QPushButton("Continue to Instructions", self.w4)
        self.continueButton2.setFont(QFont("Ariel", 10))
        self.continueButton2.setStyleSheet("background-color: white;")
        self.continueButton2.setGeometry(420, 320, 170, 20)

        self.w4.show()
        self.w2.hide()


#initializing 1 and 2 buttons for system
        self.button_is_checked  = False
        self.button_is_checked2 = False

        self.fluidOneButton.setCheckable(True)
        self.fluidOneButton.released.connect(self.the_button_was_released)
        self.fluidOneButton.setChecked(self.button_is_checked)

        self.fluidTwoButton.setCheckable(True)
        self.fluidTwoButton.released.connect(self.the_button_was_released2)
        self.fluidTwoButton.setChecked(self.button_is_checked2)

#initializing yes and no buttons for heat
        self.button_is_checked3  = False
        self.button_is_checked4 = False

        self.heatYes.setCheckable(True)
        self.heatYes.released.connect(self.the_button_was_released3)
        self.heatYes.setChecked(self.button_is_checked3)

        self.heatNo.setCheckable(True)
        self.heatNo.released.connect(self.the_button_was_released4)
        self.heatNo.setChecked(self.button_is_checked4)

#tracking button 1's clicks and connection to instructions page based on 1 fluid
    def the_button_was_released(self):
        self.button_is_checked = self.fluidOneButton.isChecked()

        if self.button_is_checked:
            print("True, clicked")
            self.fluidTwoButton.setChecked(False)
            self.continueButton2.clicked.connect(self.window5)
            self.sysChoice = str(0) #storing value for code to send to arduino
        else:
            print("False, not clicked")

#tracking button 2's clicks and connection to instructions page based on 2 fluid
    def the_button_was_released2(self):
        self.button_is_checked2 = self.fluidTwoButton.isChecked() 

        if self.button_is_checked2:
            print("True, clicked")
            self.fluidOneButton.setChecked(False)
            self.continueButton2.clicked.connect(self.window6)
            self.sysChoice = str(1) #storing value for code to send to arduino


#tracking yes button's clicks
    def the_button_was_released3(self):
        self.button_is_checked3 = self.heatYes.isChecked()

        if self.button_is_checked3:
            print("True, clicked")
            self.heatNo.setChecked(False)
            #self.continueButton2.clicked.connect(self.window5)
            self.heatChoice = str(0) #storing value for code to send to arduino
        else:
            print("False, not clicked")

#tracking button 2's clicks and connection to instructions page based on 2 fluid
    def the_button_was_released4(self):
        self.button_is_checked4 = self.heatNo.isChecked() 

        if self.button_is_checked4:
            print("True, clicked")
            self.heatYes.setChecked(False)
            #self.continueButton2.clicked.connect(self.window6)
            self.heatChoice = str(1) #storing value for code to send to arduino


#controlling the availability of temp through if the yes button is selected for heating option
    def enable_temp(self):
        self.temp.setEnabled(True)

    def disable_temp(self):
        self.temp.setEnabled(False)


    #saving all of the paramters into a dictionary to send to arduino
    def flowRateParameters(self):
        # Saving user input into a dictionary
        frParameters["TestParameters"] = str(0) + self.sysChoice + self.heatChoice
        frParameters["oneFluidButton"] = self.fluidOneButton.isChecked()
        frParameters["TwoFluidButton"] = self.fluidTwoButton.isChecked()
        frParameters["testPressure"] = self.flushPeriod.value()
        frParameters["holdPeriod"] = self.holdPeriodF.value()
        frParameters["heatYes"] = self.heatYes.isChecked()
        frParameters["heatNo"] = self.heatNo.isChecked()
        frParameters["temp"] = self.temp.value()

    #if the temperature is not enabled, sends the value in the dictionary as 0
        if self.temp.isEnabled():
            frParameters["temp"] = self.temp.value()
        else:
            frParameters["temp"] = 0

        print(frParameters)




#opening window 5 (one fluid screen test instructions)###########################################################################################################################################
    def window5(self):
        self.w5 = window5()

    #creating the background of window3
        self.w5.setGeometry(100,100,600,350)
        self.w5.setWindowTitle("OER-Heat UNCC")

        self.label5 = QLabel("1 Fluid Heat Exchanger", self.w5)
        self.label5.setFont(QFont("Ariel", 15))
        self.label5.setAlignment(Qt.AlignCenter)
        self.label5.setGeometry(100, 100, 400, 50)
        self.label5.setStyleSheet("background-color: lightgrey;")

        # Create the button
        self.nextButton2 = QPushButton('Next', self.w5)
        self.nextButton2.setGeometry(250, 310, 100, 30)

        self.nextButton2.clicked.connect(self.on_button_click2)
        
        # Create the label
        self.label9 = QLabel('Instructions', self.w5)
        self.label9.setStyleSheet("background-color:lightgrey;")  
        self.label9.setAlignment(Qt.AlignCenter)
        self.label9.setGeometry(50, 50, 500, 250)
        self.label9.setWordWrap(True)                       #fits text to screen

        self.label10 = QLabel("One Fluid Flow Rate Test", self.w5)
        self.label10.setStyleSheet("background-color:white;")
        self.label10.setAlignment(Qt.AlignCenter)
        self.label10.setGeometry(50, 10, 500, 30)
        self.label10.setFont(QFont("Ariel", 13))

        self.init_style()
        
        # List of messages
        self.messages2 = [
            "Hello",
            "Second message.",
            "Third message.",
            "Fourth message.",
            "You've seen all messages. Starting over."
        ]
        
        # Counter for button clicks
        self.counter2 = 0

        #creating button back to tests page
        self.mainPage4 = QPushButton("Main", self.w5)
        self.mainPage4.setFont(QFont("Ariel", 11))
        self.mainPage4.setStyleSheet("background-color: lightblue;")
        self.mainPage4.setGeometry(500, 320, 80, 20)

        #pressing button takes you back to tests page
        self.mainPage4.clicked.connect(self.window2)

        # pressing button connects you to clear the flow rate dictionary
        self.mainPage4.clicked.connect(self.clear_dictionary)

        #pressing button closes window
        self.mainPage4.clicked.connect(self.close_window4)

        #showing window and closing air leak parameters window
        self.w5.show()
        self.w4.hide()
        
    def on_button_click2(self):
        self.label9.setText(self.messages2[self.counter2])
        
        # Update counter
        self.counter2 = (self.counter2 + 1) % len(self.messages2)

        #function to clear flow rate dictionary
    def clear_dictionary(self):
        frParameters.clear()
        print("Dictionary cleared")

    def close_window4(self):
        self.w5.close()



#opening window6 (two fluid screen test instructions)###########################################################################################################################################
    def window6(self):
        self.w6 = window6()

    #creating the background of window3
        self.w6.setGeometry(100,100,600,350)
        self.w6.setWindowTitle("OER-Heat UNCC")

        self.label6 = QLabel("2 Fluid Heat Exchanger", self.w6)
        self.label6.setFont(QFont("Ariel", 15))
        self.label6.setAlignment(Qt.AlignCenter)
        self.label6.setGeometry(100, 100, 400, 50)
        self.label6.setStyleSheet("background-color: lightgrey;")

        self.label11 = QLabel("1 Fluid Heat Exchanger", self.w6)
        self.label11.setFont(QFont("Ariel", 15))
        self.label11.setAlignment(Qt.AlignCenter)
        self.label11.setGeometry(100, 100, 400, 50)
        self.label11.setStyleSheet("background-color: lightgrey;")

        # Create the button
        self.nextButton3 = QPushButton('Next', self.w6)
        self.nextButton3.setGeometry(250, 310, 100, 30)

        self.nextButton3.clicked.connect(self.on_button_click3)
        
        # Create the label
        self.label12 = QLabel('Instructions', self.w6)
        self.label12.setStyleSheet("background-color:lightgrey;")  
        self.label12.setAlignment(Qt.AlignCenter)
        self.label12.setGeometry(50, 50, 500, 250)
        self.label12.setWordWrap(True)                       #fits text to screen

        self.label13 = QLabel("Two Fluid Flow Rate Test", self.w6)
        self.label13.setStyleSheet("background-color:white;")
        self.label13.setAlignment(Qt.AlignCenter)
        self.label13.setGeometry(50, 10, 500, 30)
        self.label13.setFont(QFont("Ariel", 13))

        self.init_style()
        
        # List of messages
        self.messages3 = [
            "Hello",
            "Second message.",
            "Third message.",
            "Fourth message.",
            "You've seen all messages. Starting over."
        ]
        
        # Counter for button clicks
        self.counter3 = 0

        #creating button back to tests page
        self.mainPage3 = QPushButton("Main", self.w6)
        self.mainPage3.setFont(QFont("Ariel", 11))
        self.mainPage3.setStyleSheet("background-color: lightblue;")
        self.mainPage3.setGeometry(500, 320, 80, 20)

        #pressing button takes you back to tests page
        self.mainPage3.clicked.connect(self.window2)

        #pressing button connects you to clear the flow rate dictionary
        self.mainPage3.clicked.connect(self.clear_dictionary2)

        #pressing button closes window
        self.mainPage3.clicked.connect(self.close_window)

        #showing window and closing others
        self.w6.show()
        self.w4.hide()
        self.w5.hide()
        
    def on_button_click3(self):
        self.label12.setText(self.messages3[self.counter3])
        
        # Update counter
        self.counter3 = (self.counter3 + 1) % len(self.messages3)

    #function to clear flow rate dictionary
    def clear_dictionary2(self):
        frParameters.clear()
        print("Dictionary cleared")

    def close_window(self):
        self.w6.close()

    



#opening window7 (air leak test)###########################################################################################################################################
    def window7(self):
        self.w7 = window7()


    #defining window title
        self.w7.setWindowTitle("OER-Heat UNCC")

    #creating the background
        self.w7.setGeometry(100,100,600,350)


        # Create the button
        self.nextButton = QPushButton('Next', self.w7)
        self.nextButton.setGeometry(250, 310, 100, 30)

        self.nextButton.clicked.connect(self.on_button_click)
        
        # Create the label
        self.label7 = QLabel('Instructions', self.w7)
        self.label7.setStyleSheet("background-color:lightgrey;")  
        self.label7.setAlignment(Qt.AlignCenter)
        self.label7.setGeometry(50, 50, 500, 250)
        self.label7.setWordWrap(True)                       #fits text to screen

        self.label8 = QLabel("Air Leak Test", self.w7)
        self.label8.setStyleSheet("background-color:white;")
        self.label8.setAlignment(Qt.AlignCenter)
        self.label8.setGeometry(50, 10, 500, 30)
        self.label8.setFont(QFont("Ariel", 13))

        self.init_style()
        
        # List of messages
        self.messages = [
            "Hello",
            "Second message.",
            "Third message.",
            "Fourth message.",
            "You've seen all messages. Starting over."
        ]
        
        # Counter for button clicks
        self.counter = 0

        #creating button back to tests page
        self.mainPage2 = QPushButton("Main", self.w7)
        self.mainPage2.setFont(QFont("Ariel", 11))
        self.mainPage2.setStyleSheet("background-color: lightblue;")
        self.mainPage2.setGeometry(500, 320, 80, 20)

        #pressing button takes you back to tests page
        self.mainPage2.clicked.connect(self.window2)

        # pressing button connects you to clear the air leak dictionary
        self.mainPage2.clicked.connect(self.clear_dictionary3)

        #pressing button closes window
        self.mainPage2.clicked.connect(self.close_window2)

        #showing window and closing air leak parameters window
        self.w7.show()
        self.w3.hide()
        
    def on_button_click(self):
        self.label7.setText(self.messages[self.counter])
        
        # Update counter
        self.counter = (self.counter + 1) % len(self.messages)

    #function to clear air leak dictionary
    def clear_dictionary3(self):
        alParameters.clear()
        print("Dictionary cleared")

    def close_window2(self):
        self.w7.close()


#opening window8 (thermal camera page)###########################################################################################################################################
    def window8(self):
        self.w8 = window8()


    #creating the background of window3
        self.w8.setGeometry(100,100,600,350)
        self.w8.setWindowTitle("OER-Heat UNCC")

        self.label14 = QLabel("Thermal Camera", self.w8)
        self.label14.setFont(QFont("Ariel", 15))
        self.label14.setAlignment(Qt.AlignCenter)
        self.label14.setGeometry(25, 25, 550, 50)
        self.label14.setStyleSheet("background-color: white;")

        #creating button back to test menu
        self.mainPage = QPushButton("Main", self.w8)
        self.mainPage.setFont(QFont("Ariel", 11))
        self.mainPage.setStyleSheet("background-color: lightblue;")
        self.mainPage.setGeometry(500, 320, 80, 20)

        #pressing button takes you back to test menu
        self.mainPage.clicked.connect(self.window2)

        #pressing button closes window
        self.mainPage.clicked.connect(self.close_window3)

        #showing window and test screen menu
        self.w8.show()
        self.w2.hide()

        #pressing button closes window
    def close_window3(self):
        self.w8.close()






# Empty dictionary to store the user input for the air leak test parameters
alParameters = {}

# Empty dictionary to store the user input for the flow rate test parameters
frParameters = {}

app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec_()

