import GetNovelText, pyperclip
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container

class PasswordGenerator(App):

    CSS_PATH = "suetonius.css"
    BINDINGS = [('d','toggle_dark','Toggle dark mode')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(PasswordGenerationButton(),Passwords(password_candidates))

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

class PasswordGenerationButton(Static):

    def on_button_pressed(self, event: Button.Pressed) -> list:
        #password_candidates = GetNovelText.main()
        #return password_candidates

    def compose(self) -> ComposeResult:
        yield Button(label="Generate Password",id="generatePassword")
        for candidate in password_candidates:
            yield Button(label=candidate, id="password")

class Passwords(Static):

    def __init__(self,password_candidates):
        self.password_candidates = password_candidates

    def on_button_pressed(self, event: Button.Pressed):
        pyperclip.copy(Button.label)
        
    def compose(self) -> ComposeResult:
        for candidate in self.password_candidates:
            yield Button(label=candidate, id="password")

if __name__ == "__main__":
    password_candidates = []
    app = PasswordGenerator()
    app.run()
