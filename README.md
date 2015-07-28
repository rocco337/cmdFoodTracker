###Intake tracker

####1. Intro

Intake tracker is command line app that you can use to track food and liquids that you take in during a day.
Other than trackin intake it can show you various information based on enterd data.

####2. Basic information

Before you start to track you daily food intake you need to provide some basic info like name, weight, height.

* Read inputs
* Store to DB

####3. Food intake

Enter your intake in following format <ingirident name> <unit> <measure>
During entering each argument you can press tab to get possible all arguments for entered characters. 
There is no possiblity to edit entered items but you can remove last entered item if you made a mistake.

On each entry try to find ingridient in nutrition table and save it's values. If there are more records in table that contains that ingirident then force user to choose one.

####4. Daily status and log

Show aggregation of consumed nutritients every day. By default load last 7 days and order them from current to 7 days agoo. Add possiblity to add date range for filtering.
When looking in log load intakes for todaya and if date provided than load intakes for given day.

####5. Statistics
####6. Refactor and todo notes
* add fibers and split fats
* http://missionripped.com/tools/daily-caloric-calculator/