# C950 PA for Nikolas Butalid (Student ID: 001531753)

# Imports
from csv_handler import *
from distance import *

my_distance = Distance(create_distance_graph(), create_address_list())

all_packages = create_package_hash()

print(my_distance.min_distance('4001 South 700 East', all_packages, [1, 2, 3, 4, 5]))
