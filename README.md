# Butalid_C950_PA
This Project was the Peformance Assessment for **C950 (Data Structures and Algorithms II)**

Run 'py main.py' to run program

I solved this project using the Nearest Neighbors Algorithm. There is a simple GUI that allows you to:
1) Find the total mileage of all trucks' when all packages have been delivered
2) Find the status of all packages at a specific time
3) Find information about a package using its package id

One requirement was to create a data structure so I created a hash map with insertion, lookup, and update functionality. No external libraries were allowed to be used.

### The algorithm I used

This is the basic pseudocode my program followed for the Nearest Neighbor algorithm

General steps for Nearest Neighbor Algorithm 
1.	Create a list of all vertices to be visited and called it ‘unvisited’ or ‘u’
2.	Start at a vertex
3.	Find the edge with the smallest value in the unvisited list connected to the current vertex. Call the connecting vertex ‘v’
4.	Remove the current vertex and ‘v’ from the unvisited list. Record the edge’s value
5.	Repeat steps 2 - 4 until the unvisited list is empty
6.	Add up all the values together and add the edge from the last ‘v’ to the original vertex 

Pseudocode for Nearest Neighbors Algorithm

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

### Scenario
The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

Keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

### Assumptions
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

