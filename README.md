# Html_maps_project
The project made to produce HTML maps of film shooting locations.

## Description

Module main.py is the basic one. It may be started using argparse.

The necessary arguments for the module are:
- year of the movie;
- latitude of the coordinates;
- longitude of the coordinates; 
- path to the file with movies (locations.list in the project).

These libraries have to be imported:
- folium - for the HTML map creation;
- pandas - to make a DataFrame and work with the data;
- argparse - to get the arguments;
- geopy - to get the coordinates of any location;
- haversine - to find the distance between two coordinates.

The module has 5 functions:
- read_file() - reads the file and excludes everything except for location and name of the movie;
- dataframe_maker() - makes a pandas DataFrame with two colums: "Names_of_movies" and "Locations";
- coordinate_columns() - adds two columns to the df with the latitude and the longitude of each location;
- distance_column() - adds the column with the distance to the user's coordinates and sorts the df according to it;
- map_maker() - creates the HTML map and saves it into the necessary file.
 
 ## Visuals
 
 There are 5 examples of maps in the project. Every map has the locations of a certain year.
 <img width="1789" alt="Screenshot 2022-02-09 at 23 16 08" src="https://user-images.githubusercontent.com/92577092/153291779-f7b44ffe-6feb-4181-9b12-9703a0c2377d.png">

