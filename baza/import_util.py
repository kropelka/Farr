#from . import models
import csv

'''
wymagany format:
nazwa_firmy, wlasciciel, adres, telefon
'''
def import_csv_to_db(file):
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            nazwa = row[0]
            print('Nazwa firmy: ' + nazwa)
            wlasciciel_dane = row[1].split(' ')
            adres = row[2].split(' ')
            telefon = row[3]
            if len(wlasciciel_dane)>1:
                print("Wlasciciel - imie: " + wlasciciel_dane[0] + ", nazwisko: " +
                      wlasciciel_dane[1])
            if len(adres) > 0:
                if len(adres) >= 3:
                    print("Adres - [%s] [%s] [%s]" %
                          (adres[0], ' '.join(adres[1:-1]), adres[-1] ))



if __name__ == "__main__":
    import_csv_to_db("test.csv")
