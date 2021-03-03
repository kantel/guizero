from guizero import App, Text

app = App(title = "Hello guizero! 🐍")
app.bg = (251, 251, 208)
text = Text(app, text = "Hällo Wörld mit Python 🐍 und guizero.")
text.text_size = 25

app.display()