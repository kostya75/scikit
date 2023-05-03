
# start class with capital letter

# class is factory
class Point():
  pass

# instance
point1=Point()
print(point1)

# method is function that belongs to class
# function has at least one argument "self"

class Point():
  def getX(self):
    return(self.x)
  
point2=Point()
point2.x=5
point2.getX()

####### CONSTRUCTOR ####
# DUNDER SCORE __init__
class Point():
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def getX(self):
    return self.x


point3=Point(4,5)
  
  
####### ADDITIONAL METHODS ########
class Point():
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y

###### add distance as method ####
class Point():
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y
  
  def distance(self,point): # AS METHOD
    dist=((self.getX()-point.getX())**2+(self.getY()-point.getY())**2)**.5
    return dist
  def __str__(self): # RETURNS Text representation. Readable representation of the Instance
    return f"Point with coords: {self.x}, {self.y}"
  def values(self):
    return self.x, self.y
  
  
def dist2(point1, point2): # AS function: NOTICE Idententition
  dist=((point1.getX()-point2.getX())**2+(point1.getY()-point2.getY())**2)**.5
  return dist
######################################

point1=Point(2,3)
point2=Point(4,5)
print(point1.distance(point2),dist2(point1,point2))
print(point1.values())

##########################################
##### DUNDER SCORE METHODS ###############
# __add__ and __sub__ can be overwritten 
##########################################

class Point():
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
  def getX(self):
    return self.x
  
  def getY(self):
    return self.y
  
  def distance(self, point): # AS METHOD
    dist=((self.getX()-point.getX())**2+(self.getY()-point.getY())**2)**.5
    return dist
  def __str__(self): # RETURNS Text representation. Readable representation of the Instance
    return f"Point with coords: {self.x}, {self.y}"
  def values(self):
    return self.x, self.y
  
  def __add__(self,point):
    return Point(self.x+point.x, self.y+point.y)
  

def dist2(point1, point2): # AS function: NOTICE Idententition
  dist=((point1.getX()-point2.getX())**2+(point1.getY()-point2.getY())**2)**.5
  return dist

point1+point2

# Instances as return Values see above for _add__

###########################
#### SORTING INSTANCES ####
###########################


# Sort on a tuple
[print(p) for p in sorted([point1,point2],key=lambda x: (x.getX(), x.getY()), reverse=False)]

# alternatively can devine method: sort_priority to make it look nice
  def sort_priority(self):
    return self.y
  
###########################################
#### Class Variables and Instance Variables
###########################################
