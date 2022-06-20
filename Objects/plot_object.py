from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt

# TODO: number the tables that you get back, use a button to show a graph of the table 

class Plot:

    __slots__ = ('data_dict')

    def __init__(self, data_dict) -> None:
        self.data_dict = data_dict

    def _create_graph(self, data):
        plt.hist(data)
        print(data)
        plt.show()


    def create_view(self):
        root = Tk()
        root.title('Cobra MetaData')
        root.geometry('400x200')
        for name, data in self.data_dict.items():
            print(data)
            Button(root, text=f'{name}', command=lambda: self._create_graph(data)).pack()
        root.mainloop()

    


if __name__ == '__main__':
    data = {'table1': [1, 2, 3, 4, 5, 6, 7], 'table2': [2, 3, 6, 7, 8, 9]}
    view = Plot(data)
    view.create_view()