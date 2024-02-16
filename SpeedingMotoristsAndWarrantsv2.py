"""Speeding Motorists And Warrants v2
 Fixed typo errors, Removed the 'class' code and replaced with
 definitive functions to make the program much simpler and easier
 to understand.
Created loop in which type stop to end"""


def calculate_fine(speed):
    if speed < 10:
        return 30
    elif 10 <= speed < 15:
        return 80
    elif 15 <= speed < 20:
        return 120
    elif 20 <= speed < 25:
        return 170
    elif 25 <= speed < 30:
        return 230
    elif 30 <= speed < 35:
        return 300
    elif 35 <= speed < 40:
        return 400
    elif 40 <= speed < 45:
        return 510
    else:
        return 630


def process_speeder(speeders, name, speed):
    fine = calculate_fine(speed)
    speeders.append({'Name': name, 'Amount Over Limit': speed, 'Fine': fine})
    return fine


def check_warrant(name):
    wanted_list = ['James Wilson', 'Helga Norman', 'Zachary Conroy']
    if name in wanted_list:
        print(f'{name.upper()} - WARRANT TO ARREST')


def display_summary(speeders, total_fines):
    print('\nSummary of the day:')
    print(f'Total fines: {len(speeders)}')
    for idx, speeder in enumerate(speeders, start=1):
        print(f"{idx}) Name: {speeder['Name']} Amount Over Limit: {speeder['Amount Over Limit']}")
    print(f'Total amount of fines: ${total_fines}')


def main():
    speeders = []
    total_fines = 0

    while True:
        name = input("Welcome! Please enter the name of speeder (Type 'stop' to end input mode): ")
        if name.lower() == 'stop':
            break

        speed = int(input("Enter the amount over speed limit: "))
        check_warrant(name)

        fine = process_speeder(speeders, name, speed)
        total_fines += fine
        print(f' The speeder {name} will be fined ${fine}\n! Naughty!')

    display_summary(speeders, total_fines)


if __name__ == "__main__":
    main()
