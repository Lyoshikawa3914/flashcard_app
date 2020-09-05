import kivymd

#creates the window to do stuff
from kivymd.app import MDApp
from kivy.core.window import Window
#loads the kv (kivy) file to make the app use kv file
from kivy.lang import Builder

from kivymd.uix.textfield import MDTextField

from kivymd.uix.toolbar import MDToolbar, MDBottomAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout

#Allows for screen be able to scroll down or up
from kivy.uix.scrollview import ScrollView

#makes a nice looking list
from kivymd.uix.list import MDList, OneLineListItem

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
from kivymd.uix.button import MDRectangleFlatIconButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


from screen_nav import screen_helper
from screen_nav import navigation_helper
from screen_nav import working_screenmanager


Window.size = (300, 500)

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)


class Library(Screen):
    def __init__(self, **kwargs):
        super(Library, self).__init__(**kwargs)

#Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.scrollview = ScrollView()
        self.list = MDList()

# Creates a section that will list out the decks
        self.scrollview.add_widget(self.list)
        for i in range(21):
            items = OneLineListItem(text="Deck" + str(i))
            #each item on list will send user to deckofcard page on pressing
            items.bind(on_press=self.to_deckofcards)
            self.list.add_widget(items)

        self.box.add_widget(self.scrollview)



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

# working code to switch screens with python code
    def to_deckofcards(self, instance):
        self.manager.current = "deck"
        self.manager.transition.direction = "left"


class Build(Screen):
    def __init__(self, **kwargs):
        super(Build, self).__init__(**kwargs)


#creates button to enter Name of deck
        self.button = MDRectangleFlatButton(text="Enter",
                                            pos_hint={"center_x": 0.5, "center_y": 0.5})

        self.add_widget(self.button)

class CardCreation(Screen):
    def __init__(self, **kwargs):
        super(CardCreation, self).__init__(**kwargs)
        pass

class DeckOfCards(Screen):
    def __init__(self, **kwargs):
        super(DeckOfCards, self).__init__(**kwargs)

        # Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.scrollview = ScrollView()
        self.list = MDList()

        # Creates a section that will list out the decks
        self.scrollview.add_widget(self.list)
        for i in range(21):
            items = OneLineListItem(text="Card" + str(i))
            # each item on list will send user to deckofcard page on pressing
            items.bind(on_press=self.to_cards)
            self.list.add_widget(items)

        self.box.add_widget(self.scrollview)

        # Buttons on the bottom of the screen
        # Buttons are places on bottom of screen
        self.grid = GridLayout(cols=3,
                               size_hint_y=None,
                               height=int(Window.height) / 8.9)
        self.delete_btn = Button(text="Delete")

        self.build_btn = Button(text="Build")
        self.build_btn.bind(on_press=self.to_build_card)

        self.review_btn = Button(text="Review")

        self.grid.add_widget(self.delete_btn)
        self.grid.add_widget(self.build_btn)
        self.grid.add_widget(self.review_btn)
        self.box.add_widget(self.grid)
        self.add_widget(self.box)

        # working code to switch screens with python code

    def to_cards(self, instance):
        self.manager.current = "cards"
        self.manager.transition.direction = "left"

    def to_build_card(self, instance):
        self.manager.current = "buildcard"
        self.manager.transition.direction = "left"

class Cards(Screen):
    def __init__(self, **kwargs):
        super(Cards, self).__init__(**kwargs)
        pass

class BuildCards(Screen):
    def __init__(self, **kwargs):
        super(BuildCards, self).__init__(**kwargs)


        self.box = MDBoxLayout(orientation="vertical")
        self.input_front = MDTextField(text="Front: ",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(.5,1),
                                       )

        self.input_back = MDTextField(text="Back: ",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(.5,1))
        self.button = MDRectangleFlatButton(text="Enter",
                                            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.box.add_widget(self.input_front)
        self.box.add_widget(self.input_back)
        self.box.add_widget(self.button)

        #jargon of code to push the "front", "back", and "button" this screen up
        self.box.add_widget(Widget(size_hint_y=None,
                               height=int(Window.height) / 8.9))
        self.box.add_widget(Widget(size_hint_y=None,
                                   height=int(Window.height) / 8.9))
        self.box.add_widget(Widget(size_hint_y=None,
                                   height=int(Window.height) / 8.9))
        self.add_widget(self.box)

class BuildDeck(Screen):
    # This section will be a pop
    #asks user to input a name for the deck
    pass



class Review(Screen):
    def __init__(self, **kwargs):
        super(Review, self).__init__(**kwargs)

        self.Label = MDLabel(text="review")
        self.add_widget(self.Label)

        self.box = MDBoxLayout()
        self.grid = GridLayout(cols=3,
                               size_hint_y=None,
                               height=int(Window.height) / 8.9)
        self.fail_btn = Button(text="Fail")

        self.tag_btn = Button(text="Tag")
        #self.build_btn.bind(on_press=self.to_build_card)

        self.pass_btn = Button(text="Pass")

        self.grid.add_widget(self.fail_btn)
        self.grid.add_widget(self.tag_btn)
        self.grid.add_widget(self.pass_btn)
        self.box.add_widget(self.grid)
        self.add_widget(self.box)



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