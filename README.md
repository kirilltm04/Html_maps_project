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
 
 ## Visuals and Usage
 
 There are 5 examples of maps in the project. Every map has the locations of a certain year.
 
 <img width="1789" alt="Screenshot 2022-02-09 at 23 16 08" src="https://user-images.githubusercontent.com/92577092/153291779-f7b44ffe-6feb-4181-9b12-9703a0c2377d.png"> 
 
This is a result of the main.py module after putting in the following arguments: 2015 49.83826 24.02324 "locations.list"
So, the created map shares 10 closest locations of movie shooting to the coordinates of Lviv (49.83826 24.02324).
The map has got two layers: "Short location (<1000km)" and "Long location (>1000 km)" So, if a location is closer than 1000 km 
from the user's coordinates it's getting into the first layer (Analogically, for the second). Markers of each layer have a unique color (red and orange
respectively) and a special tooltip ("Not too far" and "A little bit further" respectively). The popup for every Marker is the distance
column of the df (distance between the location and the user's coordinates).

<img width="1766" alt="Screenshot 2022-02-09 at 23 27 52" src="https://user-images.githubusercontent.com/92577092/153293148-dfe18b80-735e-4e92-a73c-9b76aabe4220.png">

<img width="1785" alt="Screenshot 2022-02-09 at 23 28 12" src="https://user-images.githubusercontent.com/92577092/153293168-0dc7f673-8426-49cd-9be5-91157dcca4e3.png">

## Licence

Licence used in the project is GNU GENERAL PUBLIC LICENSE.

## Support

In case of problems a user may apply on kirill.tumoian@ucu.edu.ua email.

## Authors and acknowledgement

The project was done by Kirill Tumoian with using the examples given in the laboratory work short statements.
