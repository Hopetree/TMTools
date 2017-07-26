# -*- coding: utf-8 -*-

class QSS():
    def __init__(self):
        self.White = '''/**********主界面样式**********/
QWidget#MainWindow {
        font-family:Microsoft YaHei;
        font-size:13px;
        border: 0px solid rgb(111, 156, 207);
        background: rgb(232, 241, 252);
}
QWidget#messageWidget {
        background: rgba(173, 202, 232, 50%);
}
/**********菜单栏**********/
QMenuBar {
        font-size:13px;
        background: rgb(187, 212, 238);
        border: 1px solid rgb(111, 156, 207);
        border-left: none;
        border-right: none;
}
QMenuBar::item {
        font-size:13px;
        font-family:Microsoft YaHei;
        border: 0px solid transparent;
        padding: 5px 10px 5px 10px;
        background: transparent;
}
QMenuBar::item:enabled {
        font-size:13px;
        color: rgb(2, 65, 132);
}
QMenuBar::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenuBar::item:enabled:selected {
        border-top-color: rgb(111, 156, 207);
        border-bottom-color: rgb(111, 156, 207);
        background: rgb(198, 224, 252);
}
/**********菜单**********/
QMenu {
        font-size:13px;
        font-family:Microsoft YaHei;
        border: 1px solid rgb(111, 156, 207);
        background: rgb(232, 241, 250);
}
QMenu::item {
        font-family:Microsoft YaHei;
        height: 18px;
        padding: 5px 25px 5px 20px;
        padding-left: 30px;
        padding-right: 12px;
}
QMenu::item:enabled {
        color: rgb(84, 84, 84);
}
QMenu::item:!enabled {
        color: rgb(155, 155, 155);
}
QMenu::item:enabled:selected {
        color: rgb(2, 65, 132);
        background: rgba(255, 255, 255, 200);
}
QMenu::separator {
        height: 1px;
        background: rgb(111, 156, 207);
}
QMenu::indicator {
        width: 13px;
        height: 13px;
}
QMenu::icon {
        padding-left: 12px;
        padding-right: 0px;
}

/**********状态栏**********/
QStatusBar {
        font-size:13px;
        font-family:Microsoft YaHei;
        background: rgb(187, 212, 238);
        border: 1px solid rgb(111, 156, 207);
        border-left: none;
        border-right: none;
        border-bottom: none;
}
QStatusBar::item {
        font-family:Microsoft YaHei;
        border: none;
        border-right: 1px solid rgb(111, 156, 207);
}
/**********分组框**********/
QGroupBox {
        font-size:13px;
        font-family:Microsoft YaHei;
        border: 1px solid rgb(111, 156, 207);
        border-radius: 4px;
        margin-top: 10px;
}
QGroupBox::title {
        font-family:Microsoft YaHei;
        color: rgb(56, 99, 154);
        top: -10px;
        left: 10px;
}
/**********滚动条-垂直**********/
QScrollBar:vertical {
        width: 20px;
        background: transparent;
        margin-left: 3px;
        margin-right: 3px;
}
QScrollBar::handle:vertical {
        width: 20px;
        min-height: 30px;
        background: rgb(170, 200, 230);
        margin-top: 15px;
        margin-bottom: 15px;
}
QScrollBar::handle:vertical:hover {
        background: rgb(165, 195, 225);
}
QScrollBar::sub-line:vertical {
        height: 15px;
        background: transparent;
        image: url("White/topArrow.png");
        subcontrol-position: top;
}
QScrollBar::add-line:vertical {
        height: 15px;
        background: transparent;
        image: url("White/bottomArrow.png");
        subcontrol-position: bottom;
}
QScrollBar::sub-line:vertical:hover {
        background: rgb(170, 200, 230);
}
QScrollBar::add-line:vertical:hover {
        background: rgb(170, 200, 230);
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: transparent;
}

QScrollBar#verticalScrollBar:vertical {
        margin-top: 30px;
}
/**********页签项**********/
QTabWidget::pane {
        font-family:Microsoft YaHei;
        border: none;
        border-top: 3px solid rgb(0, 78, 161);
        background: rgb(187, 212, 238);
}
QTabWidget::tab-bar {
        border: none;
}
QTabBar::tab {
        font-family:Microsoft YaHei;
        border: none;
        border-top-left-radius: 4px;
        border-top-right-radius: 4px;
        color: white;
        background: rgb(120, 170, 220);
        height: 28px;
        min-width: 85px;
        margin-right: 5px;
        padding-left: 5px;
        padding-right: 5px;
}
QTabBar::tab:hover {
        background: rgb(0, 78, 161);
}
QTabBar::tab:selected {
        color: white;
        background: rgb(0, 78, 161);
}

QTabWidget#tabWidget::pane {
        border: 1px solid rgb(111, 156, 207);
        background: rgb(232, 241, 252);
        margin-top: -1px;
}

QTabBar#tabBar::tab {
        border: 1px solid rgb(111, 156, 207);
        border-bottom: none;
        color: rgb(70, 71, 73);
        background: transparent;
}
QTabBar#tabBar::tab:hover {
        color: rgb(2, 65, 132);
}
QTabBar#tabBar::tab:selected {
        color: rgb(2, 65, 132);
        background: rgb(232, 241, 252);
}
/**********进度条**********/
QProgressBar {
        border: none;
        text-align: center;
        color: white;
        background-color: transparent;
        background-image: url("White/progressBar.png");
        background-repeat: repeat-x;
}
QProgressBar::chunk {
        border: none;
        background-color: transparent;
        background-image: url("White/progressBarChunk.png");
        background-repeat: repeat-x;
}
/**********单选框**********/
QRadioButton{
        font-size:13px;
        spacing: 5px;
}
QRadioButton:enabled:checked{
        color: rgb(2, 65, 132);
}
QRadioButton:enabled:!checked{
        color: rgb(70, 71, 73);
}
QRadioButton:enabled:hover{
        color: rgb(0, 78, 161);
}
QRadioButton:!enabled{
        color: rgb(80, 80, 80);
}
QRadioButton::indicator {
        width: 20px;
        height: 20px;
}
QRadioButton::indicator:unchecked {
        image: url("White/radioButton.png");
}
QRadioButton::indicator:unchecked:hover {
        image: url("White/radioButtonHover.png");
}
QRadioButton::indicator:unchecked:pressed {
        image: url("White/radioButtonPressed.png");
}
QRadioButton::indicator:checked {
        image: url("White/radioButtonChecked.png");
}
QRadioButton::indicator:checked:hover {
        image: url("White/radioButtonCheckedHover.png");
}
QRadioButton::indicator:checked:pressed {
        image: url("White/radioButtonCheckedPressed.png");
}
/**********输入框**********/
QLineEdit {
        border-radius: 4px;
        height: 25px;
        border: 1px solid rgb(111, 156, 207);
        background: white;
}
QLineEdit:enabled {
        color: rgb(84, 84, 84);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(51, 51, 51);
}
QLineEdit:!enabled {
        color: rgb(80, 80, 80);
}
/**********文本编辑框**********/
QTextEdit {
        font-family:Microsoft YaHei;
        font:12px;
        border: 1px solid rgb(111, 156, 207);
        color: rgb(70, 71, 73);
        background: rgb(187, 212, 238);
}
/**********滚动区域**********/
QScrollArea {
        border: 1px solid rgb(111, 156, 207);
        background: rgb(187, 212, 238);
}
/**********滚动区域**********/
QWidget#transparentWidget {
        background: transparent;
}
/**********标签**********/
QLabel {
        font-family:Microsoft YaHei;
        font:13px;
        color: rgb(0, 160, 230);
}
/**********按钮**********/
QPushButton{
        border-radius: 4px;
        border: none;
        width: 75px;
        height: 25px;
}
QPushButton:enabled {
        background: rgb(120, 170, 220);
        color: white;
}
QPushButton:!enabled {
        background: rgb(180, 180, 180);
        color: white;
}
QPushButton:enabled:hover{
        background: rgb(100, 140, 230);
}
QPushButton:enabled:pressed{
        background: rgb(0, 78, 161);
}'''