
expenses = []

def add_expense():
    description = input("Description: ")
    amount = float(input("Montant: "))
    expenses.append({"description": description, "amount": amount})
    print("Depense ajoutee !")

def show_expenses():
    if not expenses:
        print("Aucune depense enregistree.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total : {total:.2f}")

def delete_expense():
    if not expenses:
        print("Aucune depense a supprimer.")
        return
    show_expenses()
    try:
        choice = int(input("Numero de la depense a supprimer : "))
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Deleted: {removed['description']}")
        else:
            print("Numero invalide.")
    except ValueError:
        print("Veuillez entrer un numero valide.")

def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Delete an expense")
        choice = input("Votre choix : ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            break
        elif choice == "5":
            delete_expense()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()