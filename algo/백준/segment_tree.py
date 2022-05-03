# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:23:28 2019

@author: kjh1
"""

class SegmentTree:
    def __init__(self, values):
        self.data = [0 for _ in values] + values
        self.n = len(values)
        
        for idx in reversed(range(1, self.n)):
            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])
            
#        for idx in range(1, self.n):
#            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])
     
######원래는 위에껀데 아래로바꿔도 똑같이 작동하는듯 이유는모


    def update(self, idx, value):
        idx += self.n
        self.data[idx] = value

        while idx > 1:
            idx //= 2
            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])

    def minimum(self, left, right):
        left += self.n
        right += self.n
        minimum = self.data[left]

        while left < right:
            if left % 2:
                minimum = min(minimum, self.data[left])
                left += 1
            if right % 2:
                right -= 1
                minimum = min(minimum, self.data[right])
            left //= 2
            right //= 2

        return minimum


if __name__ == '__main__':
    st = SegmentTree([1, 5, 3, 7, 5])
    print(st.minimum(0, 3))
    print(st.minimum(1, 3))
    print(st.minimum(1, 2))

    st.update(0,3)
    st.update(2,4)

    print()
    print(st.minimum(0, 3))
    print(st.minimum(1, 3))
    print(st.minimum(1, 2))