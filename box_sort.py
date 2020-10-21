# Author: Quanyue Xie
# Date: 10/21/2020
# Description：this program include a class and a sort function
#it can sort the volume from big to small, return nothing
class Box:
    #initialized
    def __init__(self,length,width,height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def volume(self):
        return self._length*self._width*self._height

b1 = Box(3.4, 19.8, 2.1)
b2 = Box(1.0, 1.0, 1.0)
b3 = Box(8.2, 8.2, 4.5)
box_list = [b1, b2, b3]

def box_sort(a_list):
  #modify insertion sort
  for index in range(1, len(a_list)):
    currentBox = a_list[index]
    value = currentBox.volume()
    pos = index - 1
    while pos >= 0 and a_list[pos].volume() < value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = currentBox

box_sort(box_list)
#view volume(not sort)
for box in box_list:
  print("box's volume:{}".format(box.volume()))
