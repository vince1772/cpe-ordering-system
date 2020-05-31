from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, DictProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

import csv

kv = """
# listview info after add food,option
<SelectableFoodOptionBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (.5, .5, .5, 1)
        Rectangle:
            size: self.size
            pos: self.pos
            

# listview info food
<SelectableGeneratedBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (.5, .5, .5, 1)
        Rectangle:
            size: self.size
            pos: self.pos
        
    date: ''
    total: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '23sp'
        text: '{} {} {} php'.format(root.date, root.space(root.date), root.total)
        size_hint_x: None
        size: self.texture_size



<GenerateReport>:
##    rv: rv
    fv: fv
##    ov: ov
    color_r: 0
    color_g: 0.8
    color_b: 0.9
    r: 1
    g: 0.5
    b: 0.5
##    tb_input: tb_input
    BoxLayout:
        canvas:
            Color:
                rgba: root.color_r, root.color_g, root.color_b ,1
            Rectangle:
                size: self.size
                pos: self.pos
                source: "Pictures/Waiter.png"

        orientation: 'vertical'        
        BoxLayout:
            size_hint_y: None
            height: dp(70)
            spacing: dp(16)
            padding: dp(300),dp(15),0,dp(20)
            canvas:
                Color:
                    rgba: root.r, root.g, root.b, 1
                Rectangle:
                    size: self.size
                    pos: self.pos
                    source:"Pictures/TITLE (2).png"
            FloatLayout:
                Button:
                    size_hint: 0.2, 1
                    font_size:'15sp'
                    pos_hint: {'left': 1, 'center_y': .5}
                    text: 'Back'
                    size_hint_x: None
                    size: self.texture_size
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Start'
                    
        GridLayout:
            cols: 2
            rows: 1
            size_hint_y: None
            height: dp(50)
            padding: dp(8),dp(8),dp(8),0
            spacing: dp(16)     
            Label:
                text: 'Generated Report'
                color: 1,1,1,1
                bold: True
                font_size: '22sp'
##            BoxLayout:
##                spacing: dp(8)
##                padding: dp(160),0,0,0
##                Label:
##                    text: ''
##                    color: 1,1,1,1
##                    bold: True
##                    font_size: '22sp'
##                TextInput:
##                    id: tb_input
##                    size_hint_x: 0.6
##                    hint_text: 'value'
##                    padding: dp(10), dp(12), 0, 0
        GridLayout:
            cols: 2
            rows: 1
            padding: dp(10),dp(10),dp(10),dp(10)
            spacing: dp(10)
            GridLayout:
                cols: 1
                FV:
                    id: fv
                    scroll_type: ['bars', 'content']
                    scroll_wheel_distance: dp(114)
                    bar_width: dp(10)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0.09
                        Rectangle:
                            size: self.size
                            pos: self.pos
                    viewclass: 'SelectableGeneratedBoxLayout'
                    SelectableRecycleBoxLayout:
                        default_size: None, dp(49)
                        default_size_hint: 1, None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
                        multiselect: False
                        touch_multiselect: False          
                        spacing: dp(2)
                        padding: dp(10), dp(10), dp(10), 0

                
                
"""

Builder.load_string(kv)

class GenerateReport(Screen):

    def __init__(self, **kwargs):
        super(GenerateReport, self).__init__(**kwargs)
        with open("data/db.csv", 'r', encoding='utf8') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.fv.data.append(dict(row))


class SelectableGeneratedBoxLayout(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)


    def space(self, name):
        """Leave the space equal"""
        return ' ' * (30-len([i for i in name if i not in " awks "]))




class FV(RecycleView):
    select = DictProperty()

    def __init__(self, **kwargs):
        super(FV, self).__init__(**kwargs)



