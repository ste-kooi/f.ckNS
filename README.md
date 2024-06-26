# loveNS
Repository inteded for the course Algorithms &amp; Heuristics - UvA Minor Programming - spring/summer 2024

## Case: RailNL
### Contents
- Case introduction
- How to use this repository
- Algorithms
- Experiments

### Case introduction
**Terminology**

- <u>Station</u>       : A specific location marked on a map by its x and y coordinates, which has connections to other stations.
- <u>Connection</u>    : A stretch of railroad that links two stations.
- <u>Route</u>         : A series of railroads connecting two or more stations, which defines the path a train will follow throughout the day.
- <u>Train routing</u> : The network of all routes.

This project focuses on generating the train routing for Holland and the Netherlands.
For Holland, this must be achieved by connecting the 22 stations using the 28 possible connections.
For the Netherlands, this must be achieved by connecting the 61 stations using the 89 possible connections.

**Hard constraints**  
 
- The maximum number of routes allowed in the train routing for Holland and the Netherlands is 7 and 20, respectively.    
- The maximum duration of a route in Holland and the Netherlands is 120 and 180 minutes, respectively.

**Soft constraints**    

- Utilize all possible connections
- Use as few routes as possible
- Minimize the total duration of the train routing

**Objective function**    
The train routing will be evaluated for quality using the following formula:   

K = p * 10000 - (T * 100 + Min)
  
- K is the quality   
- p is the fraction of covered connections   
- T is the number of routes used in the train routing   
- Min is the total number of minutes used in the routes in the train routing

**Statespace**    
The state space of this case can be calculated using the following formula:

Statespace = (C<sup>S</sup>)<sup>T</sup>

- C is number of connections per station
- S is number of stations per route
- T is number of routes per train routing

For the map size of Holland, the maximum value of C is 4, the maximum value of S is 24, and the maximum value of T is 7, resulting in a state space of approximately 1.4 * 10<sup>101</sup>.

For the map size of the Netherlands, the maximum value of C is 4, the maximum value of S is 24, and the maximum value of T is 7, resulting in a state space of approximately 1.4 * 10<sup>101</sup>.

### How to use this repository
**Requirements**   
The dependencies for this repository can be found in the '**requirements.txt**' file located in the root of the repository.

**Directories**  
 
- Algorithms  : Contains the scripts with the algorithms
- Classes     : Contains the scripts with the data structures for model, route, station, and connection
- Experiments : Contains the scripts for setting up experiments with the algorithms
- Output      : Contains the scripts for visual, terminal, and .csv output. Also includes a data folder with the experiment outputs
- Source      : Contains the .csv files with information about the stations and connections used in the data structure

**Algortihms and experiments**   
All algorithms and experiments can be accessed via main.py.
To view all possible command line arguments, type **-h** or **--help** in the command line.

To run an algorithm or experiment, it is mandatory to choose a map size. This repository supports two map sizes:  

- Holland     : add **-hl** or **--holland** to the command line
- Netherlands : add **-nl** of **--nederland** to the command line

To run the algorithms and experiments, you can combine the map size argument with arguments listed under the specific algorithms and experiments below.

### Algortihms
**Random**    
<u>Consttructive algorithm</u>
Generates random routes
<u>Command lines</u>

 - bla die bla
 - bla die bla

**Random Greedy**   
<u>Constructive algorithm</u>  
Generates routes op basis van de korste tijd tussen connecties
<u>Command lines</u>

 - bla die bla
 - bla die bla

**Depth First**   
<u>Constructive algorithm</u>   
The depth-first (DF) algorithm is designed to explore route options systematically and improve the train routing solution based on the scoring function, making it suitable for optimizing train schedules within the given constraints. The DF algorithm’s systematic approach ensures that all possible routes are considered, allowing for a complete exploration of potential solutions to the train routing problem.

The DF algorithm takes the most recent route from a stack and explores its possible route options. For this route, it identifies all possible connections from the last station in the route. If the new connection has not been used in the route and the duration of the route is within the allowed limit, the new route is pushed onto the stack.   

Two variants of the DF algorithm are implemented in this repository:   
<u>Depth first all (DFA) algorithm</u>   
This algorithm is designed to explore all possible starting stations for each route. It creates initial route options by iterating over all stations and adding them to the stack as beginning station if they haven't been used before.

<u>Depth first chosen (DFC) algorithm</u>   
This algorithm takes a strategic approach, by pre-selecting the starting stations. It pre-selects starting stations based on the number of connections a station holds. At first the stations with only one connection are used as a beginning station. After all stations with one connection are used, the stations with the most connections are used.

An additional feature has been added to enable users to emphasize coverage more within the DFA and DFC algorithms. This enhancement involves implementing a modified scoring function to evaluate route quality. Specifically, if a route achieves 100% coverage of all connections, it receives a bonus of 100 points. The regular score will still be displayed in the output. 

<u>Bias</u>  
The DFA exhibits several biases:    

- It constructs train routes one at a time, rather than considering all routes simultaneously. Because of this, it is possible that the most optimal solution will not be achieved.    
- Another bias lies in the validation of new route options. The algorithm it is not allowed to use a connection more than once within a single route. Therefore, there is no guarantee that the most optimal solution will be generated.
- Both the DFA and DFC algorithms exhibit bias by potentially overlooking more optimal starting stations.

<u>Command lines</u>

 - **dfa**, **--depthfall**' : runs the depth first all stations algorithm
 - **dfc**, **--depthfchosen**' : runs the depth first chosen stations algorithm
 - **cov**, **--depthfcov** : add cov to command line along with dfa or dfc to emphasise coverage

**Hill Climber**   
Iterative algorithm   
Generates routes 

<u>Command lines</u>

 - bla die bla
 - bla die bla

### Experiments
**Baseline - random algorithm**   
bla die bla

<u>Command lines</u>

 - bla die bla
 - bla die bla

**Depth First experiments**   
bla die bla

<u>Command lines</u>

 - '**-dfexp**', '**--dfexperiments**': 
 - bla die bla

**Hill Climber experiments**   
bla die bla

<u>Command lines</u>

 - bla die bla
 - bla die bla

