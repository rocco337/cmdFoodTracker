import pickledb 
import jsonpickle
import json
import os

class nutritionTableRepository:
    def __init__(self): 
        self.data=[]
        self.cache = {}
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'db/nutritionTable.db')
        with open(file_path) as data_file:    
            self.data = json.load(data_file)
         
    def search(self,searchTerm):
        
        #store result into cache to avoid iteration every time
        if searchTerm in self.cache:
            return self.cache[searchTerm]
        else:
            result = [s for s in self.data if self._contains(searchTerm.lower(),s['Shrt_Desc'].lower()) or str(s['NDB_No']) == searchTerm ][:20]
            self.cache[searchTerm] = result
            return result
    
    def searchByReference(self,reference):
        if reference in self.cache:
            return self.cache[reference][0]
        else:
            result = [s for s in self.data if s['NDB_No'] == reference ]
            self.cache[reference] = result
            return result[0] if result else None
            
    def searchByReferences(self,references):
        result =[]
        for reference in references:  
            result = result + [s for s in self.data if s['NDB_No'] == reference ]
            
        return result
        
    def _contains(self,searchTerm,value):
        result = True
        for term in searchTerm.split():
            if term not in value:
                return False
        
        return result
        
    def getAll(self):
        return self.data;