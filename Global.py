from kivy.properties import StringProperty, NumericProperty
player_username = ""
player_password = ""
score_counter = 0
question_counter = ""
random_row = None
normal_mode = False
hard_mode = False

"""            StartButton:
                source: "Start.png"
                on_press:
                    source: "Start2.png"
                on_release:
                    root.transition_effect()
                    app.root.current = "First"



                     GridLayout:
        rows:1


        GridLayout:
            rows:3

            Title:
                source: 'Title.png'
                size: self.texture_size





    self.label.text = f'Welcome {self.user.text}' 

What does CPU stand for?,Central Processing Unit,Control Performance Unit,Corporate Productivity Unit,Central Predictory Unicode
What does RAM stand for?,Random Access Memory,Regulated Analysis Memory,Random Alien Magic,Real Addition Multiplication
How can you improve a computer's performance?,Add more RAM,Download more RAM,Undervolt the CPU,Shake the monitor
What is clock speed measured in?,Hertz,Bytes,Seconds,Cycles
What is a core?,A processing unit within a CPU,A second processing unit within a control unit,A system that has many processors,Clock where clock speed is counted
What is hardware?,The physical components of a computer system,The physical parts that are attached to the motherboard,The logical components of a computer system,The Monitor
Which type of concern would the digital divide be classed under,Cultural,Ethical,Legal,Copyright
Which of these statements about non-proprietary software is true?,It has no copyright and can be freely distributed,It is copyrighted and cannot be freely distributed,It is copyrighted but can be freely distributed
What is the purpose of the Copyright Designs and Patents Act 1988?,To protect peoples' creations,To allow people to share media,To deter people from sharing data
What is a copyright?,A legal means of ensuring that creators can protect what they create,A legal means of ensuring that people can stream videos online,A legal means of ensuring that people can distribute media

with open('question.csv', newline='') as questionfile:
    reader2 = csv.reader(questionfile)
"""


