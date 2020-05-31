from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
##from src.StartScreen import StartScreen
##from src.MenuScreen import MenuScreen
##from src.QueueAllScreen import QueueAllScreen
##from src.DetailQueueScreen import DetailQueueScreen
import csv

kv ="""
<Option>:
    color_r: 0
    color_g: 0.8
    color_b: 0.9
    r: 0
    g: 0.5
    b: 0.5
    Image:
        source: "Pictures/Restaurant Menu.png"
    BoxLayout:
        canvas:
            Color:
                rgba: root.color_r, root.color_g, root.color_b ,1
            Rectangle:
                size: self.size
                pos: self.pos
        orientation: 'vertical'

        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(16)
            canvas:
                Color:
                    rgba: root.r, root.g, root.b, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
            FloatLayout:
                Button:
                    size_hint: 0.2, 1
                    pos_hint: {'left': 1, 'center_y': .5}
                    text: 'Back'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Start'
                
        GridLayout:
            rows: 3
            padding: dp(160),dp(80),dp(160),dp(80)
            spacing: dp(20)
            Button:
                size_hint_y: None
                height: dp(100)
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '30sp'
                text: 'Default Theme'
                on_press:
                    root.default()
            Button:
                size_hint_y: None
                height: dp(100)
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '30sp'
                text: 'Watermelon Theme'
                on_press: 
                    root.Theme1()
            Button:
                size_hint_y: None
                height: dp(100)
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '30sp'
                text: 'Pineapple Theme'
                on_press: 
                    root.Theme2()
"""

Builder.load_string(kv)

class Option(Screen):
    top = {} # for top background color
    bg = {} # for background color
            # {'r':0, 'b':0, 'g':0}
            
    def __init__(self,startScreen, menuScreen ,queueallScreen,detailScreen,**kwargs):
        super(Option,self).__init__(**kwargs)
        self.start = startScreen
        self.menu = menuScreen
        self.queue = queueallScreen
        self.detail = detailScreen

        # read setting file

        with open('settings/top.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                self.top[row[0]] = float(row[1])

        with open('settings/bg.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                self.bg[row[0]] = float(row[1])

        self.setTheme()
        
    def setTheme(self):
        """set background color"""

        # Menu Screen
        self.menu.color_r = self.bg['r']
        self.menu.color_g = self.bg['g']
        self.menu.color_b = self.bg['b']

        # Queue All Screen
        self.queue.color_r = self.bg['r']
        self.queue.color_g = self.bg['g']
        self.queue.color_b = self.bg['b']

        # Detail Queue Screen
        self.detail.color_r = self.bg['r']
        self.detail.color_g = self.bg['g']
        self.detail.color_b = self.bg['b']

        # Start Screen
        self.start.color_r = self.bg['r']
        self.start.color_g = self.bg['g']
        self.start.color_b = self.bg['b']

        # Option Screen / This Screen
        self.color_r = self.bg['r']
        self.color_g = self.bg['g']
        self.color_b = self.bg['b']


        """ set top background color """

        # Menu Screen
        self.menu.r = self.top['r']
        self.menu.g = self.top['g']
        self.menu.b = self.top['b']

        # Queue All Screen
        self.queue.r = self.top['r']
        self.queue.g = self.top['g']
        self.queue.b = self.top['b']

        # Detail Queue Screen
        self.detail.r = self.top['r']
        self.detail.g = self.top['g']
        self.detail.b = self.top['b']

        # Option Screen / This Screen
        self.r = self.top['r']
        self.g = self.top['g']
        self.b = self.top['b']


    def default(self):
        """default color"""

        # top background color
        self.top = {'r': 1, 'g': 0.5, 'b': 0.5}
        # background color
        self.bg = {'r': 0, 'g': 0.8, 'b': 0.9}

        # setting theme
        self.setTheme()

        # save this color to csv
        self.writeFile()

    def Theme1(self):
        """Watermelon theme color"""

        # top background color
        self.top = {'r': 0.4, 'g': 0.8, 'b': 0.5}
        # background color
        self.bg = {'r': 0.9, 'g': 0.5, 'b': 1.5}

        # setting theme
        self.setTheme()

        # save this color to csv
        self.writeFile()

    def Theme2(self):
        """Pineapple theme color"""

        # top background color
        self.top = {'r': 32/255, 'g': 191/255, 'b': 107/255}
        # background color
        self.bg = {'r': 247/255, 'g': 183/255, 'b': 49/255}

        # setting theme
        self.setTheme()

        # save this color to csv
        self.writeFile()


    

    def writeFile(self):
        """Write File to keep color in csv """

        with open('settings/top.csv', mode='w') as top_file:
            top_writer = csv.writer(
                top_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            top_writer.writerow(['r', str(self.top['r'])])
            top_writer.writerow(['g', str(self.top['g'])])
            top_writer.writerow(['b', str(self.top['b'])])

        with open('settings/bg.csv', mode='w') as bg_file:
            bg_writer = csv.writer(
                bg_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            bg_writer.writerow(['r', str(self.bg['r'])])
            bg_writer.writerow(['g', str(self.bg['g'])])
            bg_writer.writerow(['b', str(self.bg['b'])])
