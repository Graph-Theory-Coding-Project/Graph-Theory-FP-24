Final Project Website Repository: https://github.com/Graph-Theory-Coding-Project/Final-Project-Website




# ✈️ Fastravel ✈️

## Group Members
| Name                              | NRP         | Contribution          |
|-----------------------------------|-------------|-----------------------|
| Fadhil Revinno Hairiman           | 5025231002  | Website Creation & Frontend Development  |
| R. Rafif Aqil Aabid Hermawan      | 5025231069  | Project Planning, Quality Assurance, & Progress Report |
| Rogelio Kenny Arisandi            | 5025231074  | Algorithm Creation & Backend Development |
| Matteo Dennequin                  | 5999241043  | Project Planning, Quality Assurance, & Progress Report |



# Background
## Travelling the world
When planning a holiday around the world, it's important to optimize your journey, both to avoid too long journey times and to save money. So the idea is to put in place a tool that will give us the shortest path from a set of airports that we have entered in advance. Using Python, based on various notions seen in lessons during the semester, the tool FasTravel was born.

![Visualization](img/background-1.png)

## Requirement Specificaiton
We wanted to make our tool as comprehensive as possible by offering users the option of searching all the world's airports, so that they can plan trips at both national and international level. 
To make our tool as accessible as possible, we need to provide visibility of the optimal path found. By using different data visualisation libraries and setting up a website, the user can obtain a clear and visible answer on a dynamic planisphere.

## Terminology

### Travelling Salesman Problem 

![TSP Representation](img/background-tsprep.png)

This optimization problem calls for the application of a TSP case. The Traveling Salesman Problem (TSP) is all about figuring out the shortest route for a salesperson to visit several cities, starting from one place and possibly ending at another. It's a well-known problem in computer science and operations research, with real-world uses in logistics and delivery.

Two main reasons stand out:
- The point of departure must also be the point of arrival. We need to return home after our incredible stay.
- For the sake of optimisation, and to vary our holidays, we'll only take the air route between two airports once: a Eulerian circuit.

### Prim's Algorithm

![Prims](img/background-prims.png)

To aid in solving Travelling Salesman Problem we can represent the cities as a graph and solve the problem by creating a minimum spanning tree from that graph, and one of the ways to get MST is with Prim’s algorithm. 
  
Prim’s algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.
  
This approach can speed up pathfinding by choosing the smallest path from two nodes which then can generate a path which the cost is never more than two times the cost of an optimal tour. 

### Hungarian Algorithm

WIP

# Methodology
## Dataset 
For this project we used the global airport database from Open Data Soft. 

![Raw Dataset](img/methodology-dataset-raw.png)

This data contains Airport Codes, Airport Name, City name, Country Name, Country Code, Latitude, Longitude, World Area Code, City Name geo_name_id, Country Name geo_name_id, and coordinates. 

![Raw Dataset](img/methodology-dataset-processed.png)

For our data preprocessing unnecessary columns from the table, which are City Name geo_name_id and Country Name geo_name_id, are dropped. After which our data preprocessing is complete and the remaining columns are used for the project.

## Graph Creation
Based on the processed data from before, we can use the longitude and latitude values to create a graph that will be used to calculate the shortest path. For our primary libraries that is used in the project : 
1. NetworkX is used to create graphs of the cities.
2. GeoPy is used to calculate distance between the cities based on the coordinates provided in the dataset.
3. Folium is used to represent the cities and its path in an OpenStreetMap view.

![Graph Creation code](img/methodology-graph-code.png)

First nodes are created based on the selected cities, then the distance between cities will be calculated one pair at a time utilizing GeoPy and the provided coordinates of each city, during calculation a Folium line and point will be generated for visual representations later.

![Graph Creation visualization](img/methodology-graph-visual.png)

## Prim's algorithm
For our first implementation, Prim’s algorithm is utilized.

![image](https://github.com/user-attachments/assets/2aa09129-0fba-4958-9fa4-e3f787179b79)


Two functions are created for this methodology, first is the addEdge function for creating a new graph after running an algorithm. 

![Prim prims function](img/methodology-prims-prims.png)

Second is the Prim’s algorithm itself where standard implementation of the algorithm is utilized, which in the end will return the edge and the cost of the graph. 

After those functions have been created, then the algorithm can be executed by providing the previously created graph and a starting point which after execution a path in edge form from the provided starting point and the total distance is obtained. A map of the resulting tree can be generated from the resulting edge information to create a visual representation using Folium, after which a real distance of the tree is generated and the map representation is generated.

![Prim visual](img/methodology-prims-visual.png)

# Hungarian Algorithm

This implementation uses a variant of the Hungarian algorithm known as the **Diagonal Completion Method**, as described in the research paper by J. R. King, X. Y. Zhang, and G. H. Jinx. The method consists of the following 8 steps:

---

## Step 1: Data Input
We use a matrix that represents distances between the following cities:

- Jakarta
- Sydney
- New York
- Toronto
- Buenos Aires
- Tokyo
- Madrid

![image](https://github.com/user-attachments/assets/657c21e8-2e5c-4a66-bcc9-2fb1d5d424a9)


---

## Step 2: Matrix Reduction
Reduce the matrix in the same way as in the Hungarian algorithm, using the following line of code:

![image](https://github.com/user-attachments/assets/38f04896-0a6c-4de0-b101-fa4068590436)

---

## Step 3: Row and Penalty Calculation
After we reduce the matrix, we have to compute the which 0’s has the biggest penalties, A row (column) penalty is defined as the difference between the next smallest element in the row (column) and the smallest element in that row (column) and represents the minimum premium that will be incurred when forced away from the choice of the smallest element in a row or a column by partial tour feasibility requirements. (A DIAGONAL COMPLETION AND 2-OPTIMAL PROCEDURE FOR THE TRAVELLING SALESMAN PROBLEM, J. R. KING,’ X. Y. ZHANG’ and G. H. JINX).

---

## Step 4: Sort the Feasible Tour (Sort the Penalties)
The penalties for the paths are as follows:

```
P(1,4) = 1567.0510247500006
P(2,6) = 1567.0510247500006
P(4,1) = 1567.0510247500006
P(6,2) = 1567.0510247500006
P(0,3) = 345.05008419000023
P(3,0) = 345.05008419000023
P(3,5) = 345.05008419000023
P(5,3) = 345.05008419000023
P(2,1) = 0.0
P(6,4) = 0.0
```

After that we can take from the top, and make a sub tours. (1, 4), (2, 6) (0, 3) (3, 5) are the sub tours. (4,1), (6,2) etc. will not be chosen as they are the closing link, resulting in closing the TSP path, as we can’t end the tour yet because we need to travel through all the nodes
	We also need to mark the corresponding column an row, that has 0’s used in the penalties, just like in similar manner in hungarian algorithm. We can mark them by changing the matrix values into infinity as we dont need to check infinity and check those corresponding rows and column.

The following function to Find the penalties and mark them are:

![image](https://github.com/user-attachments/assets/17dda62f-023c-404d-acfe-3da4f5b4cbcd)

![image](https://github.com/user-attachments/assets/b110ec16-4fc2-4e02-9482-8e8bfe842deb)


---

## Step 5: Rearrange the Matrix
The row entries for the new matrix must be written in the sequence of the vertices which form the above feasible partial tour (i.e. in the order of 1, 4, 2, 6, 0, 3, 5 for the example problem). The column entries are then rearranged in such a way that enables all the O* elements to be located on the diagonal. Therefore, the column entries in the example problem will be, from the left to right, in the following order 4, 2, 6, 0, 3, 5, 1.

---

## Step 6: Construct Sub-Matrix
Construct the sub-matrix for the closing links:

- Paths: `[[1, 4], [2, 6], [0, 3, 5]]`
- Closing links: `(4, 1)`, `(6, 2)`, `(5, 0)`

![image](https://github.com/user-attachments/assets/2328bcde-ff39-44de-a51a-ce6cfdc8e110)


---

## Step 7: Repeat Steps 2 to 6
Repeat steps 2 through 6 until all paths are constructed.

---

## Step 8: Initial Feasible Solution (IFS)
Once all paths are connected, add the starting point to complete the TSP solution:

```
Final TSP Path: [1, 4, 2, 6, 0, 3, 5, 1]
```

---

### References:
- J. R. King, X. Y. Zhang, G. H. Jinx. "A Diagonal Completion and 2-Optimal Procedure for the Travelling Salesman Problem."

# Implementation


---

## Tech Stack
- **Backend**: Python (Flask framework)
- **Frontend**: HTML

---

## Required Dependencies
Make sure to install the following dependencies for this project to work:
- Flask
- Any other necessary Python libraries

Install the dependencies using:
```
pip install -r requirements.txt
```

![image](https://github.com/user-attachments/assets/ec9e4b89-c799-4895-9490-b589f5ac3fb8)


---

## Project Structure

The project is structured as follows:

![image](https://github.com/user-attachments/assets/266f59e5-5a94-47ac-9840-525e169a045e)



---

## Setting Up the Environment

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Graph-Theory-Coding-Project/Final-Project-Website.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Final-Project-Website
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

![image](https://github.com/user-attachments/assets/30701acf-f4ea-4a9b-80fb-95627d18b97e)

---



## Displaying the Map

All calculations and rendering are handled by the backend using Python. The generated map is saved as `m_path_map.html` and displayed in the main HTML file using the `<iframe>` tag.

Example:
```html
<iframe class="rounded-xl" src="{{ url_for('static', filename='m_path_map.html') }}" width="1280" height="720"></iframe>
```

By placing the `m_path_map.html` file in the `static` folder, Flask automatically detects and serves it. If set up correctly, the map will appear as shown below:

![image](https://github.com/user-attachments/assets/1e7ae2d6-d608-488b-b47e-0630c895e12a)

---



## User Input

To enhance user experience, the application includes the following features:

- **Dropdown for Airport Selection**: Users can select airports in various countries.
- **Search Filter**: Helps users quickly find airports by city.
- **Uncheck All**: Allows users to reset their selections and plan a new trip.
- **Generate Map**: After selecting airports, users can click "Generate Map" to display the optimized travel plan.

Example interface:

![image](https://github.com/user-attachments/assets/9f06d7db-3054-4d1b-9602-6888e008c792)




---
# Conclusion

## Summary
So, with a clear idea of the destinations you want to discover, FasTravel allows you to obtain the optimum route thanks to the website powered by a calculation file written in python and some usual notions of ‘Graph Theory’.


It goes without saying that the shortest route is generally the fastest, so you can minimise the hours spent travelling. 


The tool is easy to use, accessible for all types of user. Some features could be added in the future, let’s see of examples.


## Areas of Improvement
- In order to have more precision, It may be useful not to work with airport addresses, but rather with the addresses of the exact cities that the user wishes to visit. This would mean calculating the distances between the airports and the towns visited if the airport is not in
- Depending on your convictions, over-use of the plane can be a problem when organising your trip. The addition of different means of transport (and associated distance calculation formulas), such as car, train or boat, could make FasTravel even more comprehensive.
- It could also be equipped with a route suggestion tool based on a number of cities to be visited and a number of cities considered essential to the trip. Although this would involve concepts that are far removed from the initial subject, it remains an interesting idea for optimisation.


---

---

## Contribution

Feel free to fork this repository, submit issues, and send pull requests. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```
