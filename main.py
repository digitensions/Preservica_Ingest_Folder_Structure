#!/usr/bin/env python3

'''
Description about the scripts functionality
Python version requirement
Developer name, date
'''

import os
from shutil import move
import tenacity
import logging

# Global variables for folder names
PRSV1 = 'Preservica_preservation1_lnk'
PRSV2 = 'Preservica_preservation2_lnk'
PRSN2 = 'Preservica_presentation2_lnk'
PRSN3 = 'Preservica_presentation3_lnk'
LOG = os.environ.get('LOG')

# Global variables defining format types
PRSV_FMTS = ['dng','tif', 'avi', 'mkv', 'wav']
PRSN_FMTS = ['jpg', 'jpeg']

# Setup logging (running from bk-qnap-video)
LOGGER = logging.getLogger('main')
HDLR = logging.FileHandler(os.path.join('main.log'))
FORMATTER = logging.Formatter('%(asctime)s\t%(levelname)s\t%(message)s')
HDLR.setFormatter(FORMATTER)
LOGGER.addHandler(HDLR)
LOGGER.setLevel(logging.INFO)


@tenacity.retry(stop=tenacity.stop_after_attempt(10))
def get_path():
    '''
    Gets source path from user
    '''
    try:
        root = (input('Enter folder path: '))
        os.chdir(root)
        print(f'Path found: {os.getcwd()}')
        LOGGER.info("Path successfully retrieved: %s", root)
        return root
    except FileNotFoundError:
        LOGGER.info("File path was not valid: %s", root)
        print("Path not valid, please try again.")
        raise TryAgain


def get_formats():
    '''
    Determines which formats are in folder and returns as list
    '''
    formats = []
    os.chdir(root)
    for file in os.listdir(root):
        if os.path.isfile(file):
            name, ext = file.split('.')
            if ext not in formats:
                formats.append(ext)
    return formats


def format_analysis():
    '''
    Determines how many folders are needed based on number of formats present
    '''
    prsv_fldrs = 0
    prsn_fldrs = 0
    for format in get_formats():
        if format in PRSV_FMTS:
            prsv_fldrs += 1
        elif format in PRSN_FMTS:
            prsn_fldrs += 1
    return [prsv_fldrs, prsn_fldrs]


def main():
    '''
    Main function to create folders and push files in to them
    '''
    try:
        root = get_path()
    except Exception:
        print('Path could not be established after ten attempts. Script exiting!')
        raise SystemExit

    os.chdir(root)
    folder_nos = format_analysis()

    for file in os.listdir(root):
        os.chdir(root)
        if os.path.isfile(file):
            new_dir = file.strip(f'.{tuple(PRSN_FMTS + PRSV_FMTS)}')
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            os.chdir(new_dir)

            if folder_nos == [1, 0]:
                move(os.path.join(root, file), os.path.join(root, new_dir))

            elif folder_nos == [2, 0]:
                if not os.path.exists(PRSV1):
                    os.mkdir(PRSV1)
                if file.endswith('dng'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSV1))
                if not os.path.exists(PRSV2):
                    os.mkdir(PRSV2)
                if file.endswith('tif'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSV2))

            elif folder_nos == [1, 1]:
                if not os.path.exists(PRSV1):
                    os.mkdir(PRSV1)
                if file.endswith(tuple(PRSV_FMTS)):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSV1))
                if not os.path.exists(PRSN2):
                    os.mkdir(PRSN2)
                if file.endswith(tuple(PRSN_FMTS)):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSN2))

            elif folder_nos == [2, 1]:
                if not os.path.exists(PRSV1):
                    os.mkdir(PRSV1)
                if file.endswith('dng'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSV1))
                if not os.path.exists(PRSV2):
                    os.mkdir(PRSV2)
                if file.endswith('tif'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSV2))
                if not os.path.exists(PRSN3):
                    os.mkdir(PRSN3)
                if file.endswith(tuple(PRSN_FMTS)):
                    move(os.path.join(root, file), os.path.join(root, new_dir, PRSN3))

            else:
                print('Unexpected number of files formats')
                raise SystemExit

if __name__ == '__main__':
    main()
