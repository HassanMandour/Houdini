from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui

import hou

#####################################################################
class Parm_Renamer(QtWidgets.QDialog):
    def __init__(self):
        super().__init__(hou.qt.mainWindow())

        self.configure_dialog()
        self.widgets()
        self.layout()

        self.connections()

    def configure_dialog(self):
        self.setWindowTitle("Parameter Renamer")
        self.setFixedSize(280, 200)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

    def widgets(self):
        self.search = QtWidgets.QLineEdit()
        self.search.setPlaceholderText("Search")

        self.replace = QtWidgets.QLineEdit()
        self.replace.setPlaceholderText("Replace")

        self.type_pattern_label = QtWidgets.QLabel("Type Pattern")
        self.type_pattern = QtWidgets.QLineEdit()
        self.type_pattern.setPlaceholderText("e.g. file* light alembic")

        self.name_pattern_label = QtWidgets.QLabel("Name Pattern")
        self.name_pattern = QtWidgets.QLineEdit()
        self.name_pattern.setPlaceholderText("e.g. cloth*")

        self.path_label = QtWidgets.QLabel("Node Path")
        self.path = QtWidgets.QLineEdit()
        self.path.setPlaceholderText("e.g. /obj /mat /obj/subnet1")

        self.sep = hou.qt.Separator()

        self.okBut = QtWidgets.QPushButton("Rename")
        self.matchsub = QtWidgets.QCheckBox("Match Substrings")
        # self.matchsub.setCheckState(QtCore.Qt.Unchecked)

    def layout(self):
        mainlyt = QtWidgets.QVBoxLayout(self)
        mainlyt.addWidget(self.search)
        mainlyt.addWidget(self.replace)
        mainlyt.addWidget(self.matchsub)
        mainlyt.addWidget(self.sep)

        optionslyt = QtWidgets.QFormLayout(self)
        optionslyt.addRow(self.type_pattern_label, self.type_pattern)
        optionslyt.addRow(self.name_pattern_label, self.name_pattern)
        optionslyt.addRow(self.path_label, self.path)

        butlyt = QtWidgets.QHBoxLayout()
        butlyt.addWidget(self.okBut)

        mainlyt.addLayout(optionslyt)
        mainlyt.addLayout(butlyt)

    def rename(self):
        type_pattern = self.type_pattern.text()
        name_pattern = self.name_pattern.text()
        path = self.path.text()

        find = self.search.text()
        replace = self.replace.text()
        matchsub = "-i" if self.matchsub.isChecked() else ""

        type_pattern = "-t " + type_pattern if type_pattern else ""
        name_pattern = "-n " + name_pattern if name_pattern else ""
        path = "-p " + path if path else ""

        hscript = f"opchange {type_pattern} {name_pattern} {path} {matchsub} -s {find} {replace}"
        # print(hscript)
        hou.hscript(hscript)

    def connections(self):
        self.okBut.clicked.connect(self.rename)
