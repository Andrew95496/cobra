

def cobra_compile(x):
    print(x)

with open('/Users/drewskikatana/Documents/Programming/cobra/Cobra/example.cobra', 'r') as file:
    file = file.readlines()
    for line in file:
        cobra_compile(line)
