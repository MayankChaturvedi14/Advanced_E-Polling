import datetime
from dateutil.relativedelta import relativedelta

one_year_from_now = datetime.datetime.now().strftime("%d/%m/%Y")
print(one_year_from_now)