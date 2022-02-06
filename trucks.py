from hashmap import *
from distance import *


class Truck:
    def __init__(self, all_packages):
        self.packages = []
        self.__max = 16
        self.speed = 18
        self.hub = '4001 South 700 East'
        self.all_packages = all_packages
        self.truck_distance = Distance(create_distance_graph(), create_address_list())

    def load_package(self, packages):
        self.packages = packages

    def deliver_package(self, time):
        for i in self.packages:
            self.all_packages.update_time(i, time, 'En Route')
        print(self.truck_distance.min_distance(self.hub, self.all_packages, self.packages))


def load_trucks(trucks, all_packages):
    package_list = all_packages.get_package_id_list()
    truck_packages1 = []
    truck_packages2 = []
    truck_packages3 = []

    for i in package_list:
        if all_packages.get_package(i)[1][4] == '9:00 AM':
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[1][4] == '10:30 AM' and len(truck_packages1) < 16 and not \
                all_packages.get_package(i)[1][6]:
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[1][6] == 'Can only be on truck 2':
            truck_packages2.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[0] == 19:
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif 'Must' in all_packages.get_package(i)[1][6]:
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[1][4] == 'EOD' and len(truck_packages1) < 16 and not \
                all_packages.get_package(i)[1][6]:
            truck_packages1.append(i)
            package_list[i - 1] = 0

    for j in package_list:
        if j and not all_packages.get_package(j)[0] == 9:
            if all_packages.get_package(j)[1][4] == '10:30 AM' and (len(truck_packages2) < 16):
                truck_packages2.append(j)
                package_list[j - 1] = 0

    for j in package_list:
        if j and not all_packages.get_package(j)[0] == 9:
            if all_packages.get_package(j)[1][4] == 'EOD' and (len(truck_packages2) < 16):
                truck_packages2.append(j)
                package_list[j - 1] = 0

    for x in package_list:
        if x:
            truck_packages3.append(x)
            package_list[x - 1] = 0

    trucks[0].load_package(truck_packages1)
    trucks[1].load_package(truck_packages2)
    trucks[2].load_package(truck_packages3)
