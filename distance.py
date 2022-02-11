from datetime import datetime
from datetime import timedelta


# This class is used to create a the distance graph and an address list
# All information pertaining distance betweens addresses is dealt in this class
class Distance:
    def __init__(self, distance_data, address_list):
        self.distance_data = distance_data
        self.address_list = address_list

    # Two addresses are given and the indexes of the addresses in the address list are found
    # and then those indexes are used in the distance data graph to find the corresponding distance.
    # The distance is found no matter the order of the addresses given
    # Time Complexity: O(N) because the find index function takes O(N) at worst case
    # Space Compleixty: O(1) because only variables are declared
    # Return: Returns the float value when found in the distance data graph
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

    # Time Complexity: O(N) because of the .index() function
    # Space Complexity: O(1) because no variable or structures are created
    # Return: Returns the index of the given index in the address list
    def find_index(self, address):
        if address == '3575 W Valley Central Station bus Loop':
            address = '3575 W Valley Central Sta bus Loop'
        return self.address_list.index(address)

    # This function is where the Nearest Neighbor algorithm is implemented
    # The function takes in the list of package IDs that must be visited
    # A set of the distinct addresss that must be visited is created
    # A list containing an addresses and the package IDs that are going to that address
    # is created

    # A list of the unvisited addresses is created and looped through to find the shortest
    # distance from the current address which starts at the WGU hub. That address is then
    # removed from the unvisited list and the algorithm loops through until the list is empty

    # The milage from the current address to the next address is calculated and the packaage's
    # status is updated
    # Time Complexity: O(N^3) at worst because of the while and for loops using the distance between
    # function which also takes O(N) time
    # Space Complexity: O(N^2) because of the 2D list but at worst could be O(N^3)
    # if all packages are going to the same address. This would be a rare case and would basically be O(N^2)
    # if this happened. Time compelxity would also basically be O(1).
    # Returns a list containing the truck name, time the truck returns to the hub, and the milage it took
    def min_distance(self, from_address, packages, package_list, start_time, truck_name):
        unvisited = []
        total_dist = 0
        address_set = set()
        timer = start_time

        package_address_list = []

        u = from_address

        # Time Complexity: O(N^2) on average because of the double for loop. At worst case could be
        # O(N^3) because of the 'in' function for the set if hashed inefficiently
        # Space Compleixty: O(1)
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

        # Time Complexity: At worst would be O(N^3) because of looping through the unvisisted list twice
        # and the distance bewteen function takes O(N) time.
        # Space Complexity: O(N^2) at worst because of the time list in the while loop
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

            # Time Complexity: O(N) on average beacuse of for loop but O(N^2)
            # at worst because of the update time function if the hash function
            # is inefficient
            # Space Complexity: O(N) because of variable in the for loop
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
        return [truck_name, timer, total_dist]
