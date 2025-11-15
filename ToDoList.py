import os from datetime import datetime

-----------------------------

WCZYTYWANIE I ZAPIS PLIKU

-----------------------------

def load_tasks(filename="tasks.txt"): tasks = [] if not os.path.exists(filename): return tasks

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        # format: tytuł|priorytet|status|deadline
        parts = line.split("|")
        if len(parts) == 4:
            title, priority, done, deadline = parts
            tasks.append({
                "title": title,
                "priority": priority,
                "done": done == "1",
                "deadline": deadline if deadline != "-" else None
            })
return tasks

def save_tasks(tasks, filename="tasks.txt"): with open(filename, "w", encoding="utf-8") as f: for t in tasks: done = "1" if t["done"] else "0" deadline = t["deadline"] if t["deadline"] else "-" f.write(f"{t['title']}|{t['priority']}|{done}|{deadline}\n")

-----------------------------

FUNKCJE PROGRAMU

-----------------------------

def dodaj_zadanie(lista): tytul = input("Podaj tytuł zadania: ") priorytet = input("Priorytet (wysoki/średni/niski): ").lower() deadline = input("Termin wykonania (YYYY-MM-DD) lub Enter aby pominąć: ").strip()

if deadline == "":
    deadline = None

lista.append({
    "title": tytul,
    "priority": priorytet,
    "done": False,
    "deadline": deadline
})
print("Dodano zadanie!\n")

def pokaz_zadania(lista): if not lista: print("Brak zadań!\n") return

print("\n--- LISTA ZADAŃ ---")
for i, t in enumerate(lista):
    status = "✓" if t["done"] else " "
    deadline = t["deadline"] if t["deadline"] else "-"
    print(f"{i}. [{status}] {t['title']} (priorytet: {t['priority']}, termin: {deadline})")
print()

def oznacz_jako_wykonane(lista): try: nr = int(input("Podaj numer zadania do oznaczenia jako wykonane: ")) lista[nr]["done"] = True print("Zadanie oznaczono jako wykonane.\n") except: print("Błędny numer zadania!\n")

def usun_zadanie(lista): try: nr = int(input("Podaj numer zadania do usunięcia: ")) lista.pop(nr) print("Usunięto zadanie.\n") except: print("Błędny numer zadania!\n")

def sortuj_zadania(lista): priorytet_map = {"wysoki": 0, "średni": 1, "niski": 2} lista.sort(key=lambda x: priorytet_map.get(x["priority"], 3)) print("Posortowano po priorytecie!\n")

def pokaz_deadline(lista): def parse_date(d): try: return datetime.strptime(d, "%Y-%m-%d") except: return datetime.max

posortowane = sorted(
    [t for t in lista if t["deadline"]],
    key=lambda x: parse_date(x["deadline"])
)

print("\n--- NADCHODZĄCE DEADLINY ---")
for t in posortowane:
    status = "✓" if t["done"] else " "
    print(f"[{status}] {t['title']} (termin: {t['deadline']})")
print()

-----------------------------

PĘTLA GŁÓWNA PROGRAMU

-----------------------------

def main(): tasks = load_tasks() print("Wczytano zadania.\n")

while True:
    print("Dostępne komendy:")
    print(" dodaj | lista | zrob | usun | sort | deadline | save | exit")

    cmd = input("> ").lower()

    if cmd == "dodaj":
        dodaj_zadanie(tasks)
    elif cmd == "lista":
        pokaz_zadania(tasks)
    elif cmd == "zrob":
        oznacz_jako_wykonane(tasks)
    elif cmd == "usun":
        usun_zadanie(tasks)
    elif cmd == "sort":
        sortuj_zadania(tasks)
    elif cmd == "deadline":
        pokaz_deadline(tasks)
    elif cmd == "save":
        save_tasks(tasks)
        print("Zapisano do pliku.\n")
    elif cmd == "exit":
        save_tasks(tasks)
        print("Zapisano i zakończono program.")
        break
    else:
        print("Nieznana komenda!\n")

if name == "main": main()
