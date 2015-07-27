import pickledb 
import jsonpickle
import json
import os

class intakeRepository:
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'db/intakeTracker.db')
        self.db = pickledb.load(file_path, False) 
        
    def saveUserInfo(self,userInfo):
        self.db.set("userInfo",jsonpickle.encode(userInfo))
        self.db.dump()
    
    def getUSerInfo(self):
        data = self.db.get("userInfo")
        if data:
            return jsonpickle.decode(data)
            
        return None
    def addIngridient(self,ingridient):
        keyName ="ingridients"
        data = self.db.get(keyName)
        if not data:
            self.db.lcreate(keyName)
            
        self.db.ladd(keyName,jsonpickle.encode(ingridient,keys=True))
        self.db.dump()
        
    def getIngridients(self):
        result = []
        data = self.db.get("ingridients")
        if data:
            for item in self.db.lgetall("ingridients"):
                result.append(jsonpickle.decode(item))
            
            return result
        return []
    
    def getIntakeByDate(self,date):
        data = self.db.get("ingridients")
        if not data:
            return []
         
        result = []
        for item in self.db.lgetall("ingridients"):
                item =jsonpickle.decode(item)
                
                if item.timestamp.date() == date:
                    result.append(item)   
        return result
        
    def getIntakeListDateRangeFilter(self,dateFrom,dateTo):
        data = self.db.get("ingridients")
        if not data:
            return []
         
        result = []
        for item in self.db.lgetall("ingridients"):
                item =jsonpickle.decode(item)
                if item.timestamp.date() >= dateFrom and item.timestamp.date()<=dateTo:
                    result.append(item)   
        return result
    
    def removeLastIngridient(self):
        lastItem = len(self.getIngridients())-1
       
        if lastItem>=0:
            self.db.lpop("ingridients",lastItem)
            self.db.dump()