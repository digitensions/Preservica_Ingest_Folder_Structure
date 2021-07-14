import os
from shutil import move

# Global variables for folder names
prsv1 = 'Preservica_preservation1_lnk'
prsv2 = 'Preservica_preservation2_lnk'
prsn2 = 'Preservica_presentation2_lnk'
prsn3 = 'Preservica_presentation3_lnk'

# Global variables defining format types
prsv_fmts = ['dng','tif', 'avi', 'mkv' 'wav']
prsn_fmts = ['jpg', 'jpeg']

# Gets source path from user
def get_path():
    try:
        root = (input('Enter folder path: '))
        os.chdir(root)
        print(f'Path found: {os.getcwd()}')
        return root
    except FileNotFoundError: 
        print('Path not valid')
        raise SystemExit

# Determines which formats are in folder and returns as list
def get_formats():
    formats = []
    os.chdir(root)
    for file in os.listdir(root):
        if os.path.isfile(file):
            name, ext = file.split('.')
            if ext not in formats:
                formats.append(ext)
    return formats

# Determines how many folders are needed based on number of formats present
def format_analysis():
    prsv_fldrs = 0
    prsn_fldrs = 0
    for format in get_formats():
        if format in prsv_fmts:
            prsv_fldrs += 1
        elif format in prsn_fmts:
            prsn_fldrs += 1
    return [prsv_fldrs, prsn_fldrs]

# Main function to create folders and push files in to them
def main():
    folder_nos = format_analysis()
    
    for file in os.listdir(root):
        os.chdir(root)
        if os.path.isfile(file):
            new_dir = file.strip(f'.{tuple(prsn_fmts + prsv_fmts)}')
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            os.chdir(new_dir)

            if folder_nos == [1, 0]:
                move(os.path.join(root, file), os.path.join(root, new_dir))

            elif folder_nos == [2, 0]:
                if not os.path.exists(prsv1):
                    os.mkdir(prsv1)
                if file.endswith('dng'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsv1))
                if not os.path.exists(prsv2):
                    os.mkdir(prsv2)
                if file.endswith('tif'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsv2))
            
            elif folder_nos == [1, 1]:
                if not os.path.exists(prsv1):
                    os.mkdir(prsv1)
                if file.endswith('dng'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsv1))
                if not os.path.exists(tuple(prsv_fmts)):
                    os.mkdir(prsn2)
                if file.endswith(tuple(prsn_fmts)):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsn2))
            
            elif folder_nos == [2, 1]:
                if not os.path.exists(prsv1):
                    os.mkdir(prsv1)
                if file.endswith('dng'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsv1))
                if not os.path.exists(prsv2):
                    os.mkdir(prsv2)
                if file.endswith('tif'):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsv2))
                if not os.path.exists(prsn3):
                    os.mkdir(prsn3)
                if file.endswith(tuple(prsn_fmts)):
                    move(os.path.join(root, file), os.path.join(root, new_dir, prsn3))

            else:
                print('Unexpected number of files formats')
                raise SystemExit

if __name__ == '__main__':
    root = get_path()
    os.chdir(root)
    main()