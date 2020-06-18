from typing import *

class Line():
    def __init__(self, cmd: str, value: Optional = None):
        self.cmd = cmd
        self.value = value

    def __str__(self):
        return self.cmd + ' ' + (str(self.value) if self.value is not None else '')