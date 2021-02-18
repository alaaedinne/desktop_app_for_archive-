import datetime

CurrentDate = datetime.datetime.now()
print(CurrentDate)

ExpectedDate = "9/8/2015 4:00"
ExpectedDate = datetime.datetime.strptime(ExpectedDate, "%d/%m/%Y %H:%M")
print(ExpectedDate)

if CurrentDate > ExpectedDate:
    print("Date missed")
else:
    print("Date not missed")