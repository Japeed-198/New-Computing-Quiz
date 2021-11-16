import house as house
import kivy
import json
import requests
import pygame
import Global
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Canvas
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ListProperty, NumericProperty

pygame.init()

pygame.mixer.music.load('Quiz music.mp3')
pygame.mixer.music.play(-1)


class windowmanager(ScreenManager):
    pass

class MainMenu(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    pass

class firstquestion(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
    def add_one_counter(self):
        Global.questioncounter = Global.questioncounter + 1
    pass


class secondquestion(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
    def add_one_counter(self):
        Global.questioncounter = Global.questioncounter + 1
    pass

class thirdquestion(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
    def add_one_counter(self):
        Global.questioncounter = Global.questioncounter + 1
    pass

class fourthquestion(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
    def decide(self):
        if (Global.gryffindor == Global.hufflepuff):
            self.parent.current = 'GryHuf'
        elif (Global.gryffindor == Global.slytherin):
            self.parent.current = 'GrySly'
        elif (Global.gryffindor == Global.ravenclaw):
            self.parent.current = 'GryRav'
        elif (Global.hufflepuff == Global.gryffindor):
            self.parent.current = 'HufGry'
        elif (Global.hufflepuff == Global.slytherin):
            self.parent.current = 'HufSly'
        elif (Global.hufflepuff == Global.ravenclaw):
            self.parent.current = 'HufRav'
        elif (Global.ravenclaw == Global.hufflepuff):
            self.parent.current = 'RavHuf'
        elif (Global.ravenclaw == Global.slytherin):
            self.parent.current = 'RavSly'
        elif (Global.ravenclaw == Global.gryffindor):
            self.parent.current = 'RavGry'
        elif (Global.slytherin == Global.gryffindor):
            self.parent.current = 'SlyGry'
        elif (Global.slytherin == Global.hufflepuff):
            self.parent.current = 'SlyHuf'
        elif (Global.slytherin == Global.ravenclaw):
            self.parent.current = 'SlyRav'
        else:
            self.parent.current = 'Deciding'
    pass

class GryHuf(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
        self.parent.current = 'Deciding'
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
        self.parent.current = 'Deciding'
    pass

class GryRav(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
        self.parent.current = 'Deciding'
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
        self.parent.current = 'Deciding'
    pass

class GrySly(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
        self.parent.current = 'Deciding'
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
        self.parent.current = 'Deciding'
    pass

class HufGry(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
        self.parent.current = 'Deciding'
    def add_one_gry(self):
        Global.gryffindor = Global.gryffindor + 1
        self.parent.current = 'Deciding'
    pass

class HufSly(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
        self.parent.current = 'Deciding'
    def add_one_sly(self):
        Global.slytherin = Global.slytherin + 1
        self.parent.current = 'Deciding'
    pass

class HufRav(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    def add_one_huf(self):
        Global.hufflepuff = Global.hufflepuff + 1
        self.parent.current = 'Deciding'
    def add_one_rav(self):
        Global.ravenclaw = Global.ravenclaw + 1
        self.parent.current = 'Deciding'
    pass

class deciding(Screen):
    def decider(self):
        if (Global.gryffindor > Global.ravenclaw and Global.gryffindor > Global.slytherin and Global.gryffindor > Global.hufflepuff):
            self.parent.current = 'Gry_house'
        elif (Global.ravenclaw > Global.gryffindor and Global.ravenclaw > Global.slytherin and Global.ravenclaw > Global.hufflepuff):
            self.parent.current = 'Rav_house'
        elif (Global.hufflepuff > Global.gryffindor and Global.hufflepuff > Global.slytherin and Global.hufflepuff > Global.ravenclaw):
            self.parent.current = 'Huf_house'
        elif (Global.slytherin > Global.gryffindor and Global.slytherin > Global.hufflepuff and Global.slytherin > Global.ravenclaw):
            self.parent.current = 'Sly_house'
    pass

class StartButton(ButtonBehavior, Image):
    pass

class Title(Image):
    pass

class question1(Image):
    pass

class question2(Image):
    pass

class question3(Image):
    pass

class question4(Image):
    pass

class Answer1(ButtonBehavior, Image):
    pass

class TheGreat(ButtonBehavior ,Image):
    pass

class TheWise(ButtonBehavior, Image):
    pass

class TheBold(ButtonBehavior, Image):
    pass

class Dawn(ButtonBehavior, Image):
    pass

class Dusk(ButtonBehavior, Image):
    pass

class Violin(ButtonBehavior, Image):
    pass

class Piano(ButtonBehavior, Image):
    pass

class Trumpet(ButtonBehavior, Image):
    pass

class Drum(ButtonBehavior, Image):
    pass


class Huf(ButtonBehavior, Image):
    pass

class Sly(ButtonBehavior, Image):
    pass

class Gry(ButtonBehavior, Image):
    pass

class Rav(ButtonBehavior, Image):
    pass

class Left(ButtonBehavior, Image):
    pass

class Right(ButtonBehavior, Image):
    pass

class Gry_house(Screen):
    pass

class Rav_house(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    pass

class Huf_house(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    pass

class Sly_house(Screen):
    def transition_effect(self):
        sound = SoundLoader.load('Transition.mp3')
        if sound:
            sound.play()
    pass

class Click(Image):
    pass

class TheButton(ButtonBehavior, Image):
    pass

class grymotto(Image):
    pass


class MyMainApp(App):
    def build(self):
        kv = Builder.load_file("my.kv")
        return kv


if __name__ == "__main__":
    MyMainApp().run()