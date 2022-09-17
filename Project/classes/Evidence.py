from .Person import Person

class Evidence:
    
        #všechni pojištěnci
    def __init__(self):
        self.policyholders = []
        self.policyholders.append(Person("Daniel", "Vajdík", 31, "606256089"))
        self.policyholders.append(Person("Jan", "Novák", 50, "777555333"))

        #menu
    def menu(self):
        print("\nVyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("0 - Konec\n")

        #vyžaduje zadání čísla, od 0 do tří
        while True:
            try:
                choice = int(input("zadej te výběr: "))
            except ValueError:
                print("výběr musí být číslo")
                continue
            else:
                if choice < 0 or choice > 3:
                    print("zadejte číslo z menu")
                    continue
                else:
                    return choice
    
        #přídá pojistníka
    def addPojistenec(self):
        firstname = input("Zadej jméno pojištěného:\n")
        surname = input("Zadej příjmení pojištěného:\n")
        age = int(input("Zadej věk:\n"))
        number = input("Zadej telefonní číslo:")
        self.policyholders.append(Person(firstname, surname, age, number))
        print("Nový pojištěnec přidán")
        input("Pokračuj te libovolnou klávesou...\n")

        #vypíše pojistníky
    def printEvidence(self):
        for person in self.policyholders:
            print(person)
        input("Pokračuj te libovolnou klávesou...\n")
        
        #vyhledá pojistníka
    def search(self):
        searchString = input("Zadejte hledané jméno a nebo příjmení:\n")
        for person in self.policyholders:
            if person.firstname == searchString or person.surname == searchString:
                print(person)
        input("Pokračujte libovolnou klávesou...\n")
