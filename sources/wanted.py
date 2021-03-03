from guizero import App, Text, Picture
import os

# Hier wird der Pfad zum Verzeichnis des ».py«-Files gesetzt
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

my_font = "American Typewriter"

app = App(title = "Steckbrief", width = 400, height = 600)
app.bg = (232, 226, 7)

wanted_text = Text(app, "GESUCHT!")
wanted_text.text_size = 50
wanted_text.font = my_font

dodo = Picture(app, image = "images/dodo.jpg")

bottom_text = Text(app, "Alice und der Dodo")
bottom_text.text_size = 25
bottom_text.font = my_font

app.display()