class ingridientModel():
    
    def __init__(self):
        self.reference=''
        self.description =''
        self.measureDesc=''
        self.kcal = 0
        self.protein = 0
        self.carbo = 0
        self.fat=0
    
    def mapFromDict(self,i):
        
        self.reference=i['NDB_No']
        self.description=i['Shrt_Desc']
        self.measureDesc=i['GmWt_1']
        self.kcal=i['Energ_Kcal']
        self.protein=i['Protein']
        self.carbo=i['Carbohydrt']
        self.fat=i['Lipd_Tot']
        
        return self
        
    def formatForLogPrint(self,grams):
        quantity = grams/float(100)
        
        return [self.description,
                self.kcal*quantity,
                self.protein*quantity,
                self.carbo*quantity,
                self.fat*quantity]
       