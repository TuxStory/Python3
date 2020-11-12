class rectangle:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    def surface(self):
        return self._x*self._y

class paveDroit(rectangle):
    def __init__(self,x,y,z):
        rectangle.__init__(self,x,y)
        self.__z = z
    def volume(self):
        return self._x*self._y*self.__z

photo = rectangle(10,15)
print (photo._x)
print (photo._y)
print (photo.surface())
print (" ")
weston = paveDroit(3,4,10)
print (weston.volume())
