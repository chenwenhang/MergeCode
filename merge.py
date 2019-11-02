import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QMessageBox

root_path_list = []
suffix_list = []
file_name = ""
total = 0  # 总行数
countBlank = 0  # 空行数
# 以后有时间的话加
countPound = 0  # 注释行数


def get_list(message):
    flag = ''
    name_list = []
    while flag != '0':
        flag = input(message)
        if flag != '0':
            name_list.append(flag.strip())
    return name_list


def get_all_path(open_file_path, suffix_list):
    path_list = []
    root_dir = open_file_path
    file_list = os.listdir(root_dir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(file_list)):
        com_path = os.path.join(root_dir, file_list[i])
        if os.path.isfile(com_path) and os.path.splitext(com_path)[1] in suffix_list:
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path, suffix_list))
    return path_list


def merge(root_path_list, suffix_list, file_name):
    global total, countBlank
    path = []
    for i in range(0, len(root_path_list)):
        path.extend(get_all_path(root_path_list[i], suffix_list))
    with open(file_name, 'w') as write_file_obj:
        for i in range(0, len(path)):
            with open(path[i], encoding='utf-8') as read_file_obj:
                write_file_obj.write(
                    "  =========================  " + os.path.split(path[i])[1] + "  =========================  \n\n")
                for li in read_file_obj.readlines():
                    total += 1
                    if not li.split():  # 判断是否为空行
                        countBlank += 1
                    write_file_obj.write(li)
                write_file_obj.write("\n\n")


# 工具默认生成的参数为Object，会报错，需要改成QtWidgets.QMainWindow
class Ui_MainWindow(QtWidgets.QMainWindow):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 480)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startMergeButton = QtWidgets.QPushButton(self.centralwidget)
        self.startMergeButton.setGeometry(QtCore.QRect(110, 420, 111, 31))
        self.startMergeButton.setObjectName("startMergeButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(410, 30, 95, 65))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.addDicButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.addDicButton.setObjectName("addDicButton")
        self.verticalLayout_4.addWidget(self.addDicButton)
        self.deleteDicButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.deleteDicButton.setObjectName("deleteDicButton")
        self.verticalLayout_4.addWidget(self.deleteDicButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(410, 190, 95, 65))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addSuffixButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.addSuffixButton.setObjectName("addSuffixButton")
        self.verticalLayout_5.addWidget(self.addSuffixButton)
        self.deleteSuffixButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.deleteSuffixButton.setObjectName("deleteSuffixButton")
        self.verticalLayout_5.addWidget(self.deleteSuffixButton)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(410, 340, 95, 65))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.selectLocationButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.selectLocationButton.setObjectName("selectLocationButton")
        self.verticalLayout_6.addWidget(self.selectLocationButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 90, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 330, 71, 81))
        self.label_3.setObjectName("label_3")
        self.dicList = QtWidgets.QListWidget(self.centralwidget)
        self.dicList.setGeometry(QtCore.QRect(110, 30, 256, 131))
        self.dicList.setObjectName("dicList")
        self.suffixList = QtWidgets.QListWidget(self.centralwidget)
        self.suffixList.setGeometry(QtCore.QRect(110, 190, 256, 151))
        self.suffixList.setObjectName("suffixList")
        self.location = QtWidgets.QListWidget(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(110, 360, 256, 31))
        self.location.setObjectName("location")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addDicButton.clicked.connect(self.add_dir)
        self.deleteDicButton.clicked.connect(self.delete_dir)
        self.addSuffixButton.clicked.connect(self.add_suffix)
        self.deleteSuffixButton.clicked.connect(self.delete_suffix)
        self.selectLocationButton.clicked.connect(self.select_location)
        self.startMergeButton.clicked.connect(self.start_merge)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "代码融合统计工具"))
        self.startMergeButton.setText(_translate("MainWindow", "开始整合"))
        self.addDicButton.setText(_translate("MainWindow", "添加"))
        self.deleteDicButton.setText(_translate("MainWindow", "删除"))
        self.addSuffixButton.setText(_translate("MainWindow", "添加"))
        self.deleteSuffixButton.setText(_translate("MainWindow", "删除"))
        self.selectLocationButton.setText(_translate("MainWindow", "选择"))
        self.label.setText(_translate("MainWindow", "文件目录："))
        self.label_2.setText(_translate("MainWindow", "文件后缀名："))
        self.label_3.setText(_translate("MainWindow", "生成地址："))

    def add_dir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", './')
        if dir_choose != "" and dir_choose not in root_path_list:
            root_path_list.append(dir_choose)
            self.dicList.addItem(dir_choose)

    def delete_dir(self):
        if self.dicList.count() != 0:
            root_path_list.remove(self.dicList.currentItem().text())
            self.dicList.takeItem(self.dicList.currentRow())

    def add_suffix(self):
        text, ok = QInputDialog.getText(self, '输入框',
                                        '请输入文件后缀名（不要忘记前面的点）:')
        text = str(text)
        if ok:
            if text != "" and text not in suffix_list:
                suffix_list.append(text)
                self.suffixList.addItem(text)

    def delete_suffix(self):
        if self.suffixList.count() != 0:
            suffix_list.remove(self.suffixList.currentItem().text())
            self.suffixList.takeItem(self.suffixList.currentRow())

    def select_location(self):
        global file_name
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", './')
        if dir_choose != "":
            file_name = dir_choose + "/merge.txt"
            self.location.clear()
            self.location.addItem(dir_choose)

    def start_merge(self):
        global total, countBlank
        if root_path_list == [] or suffix_list == [] or file_name == "":
            reply = QMessageBox.information(self, '提示', '请将信息填写完整！', QMessageBox.Ok)
        else:
            merge(root_path_list, suffix_list, file_name)
            reply = QMessageBox.information(self, '提示',
                                            "整合成功！\n总行数：" + str(total) + "\n空行数：" + str(countBlank),
                                            QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
