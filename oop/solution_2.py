class Factory :
   def __init__(self,material,zips):
      self.material = material
      self.zips = zips
      

class Bhopalfatory(Factory):
    def __init__(self, material, zips , colour):
       super().__init__(material, zips)
       self.colour = colour 
       
class Punefactory(Bhopalfatory):
    def __init__(self, material, zips, colour ,pocket):
       super().__init__(material, zips, colour)
       self.pocket = pocket
       
       
obj = Punefactory()