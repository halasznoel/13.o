import calendar

def naptar():
    ev = int(input("Kérem adja meg az évet: "))
    honap = int(input("Kérem adja meg az hónapot: "))
    cal = calendar.TextCalendar(calendar.MONDAY)
    calmonth = cal.formatmonth(ev,honap)
    print(calmonth)
naptar()
    