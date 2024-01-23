# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design\cooker.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.windowBar = QtWidgets.QWidget(self.verticalWidget)
        self.windowBar.setStyleSheet("")
        self.windowBar.setObjectName("windowBar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.windowBar)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.windowBarLabelWidget = QtWidgets.QWidget(self.windowBar)
        self.windowBarLabelWidget.setObjectName("windowBarLabelWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.windowBarLabelWidget)
        self.horizontalLayout_3.setContentsMargins(3, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.windowBarLabel = QtWidgets.QLabel(self.windowBarLabelWidget)
        self.windowBarLabel.setObjectName("windowBarLabel")
        self.horizontalLayout_3.addWidget(self.windowBarLabel)
        self.horizontalLayout_2.addWidget(self.windowBarLabelWidget)
        self.widget = QtWidgets.QWidget(self.windowBar)
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(347, 2, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.widget)
        self.windowBarButtons = QtWidgets.QWidget(self.windowBar)
        self.windowBarButtons.setObjectName("windowBarButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.windowBarButtons)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minimizeButton = QtWidgets.QPushButton(self.windowBarButtons)
        self.minimizeButton.setMaximumSize(QtCore.QSize(32, 24))
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(self.windowBarButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMaximumSize(QtCore.QSize(32, 24))
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.windowBarButtons)
        self.verticalLayout.addWidget(self.windowBar, 0, QtCore.Qt.AlignTop)
        self.mainSettings_2 = QtWidgets.QWidget(self.verticalWidget)
        self.mainSettings_2.setObjectName("mainSettings_2")
        self.mainSettings = QtWidgets.QHBoxLayout(self.mainSettings_2)
        self.mainSettings.setContentsMargins(2, 1, 2, 1)
        self.mainSettings.setSpacing(4)
        self.mainSettings.setObjectName("mainSettings")
        self.serverAndCooker = QtWidgets.QVBoxLayout()
        self.serverAndCooker.setContentsMargins(-1, -1, 0, -1)
        self.serverAndCooker.setObjectName("serverAndCooker")
        self.cookerSettingsGroupBox = QtWidgets.QGroupBox(self.mainSettings_2)
        self.cookerSettingsGroupBox.setObjectName("cookerSettingsGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cookerSettingsGroupBox)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cookTimeFrame = QtWidgets.QFrame(self.cookerSettingsGroupBox)
        self.cookTimeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cookTimeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cookTimeFrame.setObjectName("cookTimeFrame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.cookTimeFrame)
        self.verticalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cookTimeLabelLayout = QtWidgets.QHBoxLayout()
        self.cookTimeLabelLayout.setContentsMargins(-1, 0, -1, -1)
        self.cookTimeLabelLayout.setSpacing(0)
        self.cookTimeLabelLayout.setObjectName("cookTimeLabelLayout")
        self.intervalTextLabel_2 = QtWidgets.QLabel(self.cookTimeFrame)
        self.intervalTextLabel_2.setObjectName("intervalTextLabel_2")
        self.cookTimeLabelLayout.addWidget(self.intervalTextLabel_2)
        self.cookTimeLabelTime = QtWidgets.QLabel(self.cookTimeFrame)
        self.cookTimeLabelTime.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.cookTimeLabelTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cookTimeLabelTime.setObjectName("cookTimeLabelTime")
        self.cookTimeLabelLayout.addWidget(self.cookTimeLabelTime)
        self.verticalLayout_8.addLayout(self.cookTimeLabelLayout)
        self.cookTimeSlider = QtWidgets.QSlider(self.cookTimeFrame)
        self.cookTimeSlider.setToolTip("")
        self.cookTimeSlider.setToolTipDuration(-1)
        self.cookTimeSlider.setMinimum(1)
        self.cookTimeSlider.setMaximum(24000)
        self.cookTimeSlider.setProperty("value", 600)
        self.cookTimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cookTimeSlider.setInvertedAppearance(False)
        self.cookTimeSlider.setObjectName("cookTimeSlider")
        self.verticalLayout_8.addWidget(self.cookTimeSlider)
        self.verticalLayout_2.addWidget(self.cookTimeFrame)
        self.checkBox = QtWidgets.QCheckBox(self.cookerSettingsGroupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.rejoinServerBox = QtWidgets.QCheckBox(self.cookerSettingsGroupBox)
        self.rejoinServerBox.setChecked(True)
        self.rejoinServerBox.setObjectName("rejoinServerBox")
        self.verticalLayout_2.addWidget(self.rejoinServerBox)
        self.cookerRejoin = QtWidgets.QFrame(self.cookerSettingsGroupBox)
        self.cookerRejoin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cookerRejoin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cookerRejoin.setObjectName("cookerRejoin")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.cookerRejoin)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.cookerRejoin)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.rejoinLimit = QtWidgets.QSpinBox(self.cookerRejoin)
        self.rejoinLimit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.rejoinLimit.setMinimum(0)
        self.rejoinLimit.setMaximum(100)
        self.rejoinLimit.setProperty("value", 0)
        self.rejoinLimit.setObjectName("rejoinLimit")
        self.horizontalLayout_4.addWidget(self.rejoinLimit)
        self.verticalLayout_2.addWidget(self.cookerRejoin)
        self.serverAndCooker.addWidget(self.cookerSettingsGroupBox)
        self.serverSettingsGroupBox = QtWidgets.QGroupBox(self.mainSettings_2)
        self.serverSettingsGroupBox.setObjectName("serverSettingsGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.serverSettingsGroupBox)
        self.verticalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.serverIP = QtWidgets.QLineEdit(self.serverSettingsGroupBox)
        self.serverIP.setText("")
        self.serverIP.setObjectName("serverIP")
        self.verticalLayout_4.addWidget(self.serverIP)
        self.serverPort = QtWidgets.QLineEdit(self.serverSettingsGroupBox)
        self.serverPort.setText("")
        self.serverPort.setMaxLength(5)
        self.serverPort.setObjectName("serverPort")
        self.verticalLayout_4.addWidget(self.serverPort)
        self.serverPassword = QtWidgets.QLineEdit(self.serverSettingsGroupBox)
        self.serverPassword.setText("")
        self.serverPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.serverPassword.setObjectName("serverPassword")
        self.verticalLayout_4.addWidget(self.serverPassword)
        self.joinServerButton = QtWidgets.QPushButton(self.serverSettingsGroupBox)
        self.joinServerButton.setCheckable(True)
        self.joinServerButton.setObjectName("joinServerButton")
        self.verticalLayout_4.addWidget(self.joinServerButton)
        self.groupBox = QtWidgets.QGroupBox(self.serverSettingsGroupBox)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.serverComboBox = QtWidgets.QComboBox(self.groupBox)
        self.serverComboBox.setEditable(False)
        self.serverComboBox.setCurrentText("")
        self.serverComboBox.setFrame(True)
        self.serverComboBox.setObjectName("serverComboBox")
        self.verticalLayout_9.addWidget(self.serverComboBox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.saveServerButton = QtWidgets.QPushButton(self.groupBox)
        self.saveServerButton.setObjectName("saveServerButton")
        self.horizontalLayout_7.addWidget(self.saveServerButton)
        self.updateServerButton = QtWidgets.QPushButton(self.groupBox)
        self.updateServerButton.setObjectName("updateServerButton")
        self.horizontalLayout_7.addWidget(self.updateServerButton)
        self.deleteServerButton = QtWidgets.QPushButton(self.groupBox)
        self.deleteServerButton.setObjectName("deleteServerButton")
        self.horizontalLayout_7.addWidget(self.deleteServerButton)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.serverAndCooker.addWidget(self.serverSettingsGroupBox)
        self.mainSettings.addLayout(self.serverAndCooker)
        self.webhookSettingsGroupBox = QtWidgets.QGroupBox(self.mainSettings_2)
        self.webhookSettingsGroupBox.setObjectName("webhookSettingsGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.webhookSettingsGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.webhookEnabledCheckBox = QtWidgets.QCheckBox(self.webhookSettingsGroupBox)
        self.webhookEnabledCheckBox.setObjectName("webhookEnabledCheckBox")
        self.verticalLayout_5.addWidget(self.webhookEnabledCheckBox)
        self.webhookUrlTextBox = QtWidgets.QLineEdit(self.webhookSettingsGroupBox)
        self.webhookUrlTextBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.webhookUrlTextBox.setClearButtonEnabled(False)
        self.webhookUrlTextBox.setObjectName("webhookUrlTextBox")
        self.verticalLayout_5.addWidget(self.webhookUrlTextBox)
        self.testWebhookButton = QtWidgets.QPushButton(self.webhookSettingsGroupBox)
        self.testWebhookButton.setObjectName("testWebhookButton")
        self.verticalLayout_5.addWidget(self.testWebhookButton)
        self.label_2 = QtWidgets.QLabel(self.webhookSettingsGroupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.listView = QtWidgets.QListView(self.webhookSettingsGroupBox)
        self.listView.setModelColumn(0)
        self.listView.setObjectName("listView")
        self.verticalLayout_5.addWidget(self.listView)
        self.webhookCriteria = QtWidgets.QGroupBox(self.webhookSettingsGroupBox)
        self.webhookCriteria.setObjectName("webhookCriteria")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.webhookCriteria)
        self.verticalLayout_6.setContentsMargins(2, -1, 2, 9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.webhookPostDisconnectCheckBox = QtWidgets.QCheckBox(self.webhookCriteria)
        self.webhookPostDisconnectCheckBox.setObjectName("webhookPostDisconnectCheckBox")
        self.verticalLayout_6.addWidget(self.webhookPostDisconnectCheckBox)
        self.webhookPostPlayerDeathsCheckBox = QtWidgets.QCheckBox(self.webhookCriteria)
        self.webhookPostPlayerDeathsCheckBox.setObjectName("webhookPostPlayerDeathsCheckBox")
        self.verticalLayout_6.addWidget(self.webhookPostPlayerDeathsCheckBox)
        self.webhookPostPlayerRejoinCheckBox = QtWidgets.QCheckBox(self.webhookCriteria)
        self.webhookPostPlayerRejoinCheckBox.setObjectName("webhookPostPlayerRejoinCheckBox")
        self.verticalLayout_6.addWidget(self.webhookPostPlayerRejoinCheckBox)
        self.line = QtWidgets.QFrame(self.webhookCriteria)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.webhookPostPeriodicCheckBox = QtWidgets.QCheckBox(self.webhookCriteria)
        self.webhookPostPeriodicCheckBox.setObjectName("webhookPostPeriodicCheckBox")
        self.verticalLayout_6.addWidget(self.webhookPostPeriodicCheckBox)
        self.periodicTimeIntervalFrame = QtWidgets.QFrame(self.webhookCriteria)
        self.periodicTimeIntervalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.periodicTimeIntervalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.periodicTimeIntervalFrame.setObjectName("periodicTimeIntervalFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.periodicTimeIntervalFrame)
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.timeLabel = QtWidgets.QHBoxLayout()
        self.timeLabel.setContentsMargins(-1, 0, -1, -1)
        self.timeLabel.setSpacing(0)
        self.timeLabel.setObjectName("timeLabel")
        self.intervalTextLabel = QtWidgets.QLabel(self.periodicTimeIntervalFrame)
        self.intervalTextLabel.setObjectName("intervalTextLabel")
        self.timeLabel.addWidget(self.intervalTextLabel)
        self.webhookPeriodicIntervalLabel = QtWidgets.QLabel(self.periodicTimeIntervalFrame)
        self.webhookPeriodicIntervalLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.webhookPeriodicIntervalLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.webhookPeriodicIntervalLabel.setObjectName("webhookPeriodicIntervalLabel")
        self.timeLabel.addWidget(self.webhookPeriodicIntervalLabel)
        self.verticalLayout_7.addLayout(self.timeLabel)
        self.webhookPeriodicIntervalSlider = QtWidgets.QSlider(self.periodicTimeIntervalFrame)
        self.webhookPeriodicIntervalSlider.setToolTipDuration(-1)
        self.webhookPeriodicIntervalSlider.setMinimum(1)
        self.webhookPeriodicIntervalSlider.setMaximum(3000)
        self.webhookPeriodicIntervalSlider.setProperty("value", 60)
        self.webhookPeriodicIntervalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.webhookPeriodicIntervalSlider.setInvertedAppearance(False)
        self.webhookPeriodicIntervalSlider.setObjectName("webhookPeriodicIntervalSlider")
        self.verticalLayout_7.addWidget(self.webhookPeriodicIntervalSlider)
        self.verticalLayout_6.addWidget(self.periodicTimeIntervalFrame, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.webhookCriteria)
        self.mainSettings.addWidget(self.webhookSettingsGroupBox)
        self.verticalLayout.addWidget(self.mainSettings_2)
        self.mainButtons = QtWidgets.QWidget(self.verticalWidget)
        self.mainButtons.setObjectName("mainButtons")
        self.buttons = QtWidgets.QHBoxLayout(self.mainButtons)
        self.buttons.setContentsMargins(2, 1, 2, 1)
        self.buttons.setSpacing(6)
        self.buttons.setObjectName("buttons")
        self.startCooker = QtWidgets.QPushButton(self.mainButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startCooker.sizePolicy().hasHeightForWidth())
        self.startCooker.setSizePolicy(sizePolicy)
        self.startCooker.setCheckable(False)
        self.startCooker.setObjectName("startCooker")
        self.buttons.addWidget(self.startCooker)
        self.startGame = QtWidgets.QPushButton(self.mainButtons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startGame.sizePolicy().hasHeightForWidth())
        self.startGame.setSizePolicy(sizePolicy)
        self.startGame.setCheckable(True)
        self.startGame.setObjectName("startGame")
        self.buttons.addWidget(self.startGame)
        self.verticalLayout.addWidget(self.mainButtons)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_5.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cookTimeSlider, self.rejoinServerBox)
        MainWindow.setTabOrder(self.rejoinServerBox, self.rejoinLimit)
        MainWindow.setTabOrder(self.rejoinLimit, self.serverIP)
        MainWindow.setTabOrder(self.serverIP, self.serverPort)
        MainWindow.setTabOrder(self.serverPort, self.serverPassword)
        MainWindow.setTabOrder(self.serverPassword, self.webhookEnabledCheckBox)
        MainWindow.setTabOrder(self.webhookEnabledCheckBox, self.webhookUrlTextBox)
        MainWindow.setTabOrder(self.webhookUrlTextBox, self.webhookPostDisconnectCheckBox)
        MainWindow.setTabOrder(self.webhookPostDisconnectCheckBox, self.webhookPostPeriodicCheckBox)
        MainWindow.setTabOrder(self.webhookPostPeriodicCheckBox, self.webhookPeriodicIntervalSlider)
        MainWindow.setTabOrder(self.webhookPeriodicIntervalSlider, self.startCooker)
        MainWindow.setTabOrder(self.startCooker, self.startGame)
        MainWindow.setTabOrder(self.startGame, self.minimizeButton)
        MainWindow.setTabOrder(self.minimizeButton, self.closeButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.windowBarLabel.setText(_translate("MainWindow", "Smuggler Suite Cooker v1.0"))
        self.minimizeButton.setText(_translate("MainWindow", "_"))
        self.closeButton.setText(_translate("MainWindow", "X"))
        self.cookerSettingsGroupBox.setTitle(_translate("MainWindow", "Cooker Settings"))
        self.cookTimeFrame.setToolTip(_translate("MainWindow", "Time to cook for"))
        self.intervalTextLabel_2.setText(_translate("MainWindow", "Cook Time:"))
        self.cookTimeLabelTime.setText(_translate("MainWindow", "10m"))
        self.checkBox.setToolTip(_translate("MainWindow", "Respawn when the player dies"))
        self.checkBox.setText(_translate("MainWindow", "Respawn On Death"))
        self.rejoinServerBox.setToolTip(_translate("MainWindow", "Automatically rejoin the server upon being kicked (will not if banned)"))
        self.rejoinServerBox.setText(_translate("MainWindow", "Rejoin Server"))
        self.cookerRejoin.setToolTip(_translate("MainWindow", "Limit how many times to rejoin the server (0 = infinite)"))
        self.label_3.setText(_translate("MainWindow", "Rejoin Limit:"))
        self.rejoinLimit.setSpecialValueText(_translate("MainWindow", "0"))
        self.serverSettingsGroupBox.setTitle(_translate("MainWindow", "Server Settings"))
        self.serverIP.setToolTip(_translate("MainWindow", "IP/Address of the server (e.g server10.phn.pw)"))
        self.serverIP.setPlaceholderText(_translate("MainWindow", "ip/address"))
        self.serverPort.setToolTip(_translate("MainWindow", "Port of the server (usually 27015)"))
        self.serverPort.setPlaceholderText(_translate("MainWindow", "port"))
        self.serverPassword.setPlaceholderText(_translate("MainWindow", "password (optional)"))
        self.joinServerButton.setText(_translate("MainWindow", "Join Server"))
        self.groupBox.setToolTip(_translate("MainWindow", "Save server connection details for easy access"))
        self.groupBox.setTitle(_translate("MainWindow", "Saved Servers:"))
        self.label.setText(_translate("MainWindow", "Server Name:"))
        self.serverComboBox.setToolTip(_translate("MainWindow", "Select a server"))
        self.serverComboBox.setPlaceholderText(_translate("MainWindow", "name"))
        self.saveServerButton.setToolTip(_translate("MainWindow", "Save current server details as a new server"))
        self.saveServerButton.setText(_translate("MainWindow", "Save New"))
        self.updateServerButton.setToolTip(_translate("MainWindow", "Update selected server"))
        self.updateServerButton.setText(_translate("MainWindow", "Update"))
        self.deleteServerButton.setToolTip(_translate("MainWindow", "Delete selected server"))
        self.deleteServerButton.setText(_translate("MainWindow", "Delete"))
        self.webhookSettingsGroupBox.setTitle(_translate("MainWindow", "Webhook Settings"))
        self.webhookEnabledCheckBox.setToolTip(_translate("MainWindow", "Enable webhook functionality"))
        self.webhookEnabledCheckBox.setText(_translate("MainWindow", "Enabled"))
        self.webhookUrlTextBox.setToolTip(_translate("MainWindow", "Discord webhook url"))
        self.webhookUrlTextBox.setPlaceholderText(_translate("MainWindow", "discord webhook url"))
        self.testWebhookButton.setToolTip(_translate("MainWindow", "Test Discord webhook"))
        self.testWebhookButton.setText(_translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "Warning/Ban Ping List"))
        self.webhookCriteria.setToolTip(_translate("MainWindow", "Specify when to send webhook updates"))
        self.webhookCriteria.setTitle(_translate("MainWindow", "Webhook Criteria"))
        self.webhookPostDisconnectCheckBox.setToolTip(_translate("MainWindow", "Send webhook whenever the player leaves the server"))
        self.webhookPostDisconnectCheckBox.setText(_translate("MainWindow", "Player Disconnects"))
        self.webhookPostPlayerDeathsCheckBox.setToolTip(_translate("MainWindow", "Send webhook whenever the player dies"))
        self.webhookPostPlayerDeathsCheckBox.setText(_translate("MainWindow", "Player Deaths"))
        self.webhookPostPlayerRejoinCheckBox.setToolTip(_translate("MainWindow", "Send webhook whenever the player rejoins the server after being disconnected"))
        self.webhookPostPlayerRejoinCheckBox.setText(_translate("MainWindow", "Player Rejoins"))
        self.webhookPostPeriodicCheckBox.setToolTip(_translate("MainWindow", "Periodically send status update webhooks (time elapsed, etc)"))
        self.webhookPostPeriodicCheckBox.setText(_translate("MainWindow", "Periodic Status Update"))
        self.periodicTimeIntervalFrame.setToolTip(_translate("MainWindow", "How often to send status updates"))
        self.intervalTextLabel.setText(_translate("MainWindow", "Status Interval:"))
        self.webhookPeriodicIntervalLabel.setText(_translate("MainWindow", "1m"))
        self.webhookPeriodicIntervalSlider.setToolTip(_translate("MainWindow", "test"))
        self.startCooker.setToolTip(_translate("MainWindow", "Start cooker (Unturned needs to be open)"))
        self.startCooker.setText(_translate("MainWindow", "Start Cooker"))
        self.startGame.setToolTip(_translate("MainWindow", "Launch/Kill Unturned"))
        self.startGame.setText(_translate("MainWindow", "Launch Unturned"))
import resource_rc