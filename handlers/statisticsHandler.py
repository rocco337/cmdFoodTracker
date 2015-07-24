from repositories.intakeRepository import intakeRepository
from repositories.nutritionTableRepository import nutritionTableRepository
import datetime,itertools 
from tabulate import tabulate

class statisticsHandler:
    def __init__(self):
        self.repository = intakeRepository()
        self.nutritionTable = nutritionTableRepository()
    
    def showLast7daysStats(self):
         
        today = datetime.date.today()
        weekAgo = today - datetime.timedelta(days=7)
        
        ingridients = self.repository.getIntakeListDateRangeFilter(weekAgo,today)
        statistics = {}
        for i in ingridients:
            date = i.timestamp.date()
            if date not in statistics:
                statistics[date] = dailiyStats(date)
            
            ingridient = self.nutritionTable.searchByReference(i.ingridientReference)
            
            statistics[date].kcalTotal += ingridient['Energ_Kcal']
            statistics[date].proteinTotal += ingridient['Protein']
            statistics[date].carboTotal += ingridient['Carbohydrt']
            statistics[date].fatTotal += ingridient['Lipd_Tot']
        
        print tabulate(statistics.values(),headers=["Date","Kcal","P","C","F"])
        
class dailiyStats:
    def __init__(self,date):
        self.date = date
        self.kcalTotal = 0
        self.proteinTotal = 0
        self.carboTotal = 0
        self.fatTotal = 0
    
    #add iterator to support printing with tabulate
    def __iter__(self):
        return iter([self.date,self.kcalTotal,self.proteinTotal,self.carboTotal,self.fatTotal])

