from dataclasses import dataclass
from tkinter import *
from PIL import ImageTk, Image
import plotly.express as px


@dataclass(slots=True)
class Plot:


    def __call__(self):
        print('Plot Object made')

    def __init__(self, data_dict) -> None:
        self.data_dict = data_dict
        self.__call__()

    def _create_graph(self, data):
        print(data)
        try:                                #! ONLY DID THIS TO SEE IF DIFFERENT DATAFRAMES ARE BEING READ
            fig = px.histogram(data, nbins=50)
            fig.show()
        except:
            pass
        


    def create_view(self):
        root = Tk()
        root.title('Cobra MetaData')
        root.geometry('400x200')
        for name in self.data_dict.keys():
            my_button = Button(root, text=name, command=lambda data = self.data_dict[name]: self._create_graph(data))
            my_button.pack()
        root.mainloop()

    


if __name__ == '__main__':
    data = {'table1': [1, 2, 3, 4, 5, 6, 7], 'table2': [2, 3, 6, 7, 8, 9]}
    view = Plot(data)
    view.create_view()