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
          
            
    foodName: ''
    foodOption: ''
    sumPrice: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '15sp'
        text: '{} {} {} {} php'.format(root.foodName, root.foodOption, root.space(root.foodName,root.foodOption), root.sumPrice)
        size_hint_x: None
        size: self.texture_size

# listview info food
<SelectableFoodBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (.5, .5, .5, 1)
        Rectangle:
            size: self.size
            pos: self.pos

        
    name: ''
    price: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '15sp'
        text: '{}{}{}php'.format(root.name, root.space(root.name), root.price)
        size_hint_x: None
        size: self.texture_size

# listview info option
<SelectableOptionBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (.5, .5, .5, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    name: ''
    price: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '15sp'
        text: '{} {} {} php'.format(root.name, root.space(root.name), root.price)
        size_hint_x: None
        size: self.texture_size
<MenuScreen>:
    rv: rv
    fv: fv
    ov: ov
    color_r: 0
    color_g: 0.8
    color_b: 0.9
    r: 1
    g: 0.5
    b: 0.5
    tb_input: tb_input
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
##            orientation:'vertical'
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
                text: 'Available Food'
                color: 1,1,1,1
                bold: True
                font_size: '17sp'
            BoxLayout:
                spacing: dp(4)
                padding: dp(20),0,0,0
                Label:
                    text: 'Enter Table'
                    color: 1,1,1,1
                    bold: True
                    font_size: '17sp'
                TextInput:
                    id: tb_input
                    size_hint_x: 0.2
                    hint_text: 'value'
                    padding: dp(6), dp(12), 0, 0
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
                    viewclass: 'SelectableFoodBoxLayout'
                    SelectableRecycleBoxLayout:
                        default_size: None, dp(35)
                        default_size_hint: 1,None
                        size_hint_y: None
                        height: self.minimum_height
                        orientation: 'vertical'
                        multiselect: False
                        touch_multiselect: False          
                        spacing: dp(2)
                        padding: dp(10), dp(10), dp(10), 0
                BoxLayout:
                    size_hint_y: None
                    padding: 0,dp(10),dp(10),0
                    Image:
                        source: "Pictures/Serve1.png"
                    Label:
                        text: 'Option'
                        color: 1,1,1,1
                        bold: True
                        font_size: '17sp'
                    Image:
                        source: "Pictures/Serve2.png"
                OV:
                    id: ov
                    scroll_type: ['bars', 'content']
                    scroll_wheel_distance: dp(114)
                    bar_width: dp(10)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0.09
                        Rectangle:
                            size: self.size
                            pos: self.pos              
                    viewclass: 'SelectableOptionBoxLayout'
                                
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
                cols: 1
                BoxLayout:
                    size_hint_y: None
                    padding: 0,0,0,dp(10)
                    spacing: dp(8)
                    Button:
                        text: 'Add'
                        on_press: root.addFood()
                        font_size: '17sp'
                    Button:
                        text: 'Delete'
                        on_press: root.delAddFood()
                        font_size: '17sp'                       
                RV:
                    id: rv
                    scroll_type: ['bars', 'content']
                    scroll_wheel_distance: dp(114)
                    bar_width: dp(10)
                    canvas.before:
##                        Color:
##                            rgba: 0, 0, 0, 0.09
                        Rectangle:
                            size: self.size
                            pos: self.pos
                            source: "Pictures/Restaurant Menu.png"
                    viewclass: 'SelectableFoodOptionBoxLayout'
                                
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
                BoxLayout:
                    size_hint_y: None
                    padding: 0, dp(10), 0, 0
                    Button:
                        text: 'Accept'
                        on_press:
                            root.acceptMenu(tb_input.text)
                        font_size: '17sp'
                
"""

Builder.load_string(kv)

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        with open("data/food.csv", 'r', encoding='utf8') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.fv.data.append(dict(row))
                
        with open("data/option.csv", 'r', encoding='utf8') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                self.ov.data.append(dict(row))

    def addFood(self):
        food = self.fv.select
        option = self.ov.select

        """
        model food, option
        {
            'name': val,
            'price': val
        }
        """

        if food == {}:
            return

        foodOptionSelected = {
            'foodName': food['name'],
            'foodOption': option['name'] if option != {} and option['name'] != '-' else '',
            'sumPrice': str(int(food['price'])+int(option['price'])) if option != {} else food['price']
        }

        self.rv.data.append(foodOptionSelected)


    def delAddFood(self):
        # remove food with selected
        foodOptionSelected = self.rv.select
        if foodOptionSelected == {}:
            return

        self.rv.data.remove(foodOptionSelected)

    def acceptMenu(self, tb):
        # accept menu
        if self.rv.data == [] or tb == '':
            return
        """
        model menuSelected
        {
            'table': val,
            'foodName': val,
            'foodOption': val,
            'sumPrice': val
        }
        """
        menuSelected = {
            'table': tb,
            'foodSelectedList': self.rv.data,
            'total': str(sum([int(i['sumPrice']) for i in self.rv.data]))
        }

        """reset value"""
        self.rv.data = []
        self.tb_input.text = ''

        self.manager.get_screen('QueueAll').addQueue(menuSelected)

        """go to QueueAll"""
        self.manager.transition.direction = 'left'
        self.manager.current = 'QueueAll'


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behavior to the view. '''


class SelectableFoodBoxLayout(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableFoodBoxLayout, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableFoodBoxLayout, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            rv.select = rv.data[index]

    def space(self, name):
        """Leave the space equal"""
        return ' ' * (30-len([i for i in name if i not in " awks "]))


class SelectableOptionBoxLayout(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableOptionBoxLayout, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableOptionBoxLayout, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            rv.select = rv.data[index]

    def space(self, option):
        """Leave the space equal"""
        return ' ' * (30-len([i for i in option if i not in " awks "]))


class SelectableFoodOptionBoxLayout(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableFoodOptionBoxLayout, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableFoodOptionBoxLayout, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            rv.select = rv.data[index]

    def space(self, name, option):
        """Leave the space equal"""
        return ' ' * (30-len([i for i in (name+option) if i not in " awks "]))


class FV(RecycleView):
    select = DictProperty()

    def __init__(self, **kwargs):
        super(FV, self).__init__(**kwargs)


class OV(RecycleView):
    select = DictProperty()

    def __init__(self, **kwargs):
        super(OV, self).__init__(**kwargs)


class RV(RecycleView):
    select = DictProperty()

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
