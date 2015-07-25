import datetime,readline
from dateutil.parser import parse

from repositories.intakeRepository import intakeRepository
from repositories.nutritionTableRepository import nutritionTableRepository
from tabulate import tabulate
import handlersCommon
import json

class intakeHandler:
    def __init__(self):
        self.repository = intakeRepository()
        self.nutritionTable = nutritionTableRepository()
        self.ingiridents =[]
        
    def addIngirident(self,ingridientName):
        
        ingridients = self.nutritionTable.search(ingridientName)
        
        #if there is exact match than take it!
        exactMatchExists = [s for s in ingridients if s['Shrt_Desc'].lower()==ingridientName.lower()]
        if len(ingridients) == 1 or exactMatchExists:
            measure = ingridients[0]['GmWt_Desc1'] + ': ' + str(ingridients[0]['GmWt_1']) + ' grams'
            amount = input('[' + measure + '] ' +'Quantity in grams:')
            
            date = raw_input("Date(dd-mm-yyyy - skip to use today date): ")
            
            if date:
                date = parse(date)
            
            print date   
            self.ingirident = ingridientModel(ingridients[0]['NDB_No'],amount,date)
            self.repository.addIngridient(self.ingirident)
        else:
           print 'No ingridient ' + ingridientName + ' found!'
       
    def showIntake(self,date):
        if not date:
            date = datetime.date.today()
        else:
            date = parse(date).date()
            
        self.ingiridents = self.repository.getIntakeByDate(date)
        if not self.ingiridents:
            print "No intakes were found for date " + str(date) + "."
            return
        
        ingridients=[]
        for i in self.ingiridents:
            ingridient = self.nutritionTable.searchByReference(i.ingridientReference)
            ingridients.append(self.formatIngridientForPrint(ingridient,i.amount))
        
       
        print tabulate(ingridients,headers=["Description","Kcal","Protein","Carbo","Fat","Grams"],tablefmt='orgtbl',numalign="right")
    
    def removeLast(self):
        self.repository.removeLastIngridient()
        self.showIntake(None)
    
    def getSimilarIngridients(self, searchTerm):
        ingridients = self.nutritionTable.search(searchTerm)
        return [str(i['Shrt_Desc']).lower() for i in ingridients]
    
    def parseMeasure(self,rawMeasure):
        if not rawMeasure:
            return '1 piece'
        
        return rawMeasure
    
    def formatIngridientForPrint(self,i,grams):
        fat = handlersCommon.getTotalFatCount(i)
        quantity = grams/100
        return [i['Shrt_Desc'],i['Energ_Kcal']*quantity,i['Protein']*quantity,i['Carbohydrt']*quantity,i['Lipd_Tot']*quantity,grams]
        
class ingridientModel:
    def __init__(self,ingridientReference,amount,time):
        self.ingridientReference=ingridientReference
        self.amount=amount
        
        if not time:
            time = datetime.datetime.utcnow()
        
        self.timestamp = time
       