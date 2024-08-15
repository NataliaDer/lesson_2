def month_to_season(month_number): 
    if (month_number ==12 or month_number ==1 or month_number ==2 ):
        print("Зима")
    if (month_number ==3 or month_number ==4 or month_number ==5 ):
        print("Весна")
    if (month_number ==6 or month_number ==7 or month_number ==8 ):
        print("Лето")
    if (month_number ==9 or month_number ==10 or month_number ==11 ):
        print("Осень")
month_number=int(input())
month_to_season(month_number)
