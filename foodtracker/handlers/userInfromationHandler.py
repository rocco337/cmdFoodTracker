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
            self.perosnalInfo.age=input("Age: ")
            self.perosnalInfo.weight=input("Weight(kg): ")
            self.perosnalInfo.height=input("Height(cm): ")
            
            self.repository.saveUserInfo(self.perosnalInfo)
        
        self.perosnalInfo.printInfo()
    
class perosnalInfo:
    def __init__(self):
        self.name=""
        self.age=0.0
        self.weight=0.0
        self.height=0.0
        self.activityLevel=0.0
        self.bodyfat=0.0
        self.sex=''
        self.bmr=0.0
        
    def printInfo(self):
        print (" Name: %s  Age: %s Weight: %s kg  Height: %s cm  BMR: %s"% (self.name,self.age,self.weight,self.height,self.bmr))
    
    
    
    