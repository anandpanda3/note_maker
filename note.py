class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteMaker:
    def __init__(self):
        self.notes = []

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        print("Note added successfully!")

    def delete_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                print("Note deleted successfully!")
                return
        print("Note not found!")

    def display_notes(self):
        if not self.notes:
            print("No notes found!")
            return
        print("----- Your Notes -----")
        for note in self.notes:
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
            print("-----------------------")

# Creating an instance of NoteMaker
note_maker = NoteMaker()

while True:
    print("\n1. Add a note")
    print("2. Delete a note")
    print("3. Display notes")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        note_maker.add_note(title, content)
    elif choice == "2":
        title = input("Enter note title to delete: ")
        note_maker.delete_note(title)
    elif choice == "3":
        note_maker.display_notes()
    elif choice == "4":
        print("Thank you for using the NoteMaker application!")
        break
    else:
        print("Invalid choice. Please try again.")
