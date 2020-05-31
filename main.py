
import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.event import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, DictProperty
from kivy.uix.image import Image

# other files
from src.StartScreen import StartScreen
from src.MenuScreen import MenuScreen
from src.QueueAllScreen import QueueAllScreen
from src.DetailQueueScreen import DetailQueueScreen
from src.Option import Option
from src.GenerateReport import GenerateReport

class StateScreen(ScreenManager):
    
    def __init__(self, **kwargs):
        super(StateScreen, self).__init__(**kwargs)
        startScreen = StartScreen(name='Start')
        self.add_widget(startScreen)
        menuScreen = MenuScreen(name='Menu') 
        self.add_widget(menuScreen)
        queueallScreen = QueueAllScreen(name='QueueAll')
        self.add_widget(queueallScreen)
        detailScreen = DetailQueueScreen(name='DetailQueue')
        self.add_widget(detailScreen)
        self.add_widget(Option(name='Option', startScreen=startScreen, menuScreen=menuScreen, queueallScreen=queueallScreen, detailScreen=detailScreen))
        generateReport = GenerateReport(name='Generate')
        self.add_widget(generateReport)

class MainApp(App):
    def build(self):
        return StateScreen()


if __name__ == '__main__':
    MainApp().run()
