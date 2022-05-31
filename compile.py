import re
from Compiler import Scanner
import multiprocessing as mp


class CobraCompiler:

    def __init__(self, line, line_number):
        self.line = line
        self.line_number = line_number


    # SCAN the line
    def scan(self):
        x = Scanner(self.line, self.line_number)
        return x.create_tokens()


    # # get the keyword | variable # * Complier >
    # if get_keyword(line[0]) == 'var':
    #     cobra_var = Variable(line[1],  )


if __name__ == '__main__':
    mp.set_start_method('spawn')
    c = CobraCompiler('var url =  "https://www.python.org/"', 1)
    p = mp.Process(target=c.scan()) 
    p.start()
    