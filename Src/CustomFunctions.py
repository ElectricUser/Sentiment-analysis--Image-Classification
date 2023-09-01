# Imports
from IPython.display import display, Image
import os
from skimage import io


# Functions 
def dirInfo(dir: str):
    # this way gets the name of each dir in training dir but not the file count 
    # Emotions = [it.name for it in os.scandir(train_dir) if it.is_dir()]
    """ dirInfo
    dir: str -> dir containing training data

    ret -> dict of {class_name : number_of_class_image}, total files in dir
    """
    Emotions = dict()

    file_number = 0

    for root_dir, cur_dir, files in os.walk(dir):
        if root_dir != dir:
            # gets the directory name
            dir_name = root_dir.replace(dir + '\\',"")

            # count files number
            file_number += len(files)

            # creates a new array based on the dir name and number of files of that dir
            Emotions.update({
                    dir_name : len(files)
            })
    
    return Emotions, file_number

def printImage(path: str, image: str): 
    """ printImage -  # function to print an image
    # path: path to dir
    # image: image name
    """
    return display(Image(path + '/' + image))
    