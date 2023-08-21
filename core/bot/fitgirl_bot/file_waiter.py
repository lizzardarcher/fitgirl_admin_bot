import glob
import time
import os
import traceback

class FileWaiter:

    def __init__(self, path: str):
        self.path = path
        self.files = set(glob.glob(path))

    def wait_new_file(self, timeout: int) -> set:
        """
        Waits for a new file to be created and returns the new file path.
        """
        endtime = time.time() + timeout
        while True:
            time.sleep(5)
            diff_files = set(glob.glob(self.path)) - self.files
            if diff_files:
                self.files = set(glob.glob(self.path))
                return diff_files
            if time.time() > endtime:
                raise Exception("No downloaded files")