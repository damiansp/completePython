from datetime import date
now = date.today()
print(now) # YYYY-MM-DD

birthday = date(1976, 11, 3)
age = now - birthday
print(age)      # 16114 days, 0:00:00
print(age.days) # 16144
