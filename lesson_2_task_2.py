def is_year_leap (year):
   
    if year % 4 ==0:
        print ("Ваш год", year,": True")
    else:
        print ("Ваш год", year, ": False") 
year=int(input())
print(is_year_leap(year))
           