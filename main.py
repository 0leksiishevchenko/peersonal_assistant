"""
Personal_assistant is a personal manager for everyday tasks:
    keeping contacts - names, addresses, phone etc;
    remaindering of upcoming birthdays;
    keeping personal notes
"""
from textual.app import App, ComposeResult
from textual.widgets import (Header,
                             Footer,
                             TabbedContent,
                             TabPane)

from tui import dashboard, contacts, notes, settings


class PersonalAssistant(App):
    """
    Main clas for personal_assistant textual app
    """

    BINDINGS = [
        ("d", "show_tab('dashbrd')", "Dashboard"),
        ("c", "show_tab('contacts')", "Contacts"),
        ("n", "show_tab('notes')", "Notes"),
        ("s", "show_tab('settings')", "Settings"),
    ]

    def compose(self) -> ComposeResult:
        """Create childs for the application"""
        yield Header()
        yield Footer()

        with TabbedContent():
            with TabPane("Dashboard", id="dashbrd"):
                yield dashboard.paDashBoard
            with TabPane("Contacts", id="contacts"):
                yield contacts.paContacts
            with TabPane("Notes", id="notes"):
                yield notes.paNotes
            with TabPane("Settings", id="settings"):
                yield settings.paSettings

    def toggle_dark(self) -> None:
        """Switch to dark mode and back"""
        self.dark = not self.dark

    def action_show_tab(self, tab_id: str) -> None:
        """
        Switching tabs by id
        :param tab_id: identificator for tab user clicked or entered command
        :return: None
        """
        self.get_child_by_type(TabbedContent).active = tab_id


if __name__ == "__main__":
    # Load/Create AddressBook
    # Load/Create NoteBook
    app = PersonalAssistant()
    app.run()
