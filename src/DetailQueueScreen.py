from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
import csv
import uuid
import datetime

kv = """
# show list food in this queue
<SelectableDetailQueueBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: .5, .5, .5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    foodName: ''
    foodOption: ''
    sumPrice: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '20sp'
        text: '{} {} {} {} php'.format(root.foodName, root.foodOption, root.space(root.foodName,root.foodOption), root.sumPrice)
        size_hint_x: None
        size: self.texture_size
        
<DetailQueueScreen>:
    dv: dv
    detail_text: detail_text
    color_r: 0
    color_g: 0.8
    color_b: 0.9
    r: 1
    g: 0.5
    b: 0.5
    BoxLayout:
        canvas:
            Color:
                rgba: root.color_r  ,root.color_g, root.color_b, 1
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
                    pos_hint: {'left': 1, 'center_y': .5}
                    font_size:'15sp'
                    text: 'Back'
                    size_hint_x: None
                    size: self.texture_size
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'QueueAll'
                Button:
                    size_hint: 0.2, 1
                    pos_hint: {'right': 1, 'center_y': .5}
                    font_size:'15sp'
                    text: 'Main Menu'
                    size_hint_x: None
                    size: self.texture_size
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.current = 'Start'

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(50)
            
            Label:
                text: 'Detailed Order'
                color: 1,1,1,1
                bold: True
                font_size: '25sp'
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(50)
            
            Label:
                id: detail_text
                text: 'Test Text'
                color: 1,1,1,1
                bold: True
                font_size: '25sp'
                font_name: 'font/THSarabunNew Bold.ttf'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(50),0,dp(50),dp(25)     
            RecycleView:
                id: dv
                scroll_type: ['bars', 'content']
                scroll_wheel_distance: dp(114)
                bar_width: dp(10)   
                canvas.before:
##                    Color:
##                        rgba: 0, 0, 0, 0.09
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        source: "Pictures/Red Serve.png"
                        
                viewclass: 'SelectableDetailQueueBoxLayout'
                    
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
        GridLayout:
            cols: 2
            rows: 1
            height: dp(80)
            size_hint_y: None
            spacing: dp(8)
            padding: dp(50),0,dp(50),dp(25)
            Button:
                text: 'Remove'
                font_size: '24sp'
                on_press: root.removeQueue()
            Button:
                text: 'Finish'
                font_size: '24sp'
                on_press: root.saveToDb()
"""

Builder.load_string(kv)


class DetailQueueScreen(Screen):
    detail = {}
    
    def __init__(self, **kwargs):
        super(DetailQueueScreen, self).__init__(**kwargs)

    def getDetail(self,detail):
        """
        model detail
        {
            'queue': val,
            'table': val,
            'foodSelectedList': [
                {'foodName': val, 'foodOption': val, 'sumPrice': val},...
            ],
            'total': val
        }
        """
        self.detail = detail
        self.dv.data = detail['foodSelectedList']
        self.detail_text.text = 'Order: {} Table: {} Amount: {} php'.format(
            detail['queue'], detail['table'], detail['total'])

    def removeQueue(self):
        """reset value"""
        self.manager.get_screen('QueueAll').qv.data.remove(self.detail)
        self.dv.data = []
        self.detail_text.text = ''
        self.detail = {}

        """go to QueueAllScreen"""
        self.manager.transition.direction = 'right'
        self.manager.current = 'QueueAll'

    def saveToDb(self):
        """
        model detail
        {
            'queue': val,
            'table': val,
            'foodSelectedList': [
                {'foodName': val, 'foodOption': val, 'sumPrice': val},...
            ],
            'total': val
        }
        """

        genFoodId = str(uuid.uuid4())  # generate foodId for two files csv

        with open('data/db.csv', mode='a') as csvFile:
            fieldnames = ['date', 'foodId', 'total']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            # writer.writeheader()
            writer.writerow({'date': str(datetime.datetime.now()),
                             'foodId': genFoodId,
                             'total': self.detail['total']
                             })

        with open('data/foodDb.csv', mode='a') as csvFile:
            fieldnames = ['FoodId', 'FoodName', 'OptionName', 'Price']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            # writer.writeheader()

            for food in self.detail['foodSelectedList']:
                writer.writerow({'FoodId': genFoodId,  # generate unique id
                                 'FoodName': food['foodName'],
                                 'OptionName': food['foodOption'],
                                 'Price': food['sumPrice']
                                 })

        self.removeQueue()  # remove this queue from queue food


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behavior to the view. '''

class SelectableDetailQueueBoxLayout(RecycleDataViewBehavior, BoxLayout):

    def space(self, name, option):
        return ' ' * (30-len([i for i in (name+option) if i not in " data"]))


    
