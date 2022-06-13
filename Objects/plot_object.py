from tkinter import *
from PIL import ImageTk, Image

# TODO: number the tables that you get back, use a button to show a graph of the table 

class Plot:

    def __init__(self, data) -> None:
        self.data = data


    def create_view(self):
        root = Tk()
        root.title('Cobra MetaData')
        root.geometry('400x200')
        root.mainloop()

    def create_graph():
        pass


if __name__ == '__main__':
    view = Plot([1, 2, 3])
    view.create_view()