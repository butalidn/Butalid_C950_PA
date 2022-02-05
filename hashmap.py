# Hashmap basic structure code from https://www.youtube.com/watch?v=9HFbhPscPU0 &
# and from "Webinar-1 - Let's Go Hashing"

# HashMap class utilizes Python list object containing other list objects
# Space Complexity: O(N^2) because lists will be containing other lists if they have the same hash value
# Time Complexity: Each function's time complexity will be commented aboved the function
class HashMap:
    # Time Complexity: O(N)
    # Default size of list is 64. Initial size of hashmap is scalable
    def __init__(self):
        self.__size = 64
        self.__table = [None] * self.__size

    # Time Complexity: O(N) because there is a for loop that could run N number of times
    # Function creates a hash value using built-in hash function and moduluo to find a appropriate
    # index for the new key, value pair.
    # If there is not already a item in the hashed location, the pair is inserted into that index.
    # Otherwise, the pair is added to the list located at the hashed index.
    def insert(self, key, value):
        key = int(key)
        key_hash = hash(key) % self.__size
        key_value = [key, value]

        if self.__table[key_hash] is None:
            self.__table[key_hash] = list([key_value])
        else:
            for i in self.__table[key_hash]:
                if i[0] == key:
                    i[1] = value
                    return True
            self.__table[key_hash].append(key_value)

    # Time Complexity: O(N) because there is a for loop that in the worst case scenario could take O(N) time
    # if there have been any collisions
    # The function finds the corresponding hash value of the key and then goes to the index of that value.
    # It then loops through the list until it finds the matching key or reaches the end of the list
    # Return: Returns a formatted string representing the data of the given key, otherwise returns None
    def lookup(self, key):
        key_hash = hash(key) % self.__size
        if self.__table[key_hash]:
            for i in self.__table[key_hash]:
                if i[0] == key:
                    return f'Package ID: {i[0]}\n' \
                           f'Address: {i[1][0]}\n' \
                           f'City: {i[1][1]}\n' \
                           f'State: {i[1][2]}\n' \
                           f'Zip: {i[1][3]}\n' \
                           f'Delivery Time: {i[1][4]}\n' \
                           f'Mass: {i[1][5]}\n'
        return None

    # Time Complexity: O(1) because it takes constant time to return attribute
    def get_table(self):
        return self.__table

    def get_package(self, key):
        key_hash = hash(key) % self.__size
        if self.__table[key_hash]:
            for i in self.__table[key_hash]:
                if i[0] == key:
                    return i

    def get_address(self, key):
        key_hash = hash(key) % self.__size
        if self.__table[key_hash]:
            for i in self.__table[key_hash]:
                if i[0] == key:
                    return i[1][0]

    # Time Complexity: O(1) because it takes constant time to return attribute
    def __len__(self):
        return self.__size
