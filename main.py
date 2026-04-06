from pyscript import display,document #type:ignore

class Classmate:  # Creating the class
    def __init__(self, name, section, subject):
        self.name = name  #attribute
        self.section= section  #attribute
        self.subject= subject  #attribute

#  Putting classmates into a list
classmate_list = [
Classmate('Caleb Arias', 'Topaz', 'Math'),
Classmate('Alejandro Enriquez', 'Topaz', 'Social Sciences'),
Classmate('Khloe Espina', 'Topaz', 'Science'),
Classmate('Martina Cajucom','Topaz', 'Science'),
Classmate('Renzo Arce', 'Topaz', 'CAT'),
]

def show_classmates (e):  # adding new classmates 

    document.getElementById('output').innerHTML =''

    name = document.getElementById('input1').value
    section= document.getElementById('input2').value
    subject = document.getElementById('input3').value

    classmate = Classmate(name, section, subject)
    classmate_list.append(classmate)  # allows multiple classmates to be added 
    
# displaying classmates with new classmate
    for classmate in classmate_list:
        display(f'{classmate.name} is part of {classmate.section} and their favourite subject is {classmate.subject}' , target='output')  