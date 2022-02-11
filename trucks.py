from csv_handler import *
from distance import *


# This class is used for creating trucks
# This class holds a list of the package ID's for that specific truck, the max speed,
# max number of packages it can hold, all of the packages, and a distance object
class Truck:
    # Space Complexity: O(N) because of the packages list
    def __init__(self, all_packages):
        self.packages = []
        self.__max = 16
        self.speed = 18
        self.hub = '4001 South 700 East'
        self.all_packages = all_packages
        self.truck_distance = Distance(create_distance_graph(), create_address_list())

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def load_package(self, packages):
        self.packages = packages

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_package_list(self):
        return self.packages

    # Time Complexity: O(N^3) because of the min distance function
    # Space Complexity: O(1)
    # Return: Returns a list from the min distance function
    def deliver_package(self, time, truck_name):
        for i in self.packages:
            self.all_packages.update_time(i, 'En Route')
        return self.truck_distance.min_distance(self.hub, self.all_packages, self.packages, time, truck_name)


# This function sorts out the packages into three different delivery using the restraints from the project
# guidelines. The trucks that have certain restrictions are dealt with manually and the rest of the packages
# are automatically loaded in the trucks with empty space. Truck 1's packages are chosen to make sure the packages
# that must be delivered the earliest are delivered first

# Time Complexity: On average is O(N) but at worst case is O(N^2) because of the get
# package function has worst case of O(N)
# Space Complexity: O(N) because of the truck package lists
def load_trucks(trucks, all_packages):
    package_list = all_packages.get_package_id_list()
    truck_packages1 = []
    truck_packages2 = []
    truck_packages3 = []

    # Time Complexity: On average is O(N) but at worst is O(N^2) because of the worst case
    # of the get package function. See 'hashmap.py' for more details about .get_package
    # Space Complexity: O(N) because of the package lists
    for i in package_list:
        if all_packages.get_package(i)[1][4] == '9:00 AM':
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[1][4] == '10:30 AM' and len(truck_packages1) < 16 and not \
                all_packages.get_package(i)[1][6]:
            truck_packages1.append(i)
            package_list[i - 1] = 0
        elif all_packages.get_package(i)[0] == 26:
            truck_packages2.append(i)
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

    # Time Complexity: On average is O(N) but at worst is O(N^2) because of the worst case
    # of the get package function
    # Space Complexity: O(N) because of the package lists
    for j in package_list:
        if j and not all_packages.get_package(j)[0] == 9:
            if all_packages.get_package(j)[1][4] == '10:30 AM' and (len(truck_packages2) < 16):
                truck_packages2.append(j)
                package_list[j - 1] = 0

    # Time Complexity: On average is O(N) but at worst is O(N^2) because of the worst case
    # of the get package function
    # Space Complexity: O(N) because of the package lists
    for j in package_list:
        if j and not all_packages.get_package(j)[0] == 9:
            if all_packages.get_package(j)[1][4] == 'EOD' and (len(truck_packages2) < 16):
                truck_packages2.append(j)
                package_list[j - 1] = 0

    # Time Complexity: O(N) because of for loop
    # Space Complexity: O(N) because of package lists
    for x in package_list:
        if x:
            truck_packages3.append(x)
            package_list[x - 1] = 0

    trucks[0].load_package(truck_packages1)
    trucks[1].load_package(truck_packages2)
    trucks[2].load_package(truck_packages3)
