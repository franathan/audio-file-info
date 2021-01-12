#!/Users/bin/python

import soundfile as sf
import os
while True:
    usr_file = input('Please paste path to file or directory, or [q]uit: ')
    if usr_file == 'q':
        break
    elif os.path.isdir(usr_file):
        for file in os.listdir(usr_file):
            filename = os.path.join(usr_file, file)
            try:
                print(sf.info(filename))
            except RuntimeError as e:
                print('File Format not recognized for <{}>!'.format(filename))
            print('***********************************************************************')
    elif os.path.isfile(usr_file):
        try:
            print(sf.info(usr_file))
        except RuntimeError as e:
            raise print('File Format not recognized for <{}>!'.format(usr_file))
    else:
        print('File cannot be parsed')
