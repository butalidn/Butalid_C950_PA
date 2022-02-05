from hashmap import *


class Distance:
    def __init__(self, distance_data, address_list):
        self.distance_data = distance_data
        self.address_list = address_list

    def distance_between(self, address1, address2):
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
        return self.address_list.index(address)

    def min_distance(self, from_address, packages, package_list):
        visited = set()
        unvisited = set()
        package_index = []
        total_dist = 0

        u = from_address
        visited.add(u)

        for i in package_list:
            unvisited.add(packages.get_address(i))
            package_index.append(packages.get_address(i))

        print(unvisited)
        while unvisited:
            min_dist = next(iter(unvisited))
            for j in unvisited:
                if j == min_dist:
                    continue
                if (self.distance_between(u, j)) <= self.distance_between(u, min_dist):
                    min_dist = j
            next_address = min_dist
            total_dist += self.distance_between(u, next_address)
            u = next_address
            unvisited.remove(min_dist)
            visited.add(min_dist)

        total_dist += self.distance_between(from_address, u)
        return total_dist
