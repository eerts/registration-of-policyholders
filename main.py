from tridy.Evidence import Evidence

#možnosti volby
def main():
    evidence = Evidence()
    while True:
        choice = evidence.menu()
        if choice == 0:
            print("\n\nUkončuji...")
            break
        elif choice == 1:
            evidence.addPojistenec()
        elif choice == 2:
            evidence.printEvidence()
        else:
            evidence.search()

#vypíše úvod 
if __name__ == '__main__':
    print("----------------------------")
    print("Evidence pojištěných")
    print("----------------------------")
    main()

