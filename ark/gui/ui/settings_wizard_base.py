# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ark/gui/ui/settings_wizard_base.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SettingsWizard(object):
    def setupUi(self, SettingsWizard):
        SettingsWizard.setObjectName(_fromUtf8("SettingsWizard"))
        SettingsWizard.resize(704, 436)
        SettingsWizard.setOptions(QtGui.QWizard.CancelButtonOnLeft|QtGui.QWizard.NoBackButtonOnLastPage|QtGui.QWizard.NoBackButtonOnStartPage|QtGui.QWizard.NoDefaultButton)
        self.WelcomePage = QtGui.QWizardPage()
        self.WelcomePage.setObjectName(_fromUtf8("WelcomePage"))
        self.gridLayout = QtGui.QGridLayout(self.WelcomePage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        SettingsWizard.addPage(self.WelcomePage)
        self.folderPage = FolderPage()
        self.folderPage.setObjectName(_fromUtf8("folderPage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.folderPage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.folderLabel = QtGui.QLabel(self.folderPage)
        self.folderLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.folderLabel.setWordWrap(True)
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.gridLayout_2.addWidget(self.folderLabel, 0, 0, 1, 1)
        self.projectFolderLayout = QtGui.QHBoxLayout()
        self.projectFolderLayout.setObjectName(_fromUtf8("projectFolderLayout"))
        self.projectFolderEdit = QtGui.QLineEdit(self.folderPage)
        self.projectFolderEdit.setObjectName(_fromUtf8("projectFolderEdit"))
        self.projectFolderLayout.addWidget(self.projectFolderEdit)
        self.projectFolderButton = QtGui.QToolButton(self.folderPage)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/ark/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.projectFolderButton.setIcon(icon)
        self.projectFolderButton.setObjectName(_fromUtf8("projectFolderButton"))
        self.projectFolderLayout.addWidget(self.projectFolderButton)
        self.gridLayout_2.addLayout(self.projectFolderLayout, 1, 0, 1, 1)
        SettingsWizard.addPage(self.folderPage)
        self.projectPage = ProjectPage()
        self.projectPage.setObjectName(_fromUtf8("projectPage"))
        self.gridLayout_3 = QtGui.QGridLayout(self.projectPage)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.projectCodeLabel = QtGui.QLabel(self.projectPage)
        self.projectCodeLabel.setObjectName(_fromUtf8("projectCodeLabel"))
        self.gridLayout_3.addWidget(self.projectCodeLabel, 0, 0, 1, 1)
        self.projectNameLabel = QtGui.QLabel(self.projectPage)
        self.projectNameLabel.setObjectName(_fromUtf8("projectNameLabel"))
        self.gridLayout_3.addWidget(self.projectNameLabel, 2, 0, 1, 1)
        self.projectCodeEdit = QtGui.QLineEdit(self.projectPage)
        self.projectCodeEdit.setObjectName(_fromUtf8("projectCodeEdit"))
        self.gridLayout_3.addWidget(self.projectCodeEdit, 0, 1, 1, 1)
        self.projectNameEdit = QtGui.QLineEdit(self.projectPage)
        self.projectNameEdit.setObjectName(_fromUtf8("projectNameEdit"))
        self.gridLayout_3.addWidget(self.projectNameEdit, 2, 1, 1, 1)
        self.arkUrlLabel = QtGui.QLabel(self.projectPage)
        self.arkUrlLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.arkUrlLabel.setWordWrap(True)
        self.arkUrlLabel.setObjectName(_fromUtf8("arkUrlLabel"))
        self.gridLayout_3.addWidget(self.arkUrlLabel, 7, 0, 1, 1)
        self.arkUrlEdit = QtGui.QLineEdit(self.projectPage)
        self.arkUrlEdit.setEnabled(True)
        self.arkUrlEdit.setObjectName(_fromUtf8("arkUrlEdit"))
        self.gridLayout_3.addWidget(self.arkUrlEdit, 7, 1, 1, 1)
        self.siteCodesLabel = QtGui.QLabel(self.projectPage)
        self.siteCodesLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.siteCodesLabel.setWordWrap(True)
        self.siteCodesLabel.setObjectName(_fromUtf8("siteCodesLabel"))
        self.gridLayout_3.addWidget(self.siteCodesLabel, 6, 0, 1, 1)
        self.siteCodesEdit = QtGui.QLineEdit(self.projectPage)
        self.siteCodesEdit.setObjectName(_fromUtf8("siteCodesEdit"))
        self.gridLayout_3.addWidget(self.siteCodesEdit, 6, 1, 1, 1)
        self.label = QtGui.QLabel(self.projectPage)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 8, 1, 1, 1)
        SettingsWizard.addPage(self.projectPage)
        self.userPage = UserPage()
        self.userPage.setObjectName(_fromUtf8("userPage"))
        self.gridLayout_5 = QtGui.QGridLayout(self.userPage)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.arkUserIdLabel = QtGui.QLabel(self.userPage)
        self.arkUserIdLabel.setObjectName(_fromUtf8("arkUserIdLabel"))
        self.gridLayout_5.addWidget(self.arkUserIdLabel, 8, 0, 1, 1)
        self.userFullnameLabel = QtGui.QLabel(self.userPage)
        self.userFullnameLabel.setObjectName(_fromUtf8("userFullnameLabel"))
        self.gridLayout_5.addWidget(self.userFullnameLabel, 1, 0, 1, 1)
        self.userInitialsLabel = QtGui.QLabel(self.userPage)
        self.userInitialsLabel.setObjectName(_fromUtf8("userInitialsLabel"))
        self.gridLayout_5.addWidget(self.userInitialsLabel, 5, 0, 1, 1)
        self.userFullnameEdit = QtGui.QLineEdit(self.userPage)
        self.userFullnameEdit.setObjectName(_fromUtf8("userFullnameEdit"))
        self.gridLayout_5.addWidget(self.userFullnameEdit, 1, 1, 1, 1)
        self.userInitialsEdit = QtGui.QLineEdit(self.userPage)
        self.userInitialsEdit.setObjectName(_fromUtf8("userInitialsEdit"))
        self.gridLayout_5.addWidget(self.userInitialsEdit, 5, 1, 1, 1)
        self.arkUserIdEdit = QtGui.QLineEdit(self.userPage)
        self.arkUserIdEdit.setObjectName(_fromUtf8("arkUserIdEdit"))
        self.gridLayout_5.addWidget(self.arkUserIdEdit, 8, 1, 1, 1)
        SettingsWizard.addPage(self.userPage)
        self.confirmPage = ConfirmPage()
        self.confirmPage.setObjectName(_fromUtf8("confirmPage"))
        self.gridLayout_4 = QtGui.QGridLayout(self.confirmPage)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.projectFileLabel = QtGui.QLabel(self.confirmPage)
        self.projectFileLabel.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.projectFileLabel.setWordWrap(True)
        self.projectFileLabel.setObjectName(_fromUtf8("projectFileLabel"))
        self.gridLayout_4.addWidget(self.projectFileLabel, 0, 0, 1, 1)
        self.confirmLabel = QtGui.QLabel(self.confirmPage)
        self.confirmLabel.setWordWrap(True)
        self.confirmLabel.setObjectName(_fromUtf8("confirmLabel"))
        self.gridLayout_4.addWidget(self.confirmLabel, 2, 0, 1, 1)
        self.projectFileEdit = QtGui.QLineEdit(self.confirmPage)
        self.projectFileEdit.setObjectName(_fromUtf8("projectFileEdit"))
        self.gridLayout_4.addWidget(self.projectFileEdit, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        SettingsWizard.addPage(self.confirmPage)
        self.folderLabel.setBuddy(self.projectFolderEdit)
        self.projectCodeLabel.setBuddy(self.projectCodeEdit)
        self.projectNameLabel.setBuddy(self.projectNameEdit)
        self.arkUrlLabel.setBuddy(self.arkUrlEdit)
        self.siteCodesLabel.setBuddy(self.siteCodesEdit)
        self.arkUserIdLabel.setBuddy(self.arkUserIdEdit)
        self.userFullnameLabel.setBuddy(self.userFullnameEdit)
        self.userInitialsLabel.setBuddy(self.userInitialsEdit)
        self.projectFileLabel.setBuddy(self.projectFileEdit)

        self.retranslateUi(SettingsWizard)
        QtCore.QMetaObject.connectSlotsByName(SettingsWizard)
        SettingsWizard.setTabOrder(self.projectFolderEdit, self.projectFolderButton)
        SettingsWizard.setTabOrder(self.projectFolderButton, self.projectCodeEdit)
        SettingsWizard.setTabOrder(self.projectCodeEdit, self.projectNameEdit)
        SettingsWizard.setTabOrder(self.projectNameEdit, self.siteCodesEdit)
        SettingsWizard.setTabOrder(self.siteCodesEdit, self.arkUrlEdit)
        SettingsWizard.setTabOrder(self.arkUrlEdit, self.userFullnameEdit)
        SettingsWizard.setTabOrder(self.userFullnameEdit, self.userInitialsEdit)
        SettingsWizard.setTabOrder(self.userInitialsEdit, self.arkUserIdEdit)
        SettingsWizard.setTabOrder(self.arkUserIdEdit, self.projectFileEdit)

    def retranslateUi(self, SettingsWizard):
        SettingsWizard.setWindowTitle(_translate("SettingsWizard", "ARK Spatial - Settings Wizard", None))
        self.WelcomePage.setTitle(_translate("SettingsWizard", "New Project Wizard", None))
        self.WelcomePage.setSubTitle(_translate("SettingsWizard", "This wizard will walk you through setting up a new ARK Spatial project.", None))
        self.folderPage.setTitle(_translate("SettingsWizard", "Project Folder", None))
        self.folderPage.setSubTitle(_translate("SettingsWizard", "Please choose the folder where the project files will be stored.", None))
        self.folderLabel.setText(_translate("SettingsWizard", "This folder is usually something like \"Projects/TST01/GIS/\" where TST01 is the Project or Site Code. The folder will be created if it does not already exist.\n"
"\n"
"ARK Spatial will automatically organise the data under this folder.\n"
"", None))
        self.projectFolderEdit.setPlaceholderText(_translate("SettingsWizard", "Projects/TST01/GIS/", None))
        self.projectPage.setTitle(_translate("SettingsWizard", "Project Details", None))
        self.projectPage.setSubTitle(_translate("SettingsWizard", "Enter the details for the Project. You must enter at least a Project Code. If multiple Site Codes are entered then the first Site Code will be used as the default Site Code. If no Site Code is entered, the Project Code is used instead. For an existing Project, these values should already be set.", None))
        self.projectCodeLabel.setText(_translate("SettingsWizard", "Project Code:", None))
        self.projectNameLabel.setText(_translate("SettingsWizard", "Project Name:", None))
        self.projectCodeEdit.setPlaceholderText(_translate("SettingsWizard", "1234L", None))
        self.projectNameEdit.setPlaceholderText(_translate("SettingsWizard", "Shuqba Cave, Wadi an-Natuf", None))
        self.arkUrlLabel.setText(_translate("SettingsWizard", "ARK URL (optional):", None))
        self.arkUrlEdit.setPlaceholderText(_translate("SettingsWizard", "http://www.arch.cam.ac.uk/shuqba", None))
        self.siteCodesLabel.setText(_translate("SettingsWizard", "Site Code(s):", None))
        self.siteCodesEdit.setPlaceholderText(_translate("SettingsWizard", "SHU28", None))
        self.label.setText(_translate("SettingsWizard", "(Entering this URL will enable extra functionality to link the ARK Spatial data with an ARK Database. An example is \"http://100minories.lparchaeology.com/data/\".)", None))
        self.userPage.setTitle(_translate("SettingsWizard", "User Details", None))
        self.userPage.setSubTitle(_translate("SettingsWizard", "Please enter your user details which will be recorded in the editing metadata.", None))
        self.arkUserIdLabel.setText(_translate("SettingsWizard", "ARK User ID (Optional):", None))
        self.userFullnameLabel.setText(_translate("SettingsWizard", "Full Name:", None))
        self.userInitialsLabel.setText(_translate("SettingsWizard", "Initials:", None))
        self.userFullnameEdit.setPlaceholderText(_translate("SettingsWizard", "Dorothy Garrod", None))
        self.userInitialsEdit.setPlaceholderText(_translate("SettingsWizard", "DG", None))
        self.arkUserIdEdit.setPlaceholderText(_translate("SettingsWizard", "dgarrod", None))
        self.confirmPage.setTitle(_translate("SettingsWizard", "Create Project", None))
        self.confirmPage.setSubTitle(_translate("SettingsWizard", "Create your new project.", None))
        self.projectFileLabel.setText(_translate("SettingsWizard", "Please enter the name for the project file which will be saved in the /project subfolder.", None))
        self.confirmLabel.setText(_translate("SettingsWizard", "Click on the Done button to create your project. All required folders and files will be created. No existing data files will be overwritten.\n"
"\n"
"Once the project is created you can modify these settings or configure more settings in the Settings Dialog.", None))
        self.projectFileEdit.setPlaceholderText(_translate("SettingsWizard", "SHU28_DG", None))

from ..settings_wizard_page import ConfirmPage, FolderPage, ProjectPage, UserPage
