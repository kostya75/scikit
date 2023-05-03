
from numpy import random

class Pet():
  boredom_decrement=4
  hunger_decrement=6
  boredom_threshold=5
  hunger_threshold=10
  sounds=["mrp"]
  
  def __init__(self,name='Kitty'): # default?
    self.name=name
    self.hunger=random.randint(self.hunger_threshold)
    self.boredom=random.randint(self.boredom_threshold)
    self.sounds=self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect
    
  
  def clock_tick(self):
    self.boredom+=1
    self.hunger+=1
    
  def mood(self):
    if self.hunger<=self.hunger_threshold and self.boredom <= self.boredom_threshold:
      return "happy"
    elif self.hunger<=self.hunger_threshold:
      return "hungry"
    else:
      return "bored"
    
  def __str__(self):
    state="  I'm "+self.name+"."
    state+=" I feel "+self.mood()+"."
    return state
  
  def hi(self): # play with Pet
    print(self.sounds[random.randint(len(self.sounds))])
    self.reduce_boredom()
  
  def teach(self,word): #teach new 
    self.sounds.append(word)
    self.reduce_boredom()
  
  def feed(self): #feed Pet
    self.reduce_hunger()
    
  def reduce_hunger(self):
    self.hunger=max(0,self.hunger-self.hunger_decrement)
    
  def reduce_boredom(self):
    self.boredom=max(0,self.boredom-self.boredom_decrement)
  
# new pet
# p1=Pet("Fido")
# 
# p1 = Pet("Fido")
# print(p1)
# for i in range(10):
#     p1.clock_tick()
#     print(p1)
# p1.feed()
# p1.hi()
# p1.teach("Boo")
# for i in range(10):
#     p1.hi()
# print(p1)
# p1.hi()
# p1.hi()
# p1.hi()
# p1.hi()
# print(p1)

##################################GAME PLAY #################################
def whichone(petlist,name):
  for pet in petlist:
    if pet.name==name:
      return pet
  return None # if matched, the loop will exit at the line above. If made to this line -> <None> returned 

#whichone([p1],"Fido1")

def play2():
  animals=[]
  option="" #?
  base_prompt="""
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice:
  
  """
  feedback="" #?
  
  while True:
    action=input(feedback+"\n"+base_prompt)
    feedback=""
    words=action.split()
    command=words[0] if len(words)>0 else None

    match command:
      case "Quit":
        print("Exiting ...")
        return None # Exit the WHILE LOOP
      
      case "Adopt":
        if len(words)==2:
          if whichone(animals,words[1]): # not False means animal is in the list
            feedback+="You already have pet with this name\n"
          else:
            animals.append(Pet(words[1]))
      
      case "Greet":
        if len(words)==2:
          pet=whichone(animals,words[1]) # returns pet object or None
          if not pet:
            feedback += "I didn't recognize that pet name on GREET. Please try again."
          else:
            pet.hi()
            
      case "Teach":
        if len(words)==3:
          pet = whichone(animals, words[1])
          if not pet:
            feedback += "I didn't recognize that pet name on TEACH. Please try again."
          else:
            pet.teach(words[2]) 
            
      case "Feed":
        if len(words)==2:
          pet = whichone(animals, words[1])
          if not pet:
            feedback += "I didn't recognize that pet name FEED. Please try again."
          else:
            pet.feed()
            
      case _:
        feedback+= "I didn't understand that. Please try again."
    
    for pet in animals:
      pet.clock_tick()
      feedback += "\n" + pet.__str__()


play2()    


p1=Pet("kitty")
p1.feed()
p1.clock_tick()
p1.hunger

play()    


