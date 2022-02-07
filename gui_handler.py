from csv_handler import *
from distance import *
from trucks import *
from datetime import datetime


def start_gui():
    all_packages = create_package_hash()

    all_packages.update_address(9, '410 S State St')
    all_packages.update_zip(9, '84111')
    all_packages.update_city(9, 'Salt Lake City')
    all_packages.update_state(9, 'UT')

    truck1 = Truck(all_packages)
    truck2 = Truck(all_packages)
    truck3 = Truck(all_packages)

    load_trucks([truck1, truck2, truck3], all_packages)

    truck1_dist = truck1.deliver_package("8:00:00 AM", 'Truck 1')
    truck2_dist = truck2.deliver_package("9:05:00 AM", 'Truck 2')
    truck3_dist = truck3.deliver_package("10:25:00 AM", 'Truck 1')

    truck1_package_set = set(truck1.get_package_list())
    truck2_package_set = set(truck2.get_package_list())
    truck3_package_set = set(truck3.get_package_list())

    truck1_name = truck1_dist[0]
    truck1_time = truck1_dist[1]
    truck1_miles = truck1_dist[2]

    truck2_name = truck2_dist[0]
    truck2_time = truck2_dist[1]
    truck2_miles = truck2_dist[2]

    truck3_name = truck3_dist[0]
    truck3_time = truck3_dist[1]
    truck3_miles = truck3_dist[2]

    start_time = datetime.strptime('8:00', '%H:%M')
    start_time1 = '8:00 AM'
    start_time2 = '9:05 AM'
    start_time3 = '10:25 AM'

    error_message = ('\nEnter...\n'
                     '"1": Check total milage and times of all trucks\n'
                     '"2": Check status of all packages at a given time\n'
                     '"exit": to close the program at any time')

    print('Welcome to the WGUPS Package Tracker \n'
          'Enter...\n'
          '"1": Check total milage and times of all trucks\n'
          '"2": Check status of all packages at a given time\n'
          '"exit": to close the program at any time')
    while True:
        user_input = input()
        if user_input == 'exit':
            print('Closing WGUPS Package Tracker...')
            break
        elif user_input == '1':
            print(
                f'{truck1_name} left at {start_time1} returned to the hub at {truck1_time} and traveled {truck1_miles:.2f} miles')
            print(
                f'{truck2_name} left at {start_time2} returned to the hub at {truck2_time} and traveled {truck2_miles:.2f} miles')
            print(
                f'{truck3_name} left at {start_time3} returned to the hub at {truck3_time} and traveled {truck3_miles:.2f} miles')
            print(f'Total distance traveled by all trucks was {(truck1_miles + truck2_miles + truck3_miles):.2f}')

            print(error_message)

        elif user_input == '2':
            try:
                print('Please enter a time to check the statuses of all packages\n'
                      'Time must be in 24 hour time and be after 8:00 (8 AM) and before 24:00 (12 AM)\n'
                      'Please use the HH:MM format (e.g., 13:00):')
                user_time = input()
                if user_time == 'exit':
                    print('Closing WGUPS Package Tracker...')
                    break
                user_time = datetime.strptime(user_time, '%H:%M')
                if user_time <= start_time:
                    print('Input invalid. Please enter a time after 8:00 and before 24:00')
                    print(error_message)

                else:
                    get_package_times(user_time, all_packages,
                                      [truck1_package_set, truck2_package_set, truck3_package_set])
            except ValueError:
                print('Input invalid. Please enter a time between 8:00 and 24:00')
                print(error_message)
        else:
            print("Invalid input. Try again")
            print(error_message)


def get_package_times(get_time, packages, truck_sets):
    truck1_start = datetime.strptime('8:00', '%H:%M')
    truck2_start = datetime.strptime('9:05', '%H:%M')
    truck3_start = datetime.strptime('10:25', '%H:%M')

    for i in range(1, 41):
        package_info = packages.get_package(i)
        package_id = package_info[0]
        package_address = package_info[1][0]
        package_delivery_time = package_info[1][4]
        package_status = package_info[1][7]

        package_time = packages.get_status(i)[13:]
        if get_time < datetime.strptime(package_time, '%I:%M:%S %p'):
            if package_id in truck_sets[0]:
                if get_time >= truck1_start:
                    package_status = "En Route"
                else:
                    package_status = "At the hub"
            elif package_id in truck_sets[1]:
                if get_time >= truck2_start:
                    package_status = "En Route"
                else:
                    package_status = "At the hub"
            elif package_id in truck_sets[2]:
                if get_time >= truck3_start:
                    package_status = "En Route"
                else:
                    package_status = "At the hub"

        print(
            f'Package ID: {package_id}, Address: {package_address}, '
            f'Delivery Time: {package_delivery_time}, Status: {package_status}')

    print('\nEnter...\n'
          '"1": Check total milage and times of all trucks\n'
          '"2": Check status of all packages at a given time\n'
          '"exit": to close the program at any time')
