import re
from Compiler.type import get_keyword
from Objects.variable_object import Variable

def cobra_compile(line):
    # get the keyword | variable # * Complier >
    if get_keyword(line[0]) == 'var':
        cobra_var = Variable(line[1],  )