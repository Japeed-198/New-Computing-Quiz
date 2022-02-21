import pygame 
import Global
import csv
import pandas as pd
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
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
from kivy.properties import ObjectProperty
import random
pygame.init()

pygame.mixer.music.load('quiz music.mp3')
pygame.mixer.music.play(-1)
with open('users.csv', newline='') as userfile:
    reader = csv.reader(userfile)

with open('question.csv', newline='') as questionfile:
    reader2 = csv.reader(questionfile)
    
df = pd.read_csv('users.csv', sep=',')
questiondf = pd.read_csv('question.csv', sep=',')

class windowmanager(ScreenManager):
    pass

class MainMenu(Screen):
    pass

class Login_Screen(Screen):
    user = ObjectProperty(None)
    password = ObjectProperty(None)
    label = ObjectProperty(None)
    login_button = ObjectProperty(None)
    def login(self):
        df = pd.read_csv('users.csv', sep=',')
        attempt_username = self.ids.user.text   
        attempt_password = self.ids.password.text

        if attempt_username in df['Username'].tolist():
          password_df = df.set_index("Username", drop=False)
          if attempt_password == password_df.loc[attempt_username, 'Password']:
            self.ids.label.text = f'Welcome {attempt_username}'
            Global.player_username = attempt_username
            Global.player_password = attempt_password
            def question_creater():
                Global.random_row = questiondf.sample(n = 10)
                return Global.random_row
            print(question_creater())
            self.ids.login_button.text = f'Continue'
            self.ids.login_button.bind(on_press = self.quiz_start)
            
     
          else:
            self.ids.label.text = f'Incorrect'

        else:
            self.ids.label.text = f'Incorrect'
    def quiz_start(self, instance):
        self.parent.current = 'Mode'
    def clear(self):
        pass

class Register_Screen(Screen):
    register_user = ObjectProperty(None)
    register_password = ObjectProperty(None)
    register_label = ObjectProperty(None)
    register_button = ObjectProperty(None)
    def register(self):
        register_username = self.ids.register_user.text   
        register_password = self.ids.register_password.text

        if register_username in df['Username'].tolist():
            self.ids.register_label.text = f'Username already exists. Try again'
        else:
            if len(register_password) >= 8:
                with open('users.csv', 'a', newline='') as userfile:
                    writer = csv.writer(userfile)
                    writer.writerow([register_username, register_password, 0, 0])
                self.ids.register_label.text = f'Welcome {register_username}'
                self.ids.register_button.text = f'Go to login'
                self.ids.register_button.bind(on_press = self.go_login)
                 
            else:
                self.ids.register_label.text = f'Password must be more than 8 characters'
        

    def go_login(self, instance):
        self.parent.current = 'Login'
    def clear(self):
        pass

class mode(Screen):
    easy = ObjectProperty(None)
    hard = ObjectProperty(None)
    def easy_mode(self):
        Global.score_counter = 0
        Global.normal_mode = True
        self.parent.current = 'First'
    def hard_mode(self):
        Global.score_counter = 0
        Global.hard_mode = True
        self.parent.current = 'First'

class firstquestion(Screen): 
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_1 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_enter(self):
        Global.score_counter = 0
        print(Global.question_counter)
        self.chooser()
    
    def chooser(self): 
        self.ids.question_1.text = f'Question 1: {Global.random_row.iloc[0, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[0, options_list[0]]
        second_choice = Global.random_row.iloc[0, options_list[1]]
        third_choice = Global.random_row.iloc[0, options_list[2]]
        fourth_choice = Global.random_row.iloc[0, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_press =lambda x:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_press =lambda x:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_press =lambda x:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_press =lambda x:self.correct_answer_checker(self.ids.option_4))
    
    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Second"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Second"
                self.parent.current = 'Incorrect'
        elif Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Second"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Second"
                self.parent.current = 'Incorrect'

class secondquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_2 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self): 
        
        self.ids.question_2.text = f'Question 2: {Global.random_row.iloc[1, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[1, options_list[0]]
        second_choice = Global.random_row.iloc[1, options_list[1]]
        third_choice = Global.random_row.iloc[1, options_list[2]]
        fourth_choice = Global.random_row.iloc[1, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Third"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Third"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Third"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Third"
                self.parent.current = 'Incorrect'
    


class thirdquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_3 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_3.text = f'Question 3: {Global.random_row.iloc[2, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[2, options_list[0]]
        second_choice = Global.random_row.iloc[2, options_list[1]]
        third_choice = Global.random_row.iloc[2, options_list[2]]
        fourth_choice = Global.random_row.iloc[2, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Fourth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Fourth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Fourth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Fourth"
                self.parent.current = 'Incorrect'

class fourthquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_4 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_4.text = f'Question 4: {Global.random_row.iloc[3, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[3, options_list[0]]
        second_choice = Global.random_row.iloc[3, options_list[1]]
        third_choice = Global.random_row.iloc[3, options_list[2]]
        fourth_choice = Global.random_row.iloc[3, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Fifth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Fifth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Fifth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Fifth"
                self.parent.current = 'Incorrect'

class fifthquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_5 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_5.text = f'Question 5: {Global.random_row.iloc[4, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[4, options_list[0]]
        second_choice = Global.random_row.iloc[4, options_list[1]]
        third_choice = Global.random_row.iloc[4, options_list[2]]
        fourth_choice = Global.random_row.iloc[4, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Sixth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Sixth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Sixth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Sixth"
                self.parent.current = 'Incorrect'

class sixthquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_6 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_6.text = f'Question 6: {Global.random_row.iloc[5, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[5, options_list[0]]
        second_choice = Global.random_row.iloc[5, options_list[1]]
        third_choice = Global.random_row.iloc[5, options_list[2]]
        fourth_choice = Global.random_row.iloc[5, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Seventh"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Seventh"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Seventh"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Seventh"
                self.parent.current = 'Incorrect'

class seventhquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_7 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_7.text = f'Question 7: {Global.random_row.iloc[6, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[6, options_list[0]]
        second_choice = Global.random_row.iloc[6, options_list[1]]
        third_choice = Global.random_row.iloc[6, options_list[2]]
        fourth_choice = Global.random_row.iloc[6, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Eighth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Eighth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Eighth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Eighth"
                self.parent.current = 'Incorrect'

class eighthquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_8 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_8.text = f'Question 8: {Global.random_row.iloc[7, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[7, options_list[0]]
        second_choice = Global.random_row.iloc[7, options_list[1]]
        third_choice = Global.random_row.iloc[7, options_list[2]]
        fourth_choice = Global.random_row.iloc[7, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Nineth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Nineth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Nineth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Nineth"
                self.parent.current = 'Incorrect'

class ninethquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_9 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_9.text = f'Question 9: {Global.random_row.iloc[8, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[8, options_list[0]]
        second_choice = Global.random_row.iloc[8, options_list[1]]
        third_choice = Global.random_row.iloc[8, options_list[2]]
        fourth_choice = Global.random_row.iloc[8, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Tenth"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Tenth"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Tenth"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Tenth"
                self.parent.current = 'Incorrect'

class tenthquestion(Screen):
    option_1 = ObjectProperty(None)
    option_2 = ObjectProperty(None)
    option_3 = ObjectProperty(None)
    option_4 = ObjectProperty(None)
    question_10 = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_pre_enter(self):
        print(Global.question_counter)
        self.chooser()

    def chooser(self):         
        self.ids.question_10.text = f'Question 10: {Global.random_row.iloc[9, 0]}'
        self.ids.score_counter.text = f'{Global.score_counter}'
        values = [1, 2, 3, 4]
        options_list = random.sample(values, 4)
        first_choice = Global.random_row.iloc[9, options_list[0]]
        second_choice = Global.random_row.iloc[9, options_list[1]]
        third_choice = Global.random_row.iloc[9, options_list[2]]
        fourth_choice = Global.random_row.iloc[9, options_list[3]]
        self.ids.option_1.text = f'{first_choice}'
        self.ids.option_2.text = f'{second_choice}'
        self.ids.option_3.text = f'{third_choice}'
        self.ids.option_4.text = f'{fourth_choice}'
        self.ids.option_1.bind(on_release =lambda option_1:self.correct_answer_checker(self.ids.option_1))
        self.ids.option_2.bind(on_release =lambda option_2:self.correct_answer_checker(self.ids.option_2))
        self.ids.option_3.bind(on_release =lambda option_3:self.correct_answer_checker(self.ids.option_3))
        self.ids.option_4.bind(on_release =lambda option_4:self.correct_answer_checker(self.ids.option_4))

    def correct_answer_checker(self, option):
        if Global.normal_mode == True:
            if option.text in questiondf["Correct Answer"].tolist(): 
                Global.score_counter += 1
                Global.question_counter = "Results"
                self.parent.current = 'Correct'
            else:
                Global.question_counter = "Results"
                self.parent.current = 'Incorrect'
        if Global.hard_mode == True:
            if option.text in questiondf["Correct Answer"].tolist():
                Global.score_counter += 1
                Global.question_counter = "Results"
                self.parent.current = 'Correct'
            else:
                Global.score_counter = Global.score_counter - 1
                Global.question_counter = "Results"
                self.parent.current = 'Incorrect'

class correct_screen(Screen):
    next_screen = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_enter(self):
        print(Global.question_counter)
        self.ids.next_screen.bind(on_press = self.question_finder)
        self.display_score_counter()
    def display_score_counter(self):
        self.ids.next_screen.disabled = False
        self.ids.score_counter.text = f'Score: {Global.score_counter}'
    def question_finder(self, instance):
        if Global.question_counter == "Second":
            self.parent.current = 'Second'       
        elif Global.question_counter == "Third":
            self.parent.current = 'Third'    
        elif Global.question_counter == "Fourth":
            self.parent.current = 'Fourth'
        elif Global.question_counter == "Fifth":
            self.parent.current = 'Fifth'
        elif Global.question_counter == "Sixth":
            self.parent.current = 'Sixth'
        elif Global.question_counter == "Seventh":
            self.parent.current = 'Seventh'
        elif Global.question_counter == "Eighth":
            self.parent.current = 'Eighth'
        elif Global.question_counter == "Nineth":
            self.parent.current = 'Nineth'
        elif Global.question_counter == "Tenth":
            self.parent.current = 'Tenth'
        elif Global.question_counter == "Results":
            self.parent.current = 'Results'

class incorrect_screen(Screen):
    print(Global.question_counter)
    next_screen = ObjectProperty(None)
    score_counter = ObjectProperty(None)
    def on_enter(self):
        print(Global.score_counter)
        self.ids.next_screen.bind(on_press = self.question_finder)
        self.display_score_counter()
    def display_score_counter(self):
        self.ids.next_screen.disabled = False
        self.ids.score_counter.text = f'Score: {Global.score_counter}'
    def question_finder(self, instance):
        if Global.question_counter == "Second":
            self.parent.current = 'Second'       
        elif Global.question_counter == "Third":
            self.parent.current = 'Third'
        elif Global.question_counter == "Fourth":
            self.parent.current = 'Fourth'
        elif Global.question_counter == "Fifth":
            self.parent.current = 'Fifth'
        elif Global.question_counter == "Sixth":
            self.parent.current = 'Sixth'
        elif Global.question_counter == "Seventh":
            self.parent.current = 'Seventh'
        elif Global.question_counter == "Eighth":
            self.parent.current = 'Eighth'
        elif Global.question_counter == "Nineth":
            self.parent.current = 'Nineth'
        elif Global.question_counter == "Tenth":
            self.parent.current = 'Tenth'
        elif Global.question_counter == "Results":
            self.parent.current = 'Results'
    

class results(Screen):
    congrats = ObjectProperty(None)
    playerscore = ObjectProperty(None)
    play_again = ObjectProperty(None)
    def on_enter(self):
        pass
    def show_results(self):
        self.ids.playerscore.text = f'{Global.player_username} acheived the score of: {Global.score_counter}'
        df.set_index('Username', inplace=True, drop=True)     
        df.loc[Global.player_username, 'Recent Score'] = Global.score_counter
        current_score = df.loc[Global.player_username, 'Recent Score']
        print(current_score)
        print(df.loc[Global.player_username, 'High Score'])
        if current_score > df.loc[Global.player_username, 'High Score']:
            df.loc[Global.player_username, 'High Score'] = current_score
            self.ids.congrats.text = f'New High Score!'
            print("Blaug")
        elif Global.score_counter >= 7:
            self.ids.congrats.text = f'Congratulations!'
        elif Global.score_counter < 7:
            self.ids.congrats.text = f'Better luck next time'
        elif Global.score_counter <= 3:
            self.ids.congrats.text = f'Smh'
        df.reset_index(drop=True)
        print(df)
        df.to_csv('users.csv')
    def play_again(self):
        self.parent.current = 'First'

class leaderboard(Screen):
    first = ObjectProperty(None)
    second = ObjectProperty(None)
    third = ObjectProperty(None)
    fourth = ObjectProperty(None)
    fifth = ObjectProperty(None)
    def on_enter(self):
        pass
    def leaderboard_sorter(self):
        new_df = pd.read_csv('users.csv', sep=',')
        new_df.sort_values(by=['High Score'], inplace=True, ascending=False)
        self.ids.first.text = f'{new_df.iloc[0]["Username"]}: {new_df.iloc[0]["High Score"]}'
        self.ids.second.text = f'{new_df.iloc[1]["Username"]}: {new_df.iloc[1]["High Score"]}'
        self.ids.third.text = f'{new_df.iloc[2]["Username"]}: {new_df.iloc[2]["High Score"]}'
        self.ids.fourth.text = f'{new_df.iloc[3]["Username"]}: {new_df.iloc[3]["High Score"]}'
        self.ids.fifth.text = f'{new_df.iloc[4]["Username"]}: {new_df.iloc[4]["High Score"]}'
 


class Title(Image):
    pass


class login_next(MDRoundFlatButton):
    pass

class MyMainApp(MDApp):
    def build(self):      
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "DeepPurple"

if __name__ == "__main__":
    MyMainApp().run()