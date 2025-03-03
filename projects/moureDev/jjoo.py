"""
Exerice # 1
The JJOO of Paris have begun!!
Create a program that simulates the celebration of the JJOO of Paris.
the program must allow the registration of events and participants.
will carry out the simulation of the randomly assigned events
and generate a final report all by terminal.
Requirements:
1. Register sports events
2. Register participants
3. Simualte randomly assigned events based on participants
4. assigned medals (gold, silver, bronze) based on the results of the events
5. Show the winners of each events.
6. Show the ranking of the countries based on the medals won.
actions:
1. Register of events
2. Register of participants
3. Simulate events
4. create report
5. exit the program

"""


class Participant:
    def __init__(self, name: str, country: str) -> None:
        self.name = name
        self.country = country

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Participant):
            return False
        return self.name == other.name and self.country == other.country

    def __hash__(self) -> int:
        return hash((self.name, self.country))


class Olympics:
    def __init__(self) -> None:
        self.events = []
        self.participants = {}

    def register_event(self) -> None:
        event: str = input("Enter the name of the event: ").strip()
        if event not in self.events:
            self.events.append(event)
            print(f"{event} has been registered")
        else:
            print(f"{event} is already registered")

    def register_participant(self) -> None:
        if not self.events:
            print("There are no events registered")
            return

        name: str = input("Enter the name of the participant: ").strip()
        country: str = input("Enter the country of the participant: ").strip()
        participant: Participant = Participant(name, country)

        print("Events available: ")
        for index, event in enumerate(self.events):
            print(f"{index + 1}. {event}")

        event_choise = (
            int(input("Select the event number to assign to the participant: ")) - 1
        )

        if event_choise > 0 or event_choise < len(self.events):
            event = self.events[event_choise]

            if participant in self.participants[event]:
                print(
                    f"{participant.name} of {participant.country} is already registered in {event}"
                )
            else:
                self.participants[event].append(participant)
                print(
                    f"{participant.name} of {participant.country} has been registered in {event}"
                )
        else:
            print("Invalid event number, try again")


def main() -> None:
    olympics: Olympics = Olympics()
    while True:
        print("Welcome to the JJOO of Paris!!")
        print("1. Register of events")
        print("2. Register of participants")
        print("3. Simulate events")
        print("4. create report")
        print("5. exit the program")
        option = input("Select an option: ")

        match option:
            case "1":
                olympics.register_event()
            case "2":
                olympics.register_participant()
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Goodbye!!")
                break
            case _:
                print("Invalid option, try again")


if __name__ == "__main__":
    main()
