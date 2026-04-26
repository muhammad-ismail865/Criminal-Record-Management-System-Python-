class Criminal:
    def __init__(self):
        self.name = []
        self.id = []
        self.crime = []
        self.punish = []

    def add(self, id, name, crime, punish):
        self.name.append(name)
        self.id.append(id)
        self.crime.append(crime)
        self.punish.append(punish)

    def display(self):
        print("Criminal Record")
        if not self.id:
            print("Criminal Record empty")
        else:
            for i in range(len(self.id)):
                print("ID:", self.id[i])
                print("Name:", self.name[i])
                print("Crime:", self.crime[i])
                print("Punish:", self.punish[i])
                print("------------------")

    def search(self, id):
        found = False
        for i in range(len(self.id)):
            if id == self.id[i]:
                print("Record Found:")
                print("ID:", self.id[i])
                print("Name:", self.name[i])
                print("Crime:", self.crime[i])
                print("Punish:", self.punish[i])
                found = True
                break
        if not found:
            print("No record found")

c1 = Criminal()

while True:
    print("\n*** Criminal Record System ***")
    print("1.Add record")
    print("2.View record")
    print("3.Search record")
    print("4.Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        id = int(input("Enter Criminal id: "))
        name = input("Enter name: ")
        crime = input("Enter Crime: ")
        punish = input("Enter punishment in years: ")

        c1.add(id, name, crime, punish)
        print("Record Added successfully")

    elif choice == 2:
        c1.display()

    elif choice == 3:
        id = int(input("Enter the id: "))
        c1.search(id)

    elif choice == 4:
        print("You exit successfully")
        break
    else:
        print("Invalid Choice")