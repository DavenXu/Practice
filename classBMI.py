### Class BMI ###

class BMI : 
     def __init__(self, name, age, weight, height):
          self.__name = name
          self.__age = age 
          self.__weight = weight
          self.__height = height 

     def getBMI(self):
          Height = self.__height / 100
          value = self.__weight / (Height**2)
          return value
     
     def getStatus(self):
          bmi = self.getBMI()
          
          if bmi < 18.5 :
               return " UnderWeight "
          elif bmi < 24:
               return " Normal "
          elif bmi < 30 :
               return " OverWeigt "
          else:
               return " Obese"
          
     def getName(self):
          return self.__name
     
     def getAge(self): 
          return self.__age
     
     def getWeight(self):
          return self.__weight
     
     def getHeight(self):
          return self.__height