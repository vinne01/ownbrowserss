# class A:
#   def cv(self):
#       print("i am best friends")
# class B(A):
#   def cv(self):
#       print("i am like you")
# obj=B()
# obj.cv()
class Area:
    def area(self,x=none,y=none):
        if x!=none and y!=none :
            print(x*y)
        elif x!=none:
            print(x*x)
        else:
            print("nothing")
    obj=Area()
    obj.area()
    obj.area(12,34)
    obj.area(23)