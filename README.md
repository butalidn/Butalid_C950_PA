# Delivery Package System: Data Structures and Algorithms II 

This project was for Data Structures and Algorithms II. The application consists of a fleet of trucks delivering packages to various locations.
The goal of the project was to develop an algorithm that kept the total distance the trucks travel under an amount outlined by the project requirements.


***Run 'py main.py' to run program***

I solved this project using the Nearest Neighbors Algorithm. There is a simple GUI that allows you to:
1) Find the total mileage of all trucks' when all packages have been delivered
2) Find the status of all packages at a specific time
3) Find information about a package using its package id

One requirement was to create a data structure so I created a hash map with insertion, lookup, and update functionality. No external libraries were allowed to be used.

### The algorithm I used

This is the basic pseudocode my program followed for the Nearest Neighbor algorithm

**General steps for Nearest Neighbor Algorithm**
1.	Create a list of all vertices to be visited and called it ‘unvisited’ or ‘u’
2.	Start at a vertex
3.	Find the edge with the smallest value in the unvisited list connected to the current vertex. Call the connecting vertex ‘v’
4.	Remove the current vertex and ‘v’ from the unvisited list. Record the edge’s value
5.	Repeat steps 2 - 4 until the unvisited list is empty
6.	Add up all the values together and add the edge from the last ‘v’ to the original vertex 

**Pseudocode for Nearest Neighbors Algorithm**


	while there are unvisited addresses in a list:

		min_dist = first address in unvisited list

		for j in unvisited list:

			if equal to min_dist:

				continue through loop

			if distance between starting address and j is less than or equal to to the 
			distance between the starting address and min_dist:

				min_dist is now equal to j

		at end of for loop:

		next_address = min_dist

		distance between the starting address and next_address is calculated and saved
	


### Here are requirements from the project:
•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•   There are no collisions.

•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 

•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).

•   There is up to one special note associated with a package.

•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.

•   The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.

•   The day ends when all 40 packages have been delivered.


![Packages_Screenshot_10 00](https://user-images.githubusercontent.com/69161658/172489395-443b45ef-cff9-4faf-ac41-fc4c0a082e19.jpg)
