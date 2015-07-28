from dateutil.parser import parse
from repositories.intakeRepository import intakeRepository
from repositories.nutritionTableRepository import nutritionTableRepository
from repositories.models import intakeModel
from tabulate import tabulate
import handlersCommon,datetime,readline,json

class intakeHandler:
    def __init__(self):
        self.repository = intakeRepository()
        self.nutritionTable = nutritionTableRepository()
        self.ingiridents =[]
        
    def addIngirident(self,ingridientName):
        
        ingridients = self.nutritionTable.search(ingridientName)
        
        #if there is exact match than take it!
        exactMatchExists = [s for s in ingridients if s.description.lower()==ingridientName.lower()]
        if len(ingridients) == 1 or exactMatchExists:
            ingridient = ingridients[0]
            measure = ingridient.description + ': ' + str(ingridient.measureDesc) + ' grams'
            amount = input('[' + measure + '] ' +'Quantity in grams:')
            
            readline.set_completer(self.getDateAutocomplete)
            readline.parse_and_bind("tab: complete")
            date = raw_input("Date(dd-mm-yyyy - skip to use today date): ")
            
            if date:
                date = parse(date)
            
            self.ingirident = intakeModel(ingridient.reference,amount,date)
            self.repository.addIntake(self.ingirident)
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
            ingridients.append(ingridient.formatForLogPrint(i.amount))
        
       
        print tabulate(ingridients,headers=["Description","Kcal","Protein","Carbo","Fat","Grams"],tablefmt='orgtbl',numalign="right")
    
    def removeLast(self):
        self.repository.removeLastIntake()
        self.showIntake(None)
    
    def getSimilarIngridients(self, searchTerm):
        ingridients = self.nutritionTable.search(searchTerm)
        return [str(i.description).lower() for i in ingridients]
    
    def getDateAutocomplete(self,text, state):
        base = datetime.datetime.today()
        date_list = [(base - datetime.timedelta(days=x)).date().strftime('%d.%m') for x in range(0, 7)]
            
        return date_list[state]

       