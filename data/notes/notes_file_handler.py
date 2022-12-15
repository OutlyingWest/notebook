import os


class NoteFileHandler:
    def __init__(self, note_id: int, note_body_text=None, file_path=None):
        self.save_path = file_path
        self.id = note_id
        self.text = note_body_text

    def save_note_to_file(self):
        with open(file=f'{self.save_path}{self.id}.txt', mode="w") as note:
            note.write(self.text)

    def read_note_from_file(self):
        with open(file=f'{self.save_path}{self.id}.txt', mode="r") as note:
            rode_note_text = note.read()
        return rode_note_text

    def delete_note_file(self):
        if os.path.isfile(f'{self.save_path}{self.id}.txt'):
            os.remove(f'{self.save_path}{self.id}.txt')
        else:
            print(f'note with id: {self.id} does not exist')


if __name__ == "__main__":
    string = 'as;kdfj;kasd\nsasdfk\nsdafsdfffff'
    nfh = NoteFileHandler(3, file_path=r"C:\Users\px\PycharmProjects\notebook\data\notes\\")
    print(nfh.read_note_from_file())




