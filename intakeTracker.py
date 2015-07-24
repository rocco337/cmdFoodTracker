#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from handlers.intakeHandler import intakeHandler
from handlers.userInfromationHandler import userInfromationHandler
from handlers.statisticsHandler import statisticsHandler

import datetime
import argcomplete,argparse,readline

class main:
    
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.intakeHandler=intakeHandler()
        self.statisticsHandler = statisticsHandler()
        
        self.parser.add_argument('-a','-add', action='store_true', dest='isIntake', help='Enter your ingridient name')
        self.parser.add_argument('-i','--info', action='store_true', dest='isInfo', default=False, help='Information about user')
        self.parser.add_argument('-l','--log', help="Show intake log by date - format dd-mm-yyyy (default date is today)", dest='logDate', action='store',const=str(datetime.date.today()),nargs='?')
        self.parser.add_argument('-s','--stats', action='store_true', dest='isStatistics', default=False, help='Show intake statistics for last 7 days')
        self.parser.add_argument('-r','--remove', action='store_true', dest='isRemoveLast', default=False, help='Remove last item')
        
        argcomplete.autocomplete(self.parser)
        self.args = self.parser.parse_args()
        
    def getSimilarIngridients(self,text, state):
         return (self.intakeHandler.getSimilarIngridients(text))[state]
               
        
    def start(self):
        if self.args.isInfo:
            userHandler = userInfromationHandler()
            userHandler.readPersonalData()
        elif self.args.isIntake:
            completer = argcomplete.CompletionFinder(self.parser)
            readline.set_completer_delims("")
            readline.set_completer(self.getSimilarIngridients)
            readline.parse_and_bind("tab: complete")
            ingridient = raw_input("Ingridient name: ")
            if ingridient:
                self.intakeHandler.addIngirident(ingridient)
        elif self.args.logDate:
            self.intakeHandler.showIntake(self.args.logDate)
        elif self.args.isRemoveLast:
            self.intakeHandler.removeLast()
        elif self.args.isStatistics:
            self.statisticsHandler.showLast7daysStats()
        else:
            self.parser.print_help()

main().start()
