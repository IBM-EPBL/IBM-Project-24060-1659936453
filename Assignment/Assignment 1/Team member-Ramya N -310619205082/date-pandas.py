import datetime
import pandas as pd
 
# initializing date
test_date = datetime.datetime.strptime("01-01-2023", "%d-%m-%Y")
 
# initializing periods
periods = datetime.datetime.strptime("02-02-2023", "%d-%m-%Y")
 
date_generated = pd.date_range(test_date, periods)
print(date_generated.strftime("%d-%m-%Y"))

