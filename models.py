# -*- coding: utf-8 -*-
import os
import glob

class Album(object):
    def __init__(self, path=None, filter_extension=['jpg', 'png', 'gif']):
        self.path = path or os.path.join(os.path.dirname(__file__), 'static')
        self.path = os.path.join(self.path, 'upload')
        self.filter = filter_extension
    @property
    def data(self):
        data = {}
        filenames = []
        for e in self.filter:
            filenames += glob.glob(os.path.join(self.path, "*."+e))
        for i, filename in enumerate(filenames):
            data[str(i)] = os.path.basename(filename)
        del filenames
        print data
        return data
    
 
if __name__=='__main__':
    album = Album()
    print album.data
            