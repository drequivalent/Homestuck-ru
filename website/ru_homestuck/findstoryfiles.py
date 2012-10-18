from django.conf import settings
from django.contrib.staticfiles import finders
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
