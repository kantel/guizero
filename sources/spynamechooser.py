from guizero import App, Text, PushButton
from random import choice

my_font = "American Typewriter"

def choose_name():
    first_name = ["Anatol", "Daniel", "Woody", "Tiberius", "Smokey", "Carmen", "James",
                  "Hirni", "Beißer"]
    second_name = ["Schielauge", "Mysterioso", "Irrgartenläufer", "Katzenauge", "Dunkelmüller",
                   "Hühnerbrust", "Panzerknacker", "Hornochse", "👻💀☠️👽🤖👻"]
    spy_name = choice(first_name) + " " + choice(second_name)
    name.value = spy_name

app = App(title = "For Your Eyes Only", bg = (235, 215, 182), height = 180, width = 640)

text = Text(app, "Drücke den Knopf um Deinen Geheimnamen zu erfahren:", font = my_font, size = 18)
button = PushButton(app, choose_name, text = "Wähle einen Namen!")
# button.bg = (250, 0, 0) # Funzt nicht unter macOS Catalina
button.font = my_font
button.text_size = 30
button.text_color = (200, 0, 0)
name = Text(app, text = "",  font = my_font, size = 36, color = (0, 200, 0))

app.display()