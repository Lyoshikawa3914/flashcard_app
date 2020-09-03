import kivymd

#creates the window to do stuff
from kivymd.app import MDApp
from kivy.core.window import Window
#loads the kv (kivy) file to make the app use kv file
from kivy.lang import Builder

from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout

from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.properties import ObjectProperty

#screen is the app screen
from kivymd.uix.screen import MDScreen
#allows app to use multiple windows/pages/screens
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

from screen_nav import screen_helper
from screen_nav import navigation_helper
from screen_nav import working_screenmanager


Window.size = (300, 500)

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class DecksWindow(Screen):
    def __init__(self, **kwargs):
        super(DecksWindow, self).__init__(**kwargs)

#Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.button0 = Button(text="Button")
        self.button0.bind(on_press=self.to_deckofcards)
        self.box.add_widget(self.button0)

#Buttons on the bottom of the screen
#Buttons are places on bottom of screen
        self.grid = GridLayout(cols=3,
                               size_hint_y=None,
                               height=int(Window.height)/8.9)
        self.button1 = Button(text="Delete")
        self.button2 = Button(text="Build")
        self.button3 = Button(text="Review")
        self.grid.add_widget(self.button1)
        self.grid.add_widget(self.button2)
        self.grid.add_widget(self.button3)
        self.box.add_widget(self.grid)
        self.add_widget(self.box)

# working code to switch screens with pyton code
    def to_deckofcards(self, instance):
        self.manager.current = "cards"

class DeckOfCards(Screen):
    def __init__(self, **kwargs):
        super(DeckOfCards, self).__init__(**kwargs)
        pass



class DeckCreation(Screen):
    def __init__(self, **kwargs):
        super(DeckCreation, self).__init__(**kwargs)


#creates button to enter Name of deck
        self.button = MDRectangleFlatButton(text="Enter",
                                            pos_hint={"center_x": 0.5, "center_y": 0.5})

        self.add_widget(self.button)

class CardCreation(Screen):
    pass

class Review(Screen):
    def __init__(self, **kwargs):
        super(Review, self).__init__(**kwargs)

        self.Label = MDLabel(text="review")
        self.add_widget(self.Label)




class super_screen(Screen):
# The main screen, holding all other screens
    def __init__(self, **kwargs):
        super(super_screen, self).__init__(**kwargs)



        # lists all the decks

        # creates a bottom toolbar for the whole app
"""
        self.bottom_AppToolbar = MDBottomAppBar()
        self.bottom_toolbar = MDToolbar(icon="plus",  # gives the icon an image
                                        type="bottom",
                                        # makes the circle button in the middle
                                        mode="center")


        self.bottom_AppToolbar.add_widget(self.bottom_toolbar)
        self.add_widget(self.bottom_AppToolbar)

        self.super_screen = self.add_widget(self.sm)

"""




class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()



#MyApp must inherit from App class that was imported
class MyApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == "__main__":
    main_app = MyApp()
    main_app.run()