from hashmap import *
from csv_handler import *
from datetime import datetime
from datetime import timedelta


class Distance:
    def __init__(self, distance_data, address_list):
        self.distance_data = distance_data
        self.address_list = address_list

    def distance_between(self, address1, address2):
        if address1 == '3575 W Valley Central Station bus Loop':
            address1 = '3575 W Valley Central Sta bus Loop'
        if address2 == '3575 W Valley Central Station bus Loop':
            address2 = '3575 W Valley Central Sta bus Loop'

        try:
            if isinstance(address1, int):
                address1_index = address1
            else:
                address1_index = self.find_index(address1)
            if isinstance(address2, int):
                address2_index = address2
            else:
                address2_index = self.find_index(address2)

        except ValueError as e:
            print("Address not found")
            return

        dist_between1 = self.distance_data[address1_index][address2_index]
        dist_between2 = self.distance_data[address2_index][address1_index]

        if dist_between1:
            return float(dist_between1)
        elif dist_between2:
            return float(dist_between2)
        else:
            return 0

    def find_index(self, address):
        if address == '3575 W Valley Central Station bus Loop':
            address = '3575 W Valley Central Sta bus Loop'
        return self.address_list.index(address)

    def min_distance(self, from_address, packages, package_list, start_time, truck_name):
        unvisited = []
        total_dist = 0
        address_set = set()
        timer = start_time

        package_address_list = []

        u = from_address

        for i in package_list:
            address = packages.get_address(i)
            unvisited.append(address)
            if address in address_set:
                for x in package_address_list:
                    if address == x[0]:
                        x[1].append(i)
            else:
                address_set.add(address)
                package_address_list.append([packages.get_address(i), [i]])

        # print(package_address_list)
        # print(address_set)

        while unvisited:
            min_dist = unvisited[0]
            for j in unvisited:
                if j == min_dist:
                    continue
                if (self.distance_between(u, j)) <= self.distance_between(u, min_dist):
                    min_dist = j

            next_address = min_dist
            dist = self.distance_between(u, next_address)

            time_list = []
            for i in package_address_list:
                if next_address in i:
                    time_list = i[1]
                    break

            for x in range(len(time_list)):
                if not x:

                    ot = datetime.strptime(timer, '%I:%M:%S %p')
                    ot += timedelta(minutes=(dist / 18 * 60))

                    old_time = ot.time().strftime('%I:%M:%S %p')
                    timer = old_time
                    packages.update_time(time_list[x], f'Delivered at {old_time}')
                else:
                    ot = datetime.strptime(timer, '%I:%M:%S %p')
                    old_time = ot.time().strftime('%I:%M:%S %p')
                    timer = old_time
                    packages.update_time(time_list[x], f'Delivered at {old_time}')
            total_dist += dist
            u = next_address
            unvisited.remove(min_dist)

        total_dist += self.distance_between(from_address, u)
        # print(f'{truck_name} got back at {timer} and traveled {total_dist} miles')
        # return total_dist
        return [truck_name, timer, total_dist]
