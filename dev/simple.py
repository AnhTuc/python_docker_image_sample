from .helper import pow2

class PowerNum:
    def __init__(self, val = 1):
        self.val = val
    
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self, s):
        self._val = s
    
    def power_of_two(self):
        self.val = pow2(self.val)
    