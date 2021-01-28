import numpy as np
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        x= np.int32(x)
        quo = x
        if quo<0: #if input < 0 make it positive
            quo*= -1
        while quo!= 0:
            quo,rem = divmod(quo, 10)
            rev= rev*10 +rem
        if x<1: #if input < 0 turn the output back to negative
            rev*= -1
        if rev < np.iinfo(x).min or rev > np.iinfo(x).max: # check for overvflow
            rev = 0
        return rev