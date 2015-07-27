import pickledb 
import jsonpickle
import json
import os

class intakeRepository:
    _intakeKey = 'intakes'
    _userInfoKey= 'userInfo'
    
    def __init__(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'db/intakeTracker.db')
        self.db = pickledb.load(file_path, False) 
        
    def saveUserInfo(self,userInfo):
        self.db.set(self._userInfoKey,jsonpickle.encode(userInfo))
        self.db.dump()
    
    def getUSerInfo(self):
        data = self.db.get(self._userInfoKey)
        if data:
            return jsonpickle.decode(data)
            
        return None
    def addIntake(self,ingridient):
        data = self.db.get(self._intakeKey)
        if not data:
            self.db.lcreate(self._intakeKey)
            
        self.db.ladd(self._intakeKey,jsonpickle.encode(ingridient,keys=True))
        self.db.dump()
        
    def getIntakes(self):
        result = []
        data = self.db.get(self._intakeKey)
        if data:
            for item in self.db.lgetall(self._intakeKey):
                result.append(jsonpickle.decode(item))
            
            return result
        return []
    
    def getIntakeByDate(self,date):
        data = self.db.get(self._intakeKey)
        if not data:
            return []
         
        result = []
        for item in self.db.lgetall(self._intakeKey):
                item =jsonpickle.decode(item)
                
                if item.timestamp.date() == date:
                    result.append(item)   
        return result
        
    def getIntakeListDateRangeFilter(self,dateFrom,dateTo):
        data = self.db.get(self._intakeKey)
        if not data:
            return []
         
        result = []
        for item in self.db.lgetall(self._intakeKey):
                item =jsonpickle.decode(item)
                if item.timestamp.date() >= dateFrom and item.timestamp.date()<=dateTo:
                    result.append(item)   
        return result
    
    def removeLastIntake(self):
        lastItem = len(self.getIntakes())-1
       
        if lastItem>=0:
            self.db.lpop(self._intakeKey,lastItem)
            self.db.dump()