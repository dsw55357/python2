"""1. Napisz program, który wczytuje datę urodzenia użytkownika (w formacie RRRR-MMDD)
i oblicza jego wiek w dniach, korzystając z modułu datetime . Obsłuż błędy
związane z nieprawidłowym formatem daty."""

"""1. Moduł datetime:
Importowanie: from datetime import datetime, timedelta
Wczytywanie daty: datetime.strptime(date_string, format)
Obliczanie różnicy między datami: (date1 - date2).days"""

from datetime import datetime, timedelta
import pytz

def main():
    try:
        date_string = "2024-0101"
        format_string = "%Y-%m%d"
        print("\nWariat 1 - prawidlowy format daty: {}\n".format(date_string))
        birth_date = datetime.strptime(date_string, format_string)
        today = datetime.today()
        age_in_days = (today - birth_date).days
        print(">> Age {} (in days)". format(age_in_days))

        # data z błędem
        date_string = "2024-0101x"
        format_string = "%Y-%m%d"
        print("\nWariat 2 - nieprawidlowy format daty: {}\n".format(date_string))
        birth_date = datetime.strptime(date_string, format_string)
        today = datetime.today()
        age_in_days = (today - birth_date).days
        print(">> Age {} (in days)". format(age_in_days))


    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()