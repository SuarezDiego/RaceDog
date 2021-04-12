from datetime import date
from result import Result
from race import Race
from event import Event
from dog import Dog
from owner import Owner


def test():
    date1 = date(1999, 5, 5)
    date2 = date(2000, 5, 5)
    date3 = date(2002, 5, 1)
    date4 = date(2022, 5, 1)
    date5 = date(2022, 5, 2)
    dog1 = Dog("firulais", date1, "galgo")
    dog2 = Dog("cholo", date2, "pitbull")
    dogs = [dog1, dog2]
    owner1 = Owner("Diego", "123456789-1", [dog1, dog2])
    dog3 = Dog("cleo", date3, "golden retriever")
    owner1.add_dog(dog3)
    dogs = owner1.dogs
    race1 = Race(date4, dogs)
    race2 = Race(date5, dogs)
    races = [race1, race2]
    event1 = Event(date4, date5, "Santiago", races)
    race1.run_race()
    positions_table = race1.make_positions_table()
    print(positions_table)

def main():
    print("test")
    test()

if __name__=="__main__":
    main()

