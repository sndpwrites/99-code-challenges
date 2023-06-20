import glob
import os


def func_rename(location, pattern, newName):
    for file in glob.iglob(os.path.join(location, pattern)):
        filename, extension = os.path.splitext(os.path.basename(file))
        os.rename(file, os.path.join(location, newName % filename + extension))
# 1st argument is the path
# 2nd argument is file pattern
# 3rd argument is the new filename, e.g. 'new %s'
# func_rename('C:\\Users\\Admin\\sheet\\','*.*','old %s')
