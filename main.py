import sys, os.path
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QScrollArea, QAction, QLabel, QCheckBox, QApplication, QWidget, QFileDialog, QGridLayout, QFrame, QCalendarWidget, QPushButton, QLineEdit
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QPalette, QTextCharFormat
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from pandas import to_datetime
from numpy import log
from map.mapplot import MapCoordinates
from solid.pysolid import PySolid
        
class MarkdownPopup(QScrollArea): 
    def __init__(self, filename=None):
        super().__init__()

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        self.setGeometry(100, 60, 800, 450)

        markdown_viewer = QTextEdit()
        markdown_viewer.setReadOnly(True)
        
        with open(filename, 'r') as file:
            data = file.read().rstrip()
        markdown_text = data
        markdown_viewer.setMarkdown(markdown_text)

        title = os.path.splitext(filename)[0].capitalize() 
        self.setWindowTitle(title)

        main_layout.addWidget(markdown_viewer)



class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.initVar()
        self.initUI()
        self.plot_earth_tide()

    def initVar(self):
        self.date_begin = QDate.currentDate()
        self.date_end = None
        self.latitude  = -22.80719940
        self.longitude = -47.05231470
        self.ps = PySolid()

    def initUI(self):
        self.resize(870, 650)
        main_layout = QGridLayout()

        # Menubar
        menu_bar = self.menuBar()

        save_menu = menu_bar.addMenu('Salvar')

        savedata_action = QAction('Salvar dados', self)
        savedata_action.setShortcut('Ctrl+S')
        savedata_action.setStatusTip('Salve um arquivo texto com os dados do gráfico')
        savedata_action.triggered.connect(self.savedata_clicked)

        save_menu.addAction(savedata_action)
        saveimage_action = QAction('Salvar imagem', self)
        saveimage_action.setStatusTip('Salve a imagem do gráfico')
        saveimage_action.triggered.connect(self.saveimage_clicked)
        save_menu.addAction(saveimage_action)

        help_menu = menu_bar.addMenu('Ajuda')

        tutorial_action = QAction('Tutorial', self)
        tutorial_action.triggered.connect(self.tutorial_clicked)
        help_menu.addAction(tutorial_action)

        about_action = QAction('Sobre', self)
        about_action.triggered.connect(self.about_clicked)
        help_menu.addAction(about_action)


        # Calendar frame
        calendar_frame = QFrame(self)
        calendar_frame.setObjectName("calendar_frame")
        calendar_frame.setStyleSheet("#calendar_frame {border-width: 1;border-radius: 3;border-style: solid;border-color: rgb(10, 10, 10)}")
        calendar_frame.setMaximumHeight(300)
        main_layout.addWidget(calendar_frame, 0, 0)
        calendar_layout = QGridLayout(calendar_frame)

        self.calendar = QCalendarWidget(calendar_frame)
        self.calendar.setGridVisible(True)
        self.calendar.highlight_format = QTextCharFormat()
        self.calendar.highlight_format.setBackground(self.palette().brush(QPalette.Highlight))
        self.calendar.highlight_format.setForeground(self.palette().color(QPalette.HighlightedText))
        self.calendar.clicked.connect(self.calendar_is_clicked)
        calendar_layout.addWidget(self.calendar, 0, 0, 1, 2)

        self.date_begin_label = QLabel(calendar_frame)
        self.date_begin_label.setText('Data de Fim:')
        calendar_layout.addWidget(self.date_begin_label, 1, 0)
        self.date_begin_textbox = QLineEdit(calendar_frame)
        self.date_begin_textbox.setPlaceholderText('Data de Início (dd/mm/yyyy)')
        self.date_begin_textbox.setText(self.date_begin.toString("dd/MM/yyyy"))
        self.date_begin_textbox.textChanged.connect(self.updateCalendar)
        calendar_layout.addWidget(self.date_begin_textbox, 2, 0)

        self.date_end_label = QLabel(calendar_frame)
        self.date_end_label.setText('Data de Fim:')
        calendar_layout.addWidget(self.date_end_label, 1, 1)
        self.date_end_textbox = QLineEdit(calendar_frame)
        self.date_end_textbox.setPlaceholderText('Data de Fim (dd/mm/yyyy)')
        self.date_end_textbox.textChanged.connect(self.updateCalendar)
        calendar_layout.addWidget(self.date_end_textbox, 2, 1)


        # Map frame
        map_frame = QFrame(self)
        map_frame.setObjectName("map_frame")
        map_frame.setStyleSheet("#map_frame {border-width: 1;border-radius: 3;border-style: solid;border-color: rgb(10, 10, 10)}")
        map_frame.setMaximumHeight(300)
        main_layout.addWidget(map_frame, 0, 1)
        map_layout = QGridLayout(map_frame)

        self.map_figure = Figure()
        self.map_ax = self.map_figure.add_subplot(111)
        self.map_canvas = FigureCanvasQTAgg(self.map_figure)
        map_layout.addWidget(self.map_canvas, 0, 0, 1, 2)
        self.map_plot = MapCoordinates()
        self.map_plot.init_plot(ax=self.map_ax, x=self.longitude, y=self.latitude)
        self.map_canvas.mpl_connect("button_release_event", self.map_is_clicked)
        
        self.latitude_label = QLabel(calendar_frame)
        self.latitude_label.setText('Latitude:')
        map_layout.addWidget(self.latitude_label, 1, 0)
        self.latitude_textbox = QLineEdit(map_frame)
        self.latitude_textbox.setPlaceholderText('Latitude: ')
        self.latitude_textbox.setText(str(self.latitude))
        self.latitude_textbox.textChanged.connect(self.updateMap)
        map_layout.addWidget(self.latitude_textbox, 2, 0)

        self.longitude_label = QLabel(calendar_frame)
        self.longitude_label.setText('Longitude:')
        map_layout.addWidget(self.longitude_label, 1, 1)
        self.longitude_textbox = QLineEdit(map_frame)
        self.longitude_textbox.setPlaceholderText('Longitude: ')
        self.longitude_textbox.setText(str(self.longitude))
        self.longitude_textbox.textChanged.connect(self.updateMap)
        map_layout.addWidget(self.longitude_textbox, 2, 1)


        # Plot frame
        plot_frame = QFrame(self)
        plot_frame.setObjectName("plot_frame")
        plot_frame.setStyleSheet("#plot_frame {border-width: 1;border-radius: 3;border-style: solid;border-color: rgb(10, 10, 10)}")
        main_layout.addWidget(plot_frame, 1, 0, 1, 2)
        plot_layout = QGridLayout(plot_frame)

        self.figure = Figure()
        self.plot_ax = self.figure.add_subplot(111)
        self.plot_canvas = FigureCanvasQTAgg(self.figure)
        self.plot_toolbar = NavigationToolbar2QT(self.plot_canvas, self)
        self.addToolBar(Qt.BottomToolBarArea, self.plot_toolbar)
        plot_layout.addWidget(self.plot_canvas, 1, 0, 1, 4)


        self.radial_checkbox = QCheckBox("Radial",self)
        self.radial_checkbox.setChecked(True)
        self.radial_checkbox.stateChanged.connect(self.show_portion_plots)
        plot_layout.addWidget(self.radial_checkbox, 0, 0)

        self.latitudinal_checkbox = QCheckBox("Latitudinal",self)
        self.latitudinal_checkbox.setChecked(True)
        self.latitudinal_checkbox.stateChanged.connect(self.show_portion_plots)
        plot_layout.addWidget(self.latitudinal_checkbox, 0, 1)

        self.longitudinal_checkbox = QCheckBox("Longitudinal",self)
        self.longitudinal_checkbox.setChecked(True)
        self.longitudinal_checkbox.stateChanged.connect(self.show_portion_plots)
        plot_layout.addWidget(self.longitudinal_checkbox, 0, 2)

        self.plot_button = QPushButton('Plot', self)
        self.plot_button.clicked.connect(self.plot_earth_tide)
        plot_layout.addWidget(self.plot_button, 0, 3)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('PySolidGUI')
        self.show()

    
# ---------- Menu functions ----------
    def savedata_clicked(self):
        try: self.ps.df_solid
        except AttributeError: return
        
        filename, _ = QFileDialog.getSaveFileName(self,"Save File", "data.txt", "Text Files(*.txt);All Files(*)")
        if filename == "": return

        with open(filename, 'w') as f:
            f.write(f"# Data parameters:\n")
            f.write(f"#   Latitude, Longitude: {self.latitude}, {self.longitude}\n")
            f.write(f"#   Days: {self.date_begin.toString('dd/MM/yyyy')} to {self.date_end.toString('dd/MM/yyyy')}\n")
            self.ps.df_solid.to_csv(f, index=False)
        self.fileName = filename

    def saveimage_clicked(self):
        try: self.ps.df_solid
        except AttributeError: return
        filename, _ = QFileDialog.getSaveFileName(self, "Save Image", "image.png", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filename == "":
            return
        self.figure.savefig(filename)

    def tutorial_clicked(self):
        filename = "docs/tutorial.md"
        self.popup = MarkdownPopup(filename)
        self.popup.show()
        
    def about_clicked(self):
        filename = "docs/about.md"
        self.popup = MarkdownPopup(filename)
        self.popup.show()


# ---------- Calendar functions ----------
    def calendar_is_clicked(self, date):
        self.format_range(QTextCharFormat()) # reset highlighting of previously selected date range 
        if QApplication.instance().keyboardModifiers() & Qt.ShiftModifier and self.date_begin!=date:
            if self.date_end:
                if date < self.date_begin: self.date_begin = date
                else: self.date_end = date
            else:
                self.date_begin, self.date_end = sorted([self.date_begin, date])
            self.format_range(self.calendar.highlight_format)
        else:
            self.date_begin = date
            self.date_end = None
        self.updateDateText()
        
    def updateCalendar(self):
        self.format_range(QTextCharFormat())
        try:
            date_begin = QDate.fromString(self.date_begin_textbox.text(), "dd/MM/yyyy")
            if date_begin.isValid():
                self.calendar.setSelectedDate(date_begin)
                self.date_begin = date_begin
        except: pass

        try:
            date_end = QDate.fromString(self.date_end_textbox.text(), "dd/MM/yyyy")
            if date_end.isValid():
                self.calendar.setSelectedDate(date_end)
                self.date_end = date_end
        except: pass
        
        self.format_range(self.calendar.highlight_format)
    
    def updateDateText(self):
        self.date_begin_textbox.blockSignals(True)
        self.date_end_textbox.blockSignals(True)

        self.date_begin_textbox.setText(self.date_begin.toString("dd/MM/yyyy"))
        if self.date_end:
            self.date_end_textbox.setText(self.date_end.toString("dd/MM/yyyy"))
        else:
            self.date_end_textbox.setText(None)

        self.date_begin_textbox.blockSignals(False)
        self.date_end_textbox.blockSignals(False)

    def format_range(self, format):
        if self.date_begin and self.date_end:
            d0, d1 = sorted([self.date_begin, self.date_end])
            while d0 <= d1:
                self.calendar.setDateTextFormat(d0, format)
                d0 = d0.addDays(1)


# ---------- Map functions ----------
    def map_is_clicked(self, event):
        self.longitude_textbox.blockSignals(True)
        self.latitude_textbox.blockSignals(True)

        if event.inaxes != self.map_ax: return
        self.longitude, self.latitude = self.map_plot.get_point()
        self.latitude_textbox.setText(str(self.latitude))
        self.longitude_textbox.setText(str(self.longitude))

        self.longitude_textbox.blockSignals(False)
        self.latitude_textbox.blockSignals(False)

    def updateMap(self):
        try:
            x = float(self.longitude_textbox.text())
            y = float(self.latitude_textbox.text())
            self.map_plot.place_point(self.map_ax, x, y)
            self.map_ax.figure.canvas.draw()
            self.longitude, self.latitude = self.map_plot.get_point()
        except Exception as e:
            # print(str(e))
            pass


# ---------- Plot functions ----------
    def show_portion_plots(self, state=True):
        for l, line in enumerate(self.plot_ax.get_lines()):
            checkstate = getattr(self, f"{line.get_label().lower()}_checkbox").checkState()
            self.legend.legendHandles[l].set_visible(checkstate)
            line.set_visible(checkstate)

        self.plot_ax.relim(visible_only=True)
        self.plot_ax.autoscale()
        self.legend = self.plot_ax.legend(loc='upper left', bbox_to_anchor=(1.0, 0.9), ncol=1, fancybox=True, shadow=True)
        self.plot_ax.figure.canvas.draw()


    def calculate_sec_step(self, days):
        force = 300
        steps = force*log(days+1)
        return int(days*86400/steps)
    
    def plot_earth_tide(self):
        if self.date_end == None: self.date_end = self.date_begin
        days = self.date_begin.daysTo(self.date_end) + 1
        
        self.plot_ax.clear()
        self.ps.set_coordinates(self.latitude, self.longitude)
        self.ps.set_time_range(self.date_begin.toString("dd/MM/yyyy"), days=days, step=self.calculate_sec_step(days))
        self.ps.tide_calculation()
        x = to_datetime(self.ps.df_solid['date time'], format="%d/%m/%Y %H:%M:%S")
        y1 = self.ps.df_solid['north']
        y2 = self.ps.df_solid['east']
        y3 = self.ps.df_solid['radial']

        self.figure.subplots_adjust(0.1, 0.2, 0.82, 0.85)
        self.plot_ax.set_title(f"Deslocamento terrestre dos dias {self.date_begin.toString('dd/MM/yyyy')} a {self.date_end.toString('dd/MM/yyyy')}\n"+
                               f"Latitude: {self.latitude}, Longitude: {self.longitude}"
                               , 
                               fontsize = 10)
        self.rad_plot, = self.plot_ax.plot(x, y3, '.-', markersize=5, color="blue" , label="Radial")
        self.lat_plot, = self.plot_ax.plot(x, y1, '^-', markersize=2 , color="green", label="Latitudinal")
        self.lon_plot, = self.plot_ax.plot(x, y2, 's-', markersize=2 , color="red"  , label="Longitudinal")

        self.plot_ax.grid(True)
        self.legend = self.plot_ax.legend(loc='upper left', bbox_to_anchor=(1.0, 0.9), ncol=1, fancybox=True, shadow=True)
        self.plot_ax.xaxis.set_major_formatter(DateFormatter('%d/%m/%y\n%H:%M'))
        self.plot_ax.set_ylabel("Deslocamento (metros)")
        
        self.show_portion_plots()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui()
    sys.exit(app.exec_())
