# The main kivy code that is used

screen_helper = """
super_screen:
    ScreenManager:
        MainWindow:
        Library:
        BuildDeck:
        BuildCards:
        DeckOfCards:
        Cards:
        Review:
        

# Creates the window that slides after clicking the menu button
<ContentNavigationDrawer>:
    ScrollView:
        MDList:
            OneLineListItem:
                text: "Main Menu"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "main"
                    root.screen_manager.transition.direction = "left"

            OneLineListItem:
                text: "Library"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "library"
                    root.screen_manager.transition.direction = "left"

            OneLineListItem:
                text: "Build"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "build"
                    root.screen_manager.transition.direction = "left"
                    
            OneLineListItem:
                text: "Review"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "review"
                    root.screen_manager.transition.direction = "left"

# The screen the holds all screens in the app
<super_screen>:

# The top toolbar
# The names of each pathway to the specific class  
    NavigationLayout:
        x: toolbar.height
        
        ScreenManager:
            id: screen_manager
            
            MainWindow:
                name: "main"
                MDBoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Main"
                        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    MDLabel:
                        text: "hello"
                             
            Library:
                name: "library"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Library"
                        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                    #MDRectangleFlatButton:
                     #   text: "Button"
                      #  on_press: screen_manager.current = "cards"

                        #This button can potentially show searched decks?                        
                        left_action_items: [["magnify", lambda x: nav_drawer.set_state("open")]] 

                    Widget:
                    
                        # Changes the height of the buttons on bottom of screen               
                        #size_hint_y: None
                        #height: self.parent.height * 0.111
                        
                        #Button:
                         #   text: "Delete"
                        #Button:
                        #    text: "Build"
                        #Button:
                            #text: "Review"
                    
            DeckOfCards:
                name: "deck"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Deck"
                        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                        #This button can potentially show searched decks?                        
                        left_action_items: [["magnify", lambda x: nav_drawer.set_state("open")]]
                    Widget:
            
            BuildCards:
                name: "buildcard"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Build Card"
                        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                        #Might need to fix where the icon is on the bar                       
                        MDIconButton:
                            icon: "arrow-left"
                            pos_hint: {"center_x": 0.5, "center_y": .5}
                            theme_text_color: "Custom"
                            text_color: app.theme_cls.primary_color
                            on_press: 
                                screen_manager.current = "deck"
                                screen_manager.transition.direction = "right"
                    Widget:
                        
            Cards:
                name: "cards"
                BoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Cards"
                        right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                        #This button can potentially show searched decks?                        
                        left_action_items: [["content-save", lambda x: nav_drawer.set_state("open")]]  

                    Widget:
                    
                                                  
            BuildDeck:
                name: "build"
                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "Build"
                    right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
            
            Review:
                name: "review"
                MDToolbar:
                    id: toolbar
                    pos_hint: {"top": 1}
                    elevation: 10
                    title: "Review"
                    right_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                
                
        
        MDNavigationDrawer:
            id: nav_drawer

            # This will call on this class because of Object Properties from py code
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer

    
"""

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Flashcard App"
                        elevation: 10
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: "vertical"
                padding: 8
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Decks'
                            IconLeftWidget:
                                icon: "content-copy"
                        
                        OneLineIconListItem:
                            text: "Build deck"
                            IconLeftWidget:
                                icon: "hammer"
                        
                        OneLineIconListItem:
                            text: 'Review'
                            IconLeftWidget:
                                icon: "check"
                        
                        OneLineIconListItem:
                            text: 'Statistics'
                            IconLeftWidget:
                                icon: "chart-donut"
"""

working_screenmanager = """
<ContentNavigationDrawer>:

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Screen 1"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "Screen 2"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"



Screen:

    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            Screen:
                name: "scr 1"

                MDLabel:
                    text: "Screen 1"
                    halign: "center"

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
"""


