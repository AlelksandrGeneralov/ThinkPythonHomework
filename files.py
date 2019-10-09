

fout = open('output.txt', 'w')  # creats a new file 'output.txt' in a writing mode
print(fout)

line1 = "line1, \n"
fout.write(line1)

line2 = "line2. \n"
fout.write(line2)

x = 555
fout.write(str(x))

camels = 42
fout.write("\n" '%d' % camels)

fout.close()

import os

cwd = os.getcwd()  # returns relative directory
print(cwd)

print(os.path.abspath('output.txt'))  # returns absolute directory
print(os.path.exists('output.txt'))  # checks if file or directory exists
print(os.path.isdir('/home/aleksandr/programming_script'))  # checks if it is a directory
print(os.path.isfile('output.txt'))  # checks if it is a file
print(os.listdir(os.getcwd()))  # returns all files and dirs in current directory


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


print(walk('/home/aleksandr/programming_script'))

try:
    fout = open('bad_file.txt', 'w')
    for line in fout:
        print(line)
    fout.close()
except:
    print('something went wrong')
