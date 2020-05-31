from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty, DictProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

# from src.DetailQueueScreen import DetailQueueScreen

kv = """
# listview all queue
<SelectableQueueAllBoxLayout>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (.5, .5, .5, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    queue: ''
    table: ''
    Label:
        font_name: 'font/THSarabunNew Bold.ttf'
        font_size: '20sp'
        text: 'Order: {} Table;: {}          Click,Select'.format(root.queue, root.table)
        size_hint_x: None
        size: self.texture_size
<QueueAllScreen>:
    qv: qv
    color_r: 0
    color_g: 0.8
    color_b: 0.9
    r: 1
    g: 0.5
    b: 0.5
    BoxLayout: 
        canvas:
            Color:
                rgba: root.color_r, root.color_g, root.color_b, 1
            Rectangle:
                size: self.size
                pos: self.pos
                source:"Pictures/Waiter.png"

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
                        root.manager.current = 'Menu'
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
                text: 'Orders'
                color: 1,1,1,1
                bold: True
                font_size: '30sp'
        BoxLayout:
            orientation: 'vertical'
            padding: dp(50),0,dp(50),0     
            RV:
                id: qv
                scroll_type: ['bars', 'content']
                scroll_wheel_distance: dp(114)
                bar_width: dp(10)   
                canvas.before:
##                    Color:
##                        rgba: 0, 0, 0, 0.09
                    Rectangle:
                        size: self.size
                        pos: self.pos
                        source: "Pictures/plate.png"
                viewclass: 'SelectableQueueAllBoxLayout'
                    
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
            orientation: 'vertical'
            padding: dp(50),dp(10),dp(50),dp(50)
            size_hint_y: None
            height: dp(120)
            Button:
                text: 'Select'
                on_press : root.select()
                font_size: '24sp'
"""

Builder.load_string(kv)

class QueueAllScreen(Screen):
    queueNumber = []

    def __init__(self, **kwargs):
        super(QueueAllScreen, self).__init__(**kwargs)

    def addQueue(self, menuSelected):
        menuSelected['queue'] = str(len(self.queueNumber)+1)
        """
        model menuSelected
        {
            'queue': val,
            'table': val,
            'foodSelectedList': [
                {'foodName': val, 'foodOption': val, 'sumPrice': val},...
            ],
            'total': val
        }
        """
        self.qv.data.append(menuSelected)
        self.queueNumber.append(None)

    
    def getDetailQueue(self, queue):
        self.manager.get_screen('DetailQueue').getDetail(queue)
        self.manager.transition.direction = 'left'
        self.manager.current = 'DetailQueue'

    def select(self):
        result = self.qv.select
        if result == {}:
            return
        self.manager.get_screen('DetailQueue').getDetail(result)
        self.manager.transition.direction = 'left'
        self.manager.current = 'DetailQueue'


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behavior to the view. '''

class SelectableQueueAllBoxLayout(RecycleDataViewBehavior, BoxLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableQueueAllBoxLayout, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableQueueAllBoxLayout, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            rv.select = rv.data[index]


class RV(RecycleView):
    select = DictProperty()
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
