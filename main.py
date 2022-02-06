# C950 PA for Nikolas Butalid (Student ID: 001531753)

# Imports
from csv_handler import *
from distance import *
from trucks import *

my_distance = Distance(create_distance_graph(), create_address_list())
all_packages = create_package_hash()

all_packages.update_address(9, '410 S State St')
all_packages.update_zip(9, '84111')
all_packages.update_city(9, 'Salt Lake City')
all_packages.update_state(9, 'UT')

truck1 = Truck(all_packages)
truck2 = Truck(all_packages)
truck3 = Truck(all_packages)

load_trucks([truck1, truck2, truck3], all_packages)

truck1.deliver_package("8:00 AM")
# for i in [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]:
#     print(all_packages.lookup(i), '\n')
