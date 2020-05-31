from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
# import csv

kv ="""
<StartScreen>:
    color_r: 0
    color_g: 0.8
    color_b: 0.9

  
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: root.color_r, root.color_g, root.color_b ,6
            Rectangle:
                size: self.size
                pos: self.pos
                source: "Pictures/Waiter.png"
           

##        Image:
##            source: "Pictures/Title.png"
##            size: 500,500
##
##        Label:
##            text: "CPE RESTAURANT ORDERING SYSTEM"
##            font_size: 40
##            pos: 200,300
##
##        BoxLayout:
##            orientation: 'vertical'
##            size_hint_y: None
##            height: dp(120)
##            Label:
##                font_name: 'font/THSarabunNew Bold.ttf'
##                font_size: '50sp'
##                text:'CPE RESTAURANT ORDERING SYSTEM'
        BoxLayout:
            orientation: 'vertical'
            height: dp(270)
            size_hint_y: None
            padding: 0,0,0,dp(20)
            Image
                source: 'Pictures/TITLE (2).png'
            
        
        GridLayout:
            cols: 1
            padding: dp(134),0,dp(180),dp(30) #tsek
            spacing: dp(30) #nilagayan ng bago
            height: dp(300)
            
            Button:
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '25sp'
                text: '       Menu        '
                size_hint_x: None
                size: self.texture_size
                background_normal: 'Pictures/main1.png'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'Menu'
                
            Button:
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '25sp'
                text: '       Order        '
                size_hint_x: None
                size: self.texture_size
                background_normal: 'Pictures/main1.png'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'QueueAll'

            Button:
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '25sp'
                text: ' Generate Report'
                size_hint_x: None
                size: self.texture_size
                background_normal: 'Pictures/main1.png'
                on_press: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'Generate'


            Button:
                font_name: 'font/THSarabunNew Bold.ttf'
                font_size: '25sp'
                text: '         Exit         '
                size_hint_x: None
                size: self.texture_size
                background_normal: 'Pictures/main1.png'
                on_press: 
                    root.destroy()
     
           
       
        
 """           

Builder.load_string(kv)

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super(StartScreen,self).__init__(**kwargs)
