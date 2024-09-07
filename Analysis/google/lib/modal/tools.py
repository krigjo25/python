

import os
import numpy as np

class Tools():
    
    def __init__(self, path = None, ) -> None:
        self.path = path

    def fetch_files(self):

        try:
            if not os.scandir(self.path): raise FileNotFoundError('File / directory not found in the system')

        except FileNotFoundError as e: return f"{e}" 

        #   Initialize the data
        path = os.scandir(self.path)
        dir = np.array([])

        for i in path:

            #   Ensure its directory and initialize a dictionary
            if i.is_dir(): dir = np.append(dir, {"images":[], "json":[], "path":f"{i.path}"})


        for i in (range(np.size(dir))):

            #   initialize sub directory path
            subdir = os.scandir(dir[i]['path'])

            for f in subdir:

                #   Ensure that we add only jpg files
                if f.name.endswith('.jpg'): dir[i]['images'] += [f.path]
                if f.name.endswith('.json'): dir[i]['json'] += [f.path]

        #   Initialize a list of indexes
        terminate = []
        
        for i in range(np.size(dir)):
            if np.size(dir[i]['images']) < 1 or np.size(dir[i]['json']) < 1: terminate += [i]

        #   Clear memory
        arr = np.delete(dir, terminate)
        del subdir, dir, terminate

        #   Assign files to array
        for i in range(np.size(arr)): arr[i]['size'] = np.size(arr[i]['images'])

        return arr

