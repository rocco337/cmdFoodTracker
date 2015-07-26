from repositories.intakeRepository import intakeRepository
from repositories.nutritionTableRepository import nutritionTableRepository
import datetime,itertools,collections
from tabulate import tabulate
import handlersCommon

class statisticsHandler:
    def __init__(self):
        self.repository = intakeRepository()
        self.nutritionTable = nutritionTableRepository()
    
    def showLast7daysStats(self):
         
        today = datetime.date.today()
        weekAgo = today - datetime.timedelta(days=7)
        
        intakes = self.repository.getIntakeListDateRangeFilter(weekAgo,today)
        statistics = collections.OrderedDict()
        for i in intakes:
            date = i.timestamp.date()
            if date not in statistics:
                statistics[date] = dailiyStats(date)
            
            ingridient = self.nutritionTable.searchByReference(i.ingridientReference)
            quantity =(i.amount/float(100))
            
            statistics[date].kcalTotal += int(ingridient.kcal*quantity)
            statistics[date].proteinTotal += int(ingridient.protein*quantity)
            statistics[date].carboTotal += int(ingridient.carbo*quantity)
            statistics[date].fatTotal += int(ingridient.fat*quantity)
        
        statistics=handlersCommon.reverseDict(statistics)
        print tabulate(statistics.values(),headers=["Date","Kcal","P","C","F"],tablefmt='orgtbl',numalign="right")
        
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

