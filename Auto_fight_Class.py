import win32gui
import win32con
import win32api
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel

import time
from pynput.mouse import Listener, Button
from PySide6.QtCore import QThread, Signal
from Ui.Ui_Auto_fight import Ui_Auto_fight
# This Python file uses the following encoding: utf-8

global_hwnd1 = -1
global_hwnd2 = -1
class WorkerThread(QThread):
    result_ready = Signal(str)
    def __init__(self, key_code):
        super().__init__()
        self.key_code = key_code
        self.state_1 = False
        self.state_2 = False
        #self.stop_event = threading.Event()

    def run(self):
        global global_hwnd1
        global global_hwnd2
        while self.state_1 or self.state_2:
            if self.state_1 == True:
                # print("p1")
                win32api.SendMessage(global_hwnd1, win32con.WM_KEYDOWN, ord('W'), 0)
                time.sleep(0.05)  # 按键间隔
                win32api.SendMessage(global_hwnd1, win32con.WM_KEYUP, ord('W'), 0)
                time.sleep(0.1)
                win32api.SendMessage(global_hwnd1, win32con.WM_KEYDOWN, ord('A'), 0)
                time.sleep(0.05)  # 按键间隔
                win32api.SendMessage(global_hwnd1, win32con.WM_KEYUP, ord('A'), 0)

            if self.state_2 == True:
                # print("p2")
                win32api.SendMessage(global_hwnd2, win32con.WM_KEYDOWN, ord('W'), 0)
                time.sleep(0.05)  # 按键间隔
                win32api.SendMessage(global_hwnd2, win32con.WM_KEYUP, ord('W'), 0)
                time.sleep(0.1)
                win32api.SendMessage(global_hwnd2, win32con.WM_KEYDOWN, ord('A'), 0)
                time.sleep(0.05)  # 按键间隔
                win32api.SendMessage(global_hwnd2, win32con.WM_KEYUP, ord('A'), 0)

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.hwnd_1 = -1
        self.hwnd_2 = -1
        self.flag = False
        self.setWindowTitle("紫衣工具箱")
        self.ui = Ui_Auto_fight()
        self.ui.setupUi(self)
        self.ui.plainTextEdit.setPlainText("感谢使用")
        self.time = eval(self.ui.lineEdit_time.text())

        self.ui.lineEdit_handle1.setText("未定义")
        self.ui.lineEdit_handle2.setText("未定义")
        self.ui.lineEdit_title1.setText("未定义")
        self.ui.lineEdit_title2.setText("未定义")

        self.ui.pushButton_1.clicked.connect(self.game_1)
        self.ui.pushButton_2.clicked.connect(self.game_2)

        self.ui.pushButton_start_1.clicked.connect(self.my_start_1)
        self.ui.pushButton_start_2.clicked.connect(self.my_start_2)

        self.ui.pushButton_stop_1.clicked.connect(self.stop_thread_1)
        self.ui.pushButton_stop_2.clicked.connect(self.stop_thread_2)

        key_code = ['w', 'a']
        self.worker_thread = WorkerThread(key_code)

        # self.worker_thread.result_ready.connect(self.handle_result)
        self.worker_thread.start()

    def stop_thread_1(self):
        if self.worker_thread.state_1 == True:
            self.worker_thread.state_1 = False
            print("state1 停止")
            start_string = "停止 : 窗口1 : " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            self.ui.plainTextEdit.appendPlainText(start_string)

    def stop_thread_2(self):
        if self.worker_thread.state_2 == True:
            self.worker_thread.state_2 = False
            print("state2 停止")
            start_string = "停止 : 窗口2 : " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            self.ui.plainTextEdit.appendPlainText(start_string)
            self.flag = True

    def game_1(self):
        time.sleep(2)
        point = win32api.GetCursorPos() # 获得鼠标位置
        hwnd_1 = win32gui.WindowFromPoint(point)  # 获得对应位置的句柄
        title_1 = win32gui.GetWindowText(hwnd_1)

        self.hwnd_1 = hwnd_1
        global global_hwnd1
        global_hwnd1 = hwnd_1
        self.ui.lineEdit_handle1.setText(str(hwnd_1))
        self.title_1 = title_1
        self.ui.lineEdit_title1.setText(str(title_1))

    def game_2(self):
        time.sleep(2)
        point = win32api.GetCursorPos() # 获得鼠标位置
        hwnd_2 = win32gui.WindowFromPoint(point)  # 获得对应位置的句柄
        title_2 = win32gui.GetWindowText(hwnd_2)

        self.hwnd_2 = hwnd_2
        global global_hwnd2
        global_hwnd2 = hwnd_2
        self.ui.lineEdit_handle2.setText(str(hwnd_2))
        self.title_2 = title_2
        self.ui.lineEdit_title2.setText(str(title_2))

    def my_start_1(self):
        if self.worker_thread.state_1 == False:
            start_string = "开始 : 窗口1 : " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            self.ui.plainTextEdit.appendPlainText(start_string)
            #self.ui.plainTextEdit.appendPlainText("倒计时三秒后开始")
            #Tab_key = self.ui.lineEdit_Tab.text()
            #A_key = self.ui.lineEdit_A.text()
            #self.keys_sequence = [Tab_key, A_key]  # 按键序列
            #time.sleep(3)
            self.worker_thread.state_1 = True
            self.worker_thread.start()

    def my_start_2(self):
        if self.worker_thread.state_2 == False:
            start_string = "开始 : 窗口2 : " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            self.ui.plainTextEdit.appendPlainText(start_string)
            #self.ui.plainTextEdit.appendPlainText("倒计时三秒后开始")
            #Tab_key = self.ui.lineEdit_Tab.text()
            #A_key = self.ui.lineEdit_A.text()
            #self.keys_sequence = [Tab_key, A_key]  # 按键序列
            #time.sleep(3)
            self.worker_thread.state_2 = True
            self.worker_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

