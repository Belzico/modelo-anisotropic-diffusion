import os
import re

def remove_character(path_file):
    '''
    Elimina todas las ocurrencias del caracter '&' en el archivo path_file.
    '''
    file = open(path_file, 'r+')
    lines = file.readlines()
    new_lines = []

    for line in lines:
        new_line = re.sub(r'&', '', line)
        new_lines.append(new_line)

    file.truncate(0)
    file.seek(0)
    file.writelines(new_lines)
    file.close()

if __name__ == '__main__':

    path = 'PyUi/'
    files = os.listdir(path)

    for file in files:
        if file.__contains__('.'):
            name,_ = file.split('.')
            if name != '__init__':
                remove_character(path + file)
