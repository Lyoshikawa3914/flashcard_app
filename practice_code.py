import kivymd
import sqlite3

#creates the window to do stuff
from kivymd.app import MDApp
from kivy.core.window import Window
#loads the kv (kivy) file to make the app use kv file
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
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
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import ObjectProperty
#screen is the app screen
from kivymd.uix.screen import MDScreen
#allows app to use multiple windows/pages/screens
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatIconButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, \
    MDFlatButton
from screen_nav import screen_helper
from screen_nav import navigation_helper
from screen_nav import working_screenmanager


Window.size = (300, 500)

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        #creates the database, if the file already exists, it will auto connect
        conn = sqlite3.connect('flashcard_app.db')
        cur = conn.cursor()

        # Creates database if it doesn't exists
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Cards(
                RowID INTEGER PRIMARY KEY AUTOINCREMENT,
                CardName CHAR(25), 
                Definition CHAR(500),
                DeckName CHAR(25)
                )
        """)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Decks(
                RowID INTEGER PRIMARY KEY AUTOINCREMENT,
                DeckName CHAR(25),
                FOREIGN KEY(DeckName) REFERENCES Card(DeckName)
                )
                """)
        conn.commit()
        conn.close()


class Library(Screen):
    def __init__(self, **kwargs):
        super(Library, self).__init__(**kwargs)
        self.deckname = None
        self.skeleton_frame()

    def skeleton_frame(self):
        #Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.scrollview = ScrollView()
        self.list = MDList()
        self.scrollview.add_widget(self.list)

        #calls the activate_for_loop method
        self.display_deck()

        # Buttons on the bottom of the screen
        # Buttons are places on bottom of screen
        self.box.add_widget(MDLabel(size_hint=(0.2,0.15))) # Push down the list of buttons
        self.box.add_widget(self.scrollview)

        self.bottom_bar = MDToolbar()
        self.delete_deck_button = MDIconButton(icon="trash-can-outline",
                                               pos_hint={'center_x': .5, 'center_y': .5})
        self.delete_deck_button.bind(on_press=self.delete_deck)
        self.build_deck_button = MDIconButton(icon="plus-thick",
                                              pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                              )
        self.build_deck_button.bind(on_press=self.build_new_deck)

        #add method to make a new deck
        self.bottom_bar.add_widget(self.delete_deck_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.build_deck_button)
        self.bottom_bar.add_widget(MDLabel())
        self.box.add_widget(self.bottom_bar)
        self.add_widget(self.box)

    def skeleton_frame2(self, instance):
        # method must be used to make the on_press method work
        self.scrollview.remove_widget(self.list)
        self.box.remove_widget(self.bottom_bar)
        self.list = MDList()
        self.scrollview.add_widget(self.list)

        #Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.scrollview = ScrollView()
        self.list = MDList()
        self.scrollview.add_widget(self.list)

        #calls the activate_for_loop method
        self.display_deck()

        # Buttons on the bottom of the screen
        # Buttons are places on bottom of screen
        self.box.add_widget(MDLabel(size_hint=(0.2,0.15))) # Push down the list of buttons
        self.box.add_widget(self.scrollview)

        self.bottom_bar = MDToolbar()
        self.delete_deck_button = MDIconButton(icon="trash-can-outline",
                                               pos_hint={'center_x': .5, 'center_y': .5})
        self.delete_deck_button.bind(on_press=self.delete_deck)
        self.build_deck_button = MDIconButton(icon="plus-thick",
                                              pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                              )
        self.build_deck_button.bind(on_press=self.build_new_deck)

        #add method to make a new deck
        self.bottom_bar.add_widget(self.delete_deck_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.build_deck_button)
        self.bottom_bar.add_widget(MDLabel())
        self.box.add_widget(self.bottom_bar)
        self.add_widget(self.box)

# Creates a section that will list out the decks
    def display_deck(self):
        conn = sqlite3.connect("flashcard_app.db")
        cur = conn.cursor()
        cur.execute("""
        SELECT DeckName 
        FROM Decks
        """)
        names = cur.fetchall()
        for name in names:
            # the nested for loop will remove (),' from the string
            name = str(name)
            for char in name:
                if char == "(" or char == ")" or char =="," or char == "'":
                    name = name.replace(char, "")
            self.items = OneLineListItem(text=name)
            self.items.bind(on_press=self.display_cards)
            self.list.add_widget(self.items)
        conn.commit()
        conn.close()

# working code to switch screens with python code
    def display_cards(self, instance):
        self.scrollview.remove_widget(self.list)
        self.box.remove_widget(self.bottom_bar)
        self.list = MDList()
        self.scrollview.add_widget(self.list)
        self.deckname = instance.text
        print(self.deckname)
        conn = sqlite3.connect("flashcard_app.db")
        cur = conn.cursor()
        cur.execute("""
                SELECT CardName 
                FROM Cards
                WHERE DeckName = ?
                """, (instance.text,))
        names = cur.fetchall()
        for name in names:
            # the nested for loop will remove (),' from the string
            name = str(name)
            for char in name:
                if char == "(" or char == ")" or char == "," or char == "'":
                    name = name.replace(char, "")
            self.items = OneLineListItem(text=name)
            self.items.bind(on_press=self.display_name_def)
            self.list.add_widget(self.items)
        conn.commit()
        conn.close()
        self.get_bottom_bar()

    def display_cards2(self):
        self.scrollview.remove_widget(self.list)
        self.box.remove_widget(self.bottom_bar)
        self.list = MDList()
        self.scrollview.add_widget(self.list)
        conn = sqlite3.connect("flashcard_app.db")
        cur = conn.cursor()
        cur.execute("""
                SELECT CardName 
                FROM Cards
                WHERE DeckName = ?
                """, (self.deckname,))
        names = cur.fetchall()
        for name in names:
            # the nested for loop will remove (),' from the string
            name = str(name)
            for char in name:
                if char == "(" or char == ")" or char == "," or char == "'":
                    name = name.replace(char, "")
            self.items = OneLineListItem(text=name)
            self.items.bind(on_press=self.display_name_def)
            self.list.add_widget(self.items)
        conn.commit()
        conn.close()
        self.get_bottom_bar()

#displays the bottom nav bar when display_cards is called
    def get_bottom_bar(self):
        self.bottom_bar = MDToolbar()
        self.add_card_button = MDIconButton(icon="plus-thick",
                                              pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                              )
        self.trash_button = MDIconButton(icon="trash-can-outline",
                                         pos_hint ={'center_x': 0.5, 'center_y': 0.5}
                                         )
        self.review_button = MDIconButton(icon="check-outline",
                                          pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                          )

        self.back_button = MDIconButton(icon="arrow-left-bold",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.trash_button.bind(on_press=self.delete_card)
        self.back_button.bind(on_press=self.skeleton_frame2)
        self.add_card_button.bind(on_press=self.add_cards)
        #self.build_deck_button.bind(on_press=self.to_build_card)

        # jargon of code to space out the buttons on bottom nav bar
        self.bottom_bar.add_widget(self.back_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.trash_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.add_card_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.review_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.box.add_widget(self.bottom_bar)

    def add_cards(self, instance):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        enter_button = MDFlatButton(text="Enter", on_release=self.add_cardname_to_db)

        self.grid = MDGridLayout(rows=4,
                                 size_hint_y=None,
                                 height=int(Window.height) / 8.9
                                 )
        self.front_input = MDTextField(
                                 size_hint=(.9,1))
        self.back_input = MDTextField(
                                 size_hint=(.9,1))

        self.dialog = MDDialog(title="Card Creation",
                                pos_hint={'center_x':.5, 'center_y':.5},
                               type="custom",
                               content_cls=Content(),
                                size_hint=(.9,1),

                                buttons=[close_button, enter_button])
        self.grid.add_widget(MDLabel(text="  Front"))
        self.grid.add_widget(self.front_input)
        self.grid.add_widget(MDLabel(text="  Back"))
        self.grid.add_widget(self.back_input)
        self.dialog.add_widget(self.grid)
        self.dialog.open()

    def add_cardname_to_db(self, instance):
        front_input = self.front_input.text
        back_input = self.back_input.text

        print(self.deckname)
        print(front_input)
        print(back_input)

        con = sqlite3.connect("flashcard_app.db")
        cur = con.cursor()
        cur.execute("""
        INSERT INTO Cards (CardName, Definition, DeckName)
        VALUES(?, ?, ?)
        """, (front_input, back_input, self.deckname))
        names = cur.fetchall()
        for name in names:
            # the nested for loop will remove (),' from the string
            name = str(name)
            for char in name:
                if char == "(" or char == ")" or char == "," or char == "'":
                    name = name.replace(char, "")
            self.items = OneLineListItem(text=name)
            #self.items.bind(on_press=self.display_name_def)
            self.list.add_widget(self.items)
        con.commit()
        con.close()
        self.display_cards2()

###########################################################
    def display_name_def(self, instance):
        #displays the front and back of a single card
        self.scrollview.remove_widget(self.list)
        self.box.remove_widget(self.bottom_bar)

        # will display the front-side of selected card
        self.button = Button(text=str(self.items.text),
                             color=(1,0,1,1),
                             background_color=(0,0,0,0))
        self.scrollview.add_widget(self.button)
        self.bottom_bar_name_def()

    def bottom_bar_name_def(self):
        self.bottom_bar = MDToolbar()
        #self.box = MDBoxLayout(orientation="horizontal")
        self.back_button = MDFlatButton(text="Return to Decks",
                                        pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.back_button.bind(on_press=self.back_display_cards)
        #self.box.add_widget(self.back_button)
        #self.box.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.back_button)
        self.add_widget(self.bottom_bar)

    def back_display_cards(self, instance):
        self.box.remove_widget(self.scrollview)
        self.remove_widget(self.bottom_bar)
        self.skeleton_frame()
####################################################################

# method to build a new deck using a dialog box
    def build_new_deck(self, instance):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)

# *** This button will put name into db, then refresh the page
        enter_button = MDFlatButton(text="Enter", on_release=self.add_name_to_db)
        self.input = MDTextField(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(.9,1))
        self.dialog = MDDialog(title="Enter Deck Name",
                          size_hint=(0.7, 1),
                          buttons=[close_button, enter_button])
        self.dialog.add_widget(self.input)
        self.dialog.open()

# method to close the dialog box
    def close_dialog(self, instance):
        self.dialog.dismiss()

#method that inserts the deck name into db
    def add_name_to_db(self, instance):
        input = self.input.text

        # this will have an if else statement if an error was typed in
        #self.error = MDDialog()
        #self.error.open()
        conn = sqlite3.connect("flashcard_app.db")
        cur = conn.cursor()
        cur.execute("""
                INSERT INTO Decks (deckname)
                VALUES(?)""",
                    (input,)
        )
        conn.commit()
        conn.close()
        self.remove_widget(self.box)
        self.skeleton_frame()
        print("boo")

    def delete_deck(self, instance):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        delete_dialog_button = MDFlatButton(text="Delete", on_release=self.delete_deck_input)
        self.dialog = MDDialog(title="Delete Deck",
                                          size_hint=(0.7, 1),
                                          buttons=[close_button, delete_dialog_button]
                                          )
        self.input = MDTextField()
        self.dialog.add_widget(self.input)
        self.dialog.open()

    def delete_deck_input(self, instance):
        input = self.input.text

        con = sqlite3.connect("flashcard_app.db")
        cur = con.cursor()
        cur.execute("""
        DELETE FROM Decks
        WHERE DeckName = ?;
        """, (input,))

        cur.execute("""
        DELETE FROM Cards
        WHERE DeckName = ?;
        """, (input,))
        con.commit()
        con.close()
        self.remove_widget(self.box)
        self.skeleton_frame()

    def delete_card(self, instance):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        delete_dialog_button = MDFlatButton(text="Delete", on_release=self.delete_card_input)
        self.dialog = MDDialog(title="Delete Card",
                               size_hint=(0.7, 1),
                               buttons=[close_button, delete_dialog_button]
                               )
        self.input = MDTextField()
        self.dialog.add_widget(self.input)
        self.dialog.open()

    def delete_card_input(self, instance):
        input = self.input.text

        con = sqlite3.connect("flashcard_app.db")
        cur = con.cursor()
        cur.execute("""
        DELETE FROM Cards
        WHERE CardName = ?
        """, (input,))
        con.commit()
        con.close()
        self.display_cards2()

################################################################################
class Build(Screen):
    def __init__(self, **kwargs):
        super(Build, self).__init__(**kwargs)


#creates button to enter Name of deck
        self.button = MDRectangleFlatButton(text="Enter",
                                            pos_hint={"center_x": 0.5, "center_y": 0.5})

        self.add_widget(self.button)

class CardCreation(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class DeckOfCards(Library):
    def __init__(self, **kwargs):
        # ?
        super().__init__(**kwargs)


        self.deckofcards_toolbar_frame()

    def deckofcards_toolbar_frame(self):
        # Displays all decks on the app
        self.box = MDBoxLayout(orientation="vertical")
        self.scrollview = ScrollView()
        self.list = MDList()


        # Creates a section that will list out the decks
        self.scrollview.add_widget(self.list)
        self.box.add_widget(MDLabel(size_hint=(0.2, 0.2)))

        #this section will access database to get the name of the card
        """
         for i in range(21):
            items = OneLineListItem(text="Card " + str(i))
            # each item on list will send user to deckofcard page on pressing
            items.bind(on_press=self.to_cards)
            self.list.add_widget(items)

        """

        self.box.add_widget(self.scrollview)

        # Buttons on the bottom of the screen
        # Buttons are places on bottom of screen
        self.bottom_bar = MDToolbar()
        self.build_deck_button = MDIconButton(icon="plus-thick",
                                              pos_hint={'center_x':0.5, 'center_y':0.5}
        )
        self.trash_button = MDIconButton(icon="trash-can-outline",
                                              pos_hint={'center_x':0.5, 'center_y':0.5}
                                         )
        self.review_button = MDIconButton(icon="check-outline",
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                         )
        self.back_button = MDIconButton(icon="arrow-left-bold",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.build_deck_button.bind(on_press=self.to_build_card)

#jargon of code to space out the buttons on bottom nav bar
        self.bottom_bar.add_widget(self.back_button)
        #self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.trash_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.build_deck_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(self.review_button)
        self.bottom_bar.add_widget(MDLabel())
        self.bottom_bar.add_widget(MDLabel())
        #self.bottom_bar.add_widget(MDLabel())
        self.box.add_widget(self.bottom_bar)
        self.add_widget(self.box)

        # working code to switch screens with python code

    def to_cards(self, instance):
        self.manager.current = "card"
        self.manager.transition.direction = "left"

    def to_build_card(self, instance):
        self.manager.current = "buildcard"
        self.manager.transition.direction = "left"

# the instance from the Library.to_deckofcards will move to here




class Card(Screen):
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)

        #access database, get the card definition from the name of the card
        self.box = MDBoxLayout(orientation="vertical")
        self.front = MDLabel(text="Front: ",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(.5, 1),
                                       )

        self.back = MDLabel(text="Back: ",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(.5, 1))


        self.box.add_widget(self.front)
        self.box.add_widget(self.back)


        self.add_widget(self.box)

class BuildCards(Screen):
    def __init__(self, **kwargs):
        super(BuildCards, self).__init__(**kwargs)
        self.deck_name = ""

        self.skeleton_frame()

    def skeleton_frame(self):
        self.box = MDBoxLayout(orientation="vertical")
        self.front_label = MDLabel(text="Front",
                                   halign="center",
                                   valign="middle")
        self.back_label = MDLabel(text="Back",
                                  halign="center",
                                  valign="middle")
        self.input_front = MDTextField(hint_text="Front: ",
                                       pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(.5,1)
                                       )

        self.input_back = MDTextField(hint_text="Back: ",
                                      pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                      size_hint=(.5,1))
        self.button = MDRectangleFlatButton(text="Enter",
                                            pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.button.bind(on_press=self.insert_into_db)
        self.box.add_widget(self.front_label)
        self.box.add_widget(self.input_front)
        self.box.add_widget(self.back_label)
        self.box.add_widget(self.input_back)
        self.box.add_widget(self.button)

        self.add_widget(self.box)


    def insert_into_db(self, instance):
        front = self.input_front.text
        back = self.input_back.text

        con = sqlite3.connect("flashcard_app.db")
        cur = con.cursor()
        cur.execute("""
                INSERT INTO Cards(CardName, Definition) VALUES(?,?)""",
                    (front, back)
                    )
        con.commit()
        con.close()



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

class Content(BoxLayout):
    pass

class super_screen(Screen):
# The main screen, holding all other screens
    def __init__(self, **kwargs):
        super(super_screen, self).__init__(**kwargs)



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