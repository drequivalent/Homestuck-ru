from django.conf import settings
from django.contrib.staticfiles import finders
from django.contrib.staticfiles import utils
from django.core.files.storage import FileSystemStorage
import os.path
from glob import glob

class StoryfilesFinder(finders.BaseFinder):
    def find(self, path, all = False):
        elems = path.split("/")
        if elems[0] != "storyfiles":
            return None
        filename = os.path.join(*elems[1:])
        storyfiles_dir = settings.HOMESTUCK_STORYFILES_DIR
        found_files = glob(os.path.join(storyfiles_dir, "*", "img", filename)) + \
                      glob(os.path.join(storyfiles_dir, "*", "*", "img", filename))
        if all:
            return found_files
        else:
            return found_files[0]

    def list(self, ignore_patterns):
        storyfiles_dir = settings.HOMESTUCK_STORYFILES_DIR
        dirs = glob(os.path.join(storyfiles_dir, "*", "img")) + \
               glob(os.path.join(storyfiles_dir, "*", "*", "img"))
        for directory in dirs:
            storage = FileSystemStorage(location=directory)
            storage.prefix = "storyfiles"
            for path in utils.get_files(storage, ignore_patterns):
               yield path, storage
