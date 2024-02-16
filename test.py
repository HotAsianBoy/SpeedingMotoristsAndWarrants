class SpeedingTicketTracker:
    def __init__(self):
        self.speeders = []
        self.total_fines = 0

    def calculate_fine(self, speed):
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

    def process_speeder(self, name, speed):
        fine = self.calculate_fine(speed)
        self.total_fines += fine
        self.speeders.append({'Name': name, 'Amount Over Limit': speed, 'Fine': fine})

    def check_warrant(self, name):
        wanted_list = ['James Wilson', 'Helga Norman', 'Zachary Conroy']
        if name in wanted_list:
            print(f'{name.upper()} - WARRANT TO ARREST')

    def display_summary(self):
        print('\nSummary of the day:')
        print(f'Total fines: {len(self.speeders)}')
        for idx, speeder in enumerate(self.speeders, start=1):
            print(f"{idx}) Name: {speeder['Name']} Amount Over Limit: {speeder['Amount Over Limit']}")
        print(f'Total amount of fines: ${self.total_fines}')


def main():
    ticket_tracker = SpeedingTicketTracker()

    while True:
        name = input("Enter name of speeder (Type 'stop' to end input mode): ")
        if name.lower() == 'stop':
            break

        speed = int(input("Enter the amount over speed limit: "))
        ticket_tracker.check_warrant(name)

        ticket_tracker.process_speeder(name, speed)
        print(f'{name} to be fined ${ticket_tracker.speeders[-1]["Fine"]}\n')

    ticket_tracker.display_summary()


if __name__ == "__main__":
    main()
