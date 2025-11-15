import random

Etap 1 – Wyświetlanie jednej prognozy

def wyswietl_pojedyncza_prognoze(): miasto = input("Podaj nazwę miasta: ") temperatura = input("Podaj temperaturę: ") print(f"Miasto: {miasto}, Temperatura: {temperatura}°C")

Etap 2 – Losowa prognoza

warunki_pogodowe = ["Słonecznie", "Deszczowo", "Zachmurzenie"]

def losowa_prognoza(miasto): temperatura = random.randint(-10, 35) warunki = random.choice(warunki_pogodowe) return {"miasto": miasto, "temperatura": temperatura, "warunki": warunki}

Etap 3 – Lista miast

def generuj_dla_listy(): miasta = input("Wpisz miasta oddzielone przecinkiem: ").split(',') miasta = [m.strip() for m in miasta]

prognozy = [losowa_prognoza(m) for m in miasta]

print("\n--- Tabela prognoz ---")
print(f"{'Miasto':<15}{'Temperatura':<15}{'Warunki'}")
for p in prognozy:
    print(f"{p['miasto']:<15}{p['temperatura']:<15}{p['warunki']}")

return prognozy

Etap 4 – Funkcje

def generuj_prognoze(miasto): return losowa_prognoza(miasto)

def pokaz_prognozy(lista_miast): prognozy = [generuj_prognoze(m) for m in lista_miast] for p in prognozy: print(f"Miasto: {p['miasto']}, Temperatura: {p['temperatura']}°C, Warunki: {p['warunki']}") return prognozy

Etap 5 – Analiza danych

def analiza(prognozy): temperatury = [p['temperatura'] for p in prognozy] srednia = sum(temperatury) / len(temperatury) max_temp = max(prognozy, key=lambda x: x['temperatura']) min_temp = min(prognozy, key=lambda x: x['temperatura'])

print("\n--- Analiza temperatur ---")
print(f"Średnia temperatura: {srednia:.2f}°C")
print(f"Najwyższa temperatura: {max_temp['temperatura']}°C, miasto: {max_temp['miasto']}")
print(f"Najniższa temperatura: {min_temp['temperatura']}°C, miasto: {min_temp['miasto']}")

return srednia, max_temp, min_temp

Etap 6 – Zapis do pliku

def zapisz_do_pliku(prognozy, analiza_danych): with open("raport.txt", "w", encoding="utf-8") as f: f.write("--- Raport pogodowy ---\n\n") for p in prognozy: f.write(f"Miasto: {p['miasto']}, Temp: {p['temperatura']}°C, Warunki: {p['warunki']}\n")

srednia, max_temp, min_temp = analiza_danych

    f.write("\n--- Analiza ---\n")
    f.write(f"Średnia temperatura: {srednia:.2f}°C\n")
    f.write(f"Najwyższa temperatura: {max_temp['temperatura']}°C, {max_temp['miasto']}\n")
    f.write(f"Najniższa temperatura: {min_temp['temperatura']}°C, {min_temp['miasto']}\n")

print("\nRaport zapisany do pliku raport.txt")

Główna logika programu

def main(): print("Generator Raportów Pogodowych") prognozy = generuj_dla_listy() analiza_danych = analiza(prognozy) zapisz_do_pliku(prognozy, analiza_danych)

if name == "main": main()
