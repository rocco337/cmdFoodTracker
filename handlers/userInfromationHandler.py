from repositories.intakeRepository import intakeRepository

class userInfromationHandler:
    def __init__(self):
        self.perosnalInfo = perosnalInfo()
        self.repository = intakeRepository()
        
    def readPersonalData(self):
        
        userInfo = self.repository.getUSerInfo()
       
        if userInfo:
            self.perosnalInfo = userInfo
        else:
            self.perosnalInfo.name=raw_input("Your name: ")
            self.perosnalInfo.age=raw_input("Age: ")
            self.perosnalInfo.weight=raw_input("Weight(kg): ")
            self.perosnalInfo.height=raw_input("Height(cm): ")
            self.perosnalInfo.activityLevel=raw_input("Activity level(1-3): ")
            self.perosnalInfo.bodyfat=raw_input("Body fat(percent): ")
            
            self.repository.saveUserInfo(self.perosnalInfo)
        
        self.perosnalInfo.printInfo()
    
    
class perosnalInfo:
    def __init__(self):
        self.name=""
        self.age=0
        self.weight=0
        self.height=0
        self.activityLevel=0
        self.bodyfat=0.0
    
    def printInfo(self):
        print ("  Name: %s  Age: %s Weight: %s kg   Heighth: %s cm"% (self.name,self.age,self.weight,self.height))
    
    
        
    