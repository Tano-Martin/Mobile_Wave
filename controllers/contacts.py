from kivy.uix import scrollview
from kivymd.uix import boxlayout, label, textfield, list
from kivymd.utils import fitimage
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.app import MDApp


Builder.load_file("views/contacts.kv")

class ContactWidget(boxlayout.MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # fenetrePrincipale = boxlayout.MDBoxLayout(orientation='vertical', md_bg_color=(1, 1, 1, 1))
        # recherche = textfield.MDTextField(hint_text="A", pos_hint={'center_x': .5, 'center_y': .9}, size_hint_x=.9)
        # self.add_widget(fenetrePrincipale)
        # scroll = scrollview.ScrollView()
        # fenetrePrincipale.add_widget(recherche)
        # fenetrePrincipale.add_widget(scroll)
        
        # liste = list.MDList()
        # fenetreListe = boxlayout.MDBoxLayout(orientation='vertical', spacing=dp(10))
        
        # scroll.add_widget(liste)
        # liste.add_widget(fenetreListe)
        

        # fenetreContact = boxlayout.MDBoxLayout(orientation='vertical', spacing=dp(10))
        # labelContact = label.MDLabel(text='CONTACTS', padding_x=dp(30), font_style='Body2', color=(1,0,0))
        # fenetreListe.add_widget(labelContact)
        # fenetreListe.add_widget(fenetreContact)

        # iconeContact = fitimage.FitImage(source="asserts/account.png", size_hint_x=None, size_hint_y=None, width = dp(40), height = dp(40))
        # fenetreContact.add_widget(iconeContact)
        # self.spacing = dp(10)
        # nom = label.MDLabel(text='martin', bold=True)
        # self.add_widget(nom)
