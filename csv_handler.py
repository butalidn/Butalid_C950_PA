from hashmap import *
import csv


# This function creates a hashmap object
# It reads from the Package File.csv and uses the package id as the key
# for the hashmap items.
# Columns 1-6 are used as the value for the hashmap
# for each package id.
# Time Complexity: O(N) because the csv reader goes through and inserts the data
# for each row in the csv file. N being the amount of rows in the csv file.
# Space Complexity: O(N^2) because of the created hashmap
# Return: Returns a hashmap object with the data from the csv file
def create_package_hash():
    package_hash = HashMap()
    with open("Data/WGUPS Package File.csv") as pf:
        writer = csv.reader(pf, delimiter=',')
        next(writer)
        for i in writer:
            package_hash.insert(i[0], list(i[1:7]))
    return package_hash


def create_distance_graph():
    distance_graph = []
    with open("Data/WGUPS Distance Table.csv") as dt:
        writer = csv.reader(dt, delimiter=',')
        next(writer)
        for i in writer:
            distance_graph.append(i[2:])

    return distance_graph


def create_address_list():
    address_list = []
    with open("Data/WGUPS Distance Table.csv") as al:
        writer = csv.reader(al, delimiter=',')
        next(writer)
        for i in writer:
            address_list.append(i[0].split('\n')[1].strip().replace(',', ''))

    return address_list
