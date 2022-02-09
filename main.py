"""
Lab project for making a map with the locations of movies of a certain year.
Gets four arguments: the year of the movies, latitude, longitude and the path to the right file.
Returns an HTML map with markers on the places of movies.
"""
import folium
import pandas as pd
import argparse
from geopy.geocoders import Nominatim
import haversine

parser = argparse.ArgumentParser(description='parsing of arguments')
parser.add_argument('year', help='The year of the movies', type=int)
parser.add_argument('latitude', help='The latitude of the location', type=str)
parser.add_argument('longitude', help='The longitude of the location', type=str)
parser.add_argument('file_path', help='Path to the chosen file', type=str)
arguments = parser.parse_args()


def read_file() -> list:
    """
    Reading the file and returning the list with movies only of the right lst_with_year.
    :return: list
    """
    path = arguments.file_path
    lst, lst_with_year, ans, lst_with_no_curly, lst_no_year = [], [], [], [], []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for i in lines:
            # making a list of the file and removing extra tabs
            lst.append(i.replace("\t", ""))
        for j in lst:
            if "(" + str(arguments.year) + ")" in j:
                # sorting the list by removing the inappropriate year
                lst_with_year.append(j)
        for y in lst_with_year:
            # removing the year
            lst_no_year.append(y.split(f"({str(arguments.year)}")[0] + y.split(f"{str(arguments.year)})")[1])
        for k in lst_no_year:
            if "{" in k and "}" in k:
                # removing the curly brackets and symbols inside them
                lst_with_no_curly.append(k.split("{")[0] + k.split("}")[1])
            else:
                lst_with_no_curly.append(k)
        for x in lst_with_no_curly:
            if "(" in x and ")" in x:
                ans.append(x.split("(")[0] + x.split(")")[1])
            # removing the regular brackets and symbols inside them
            else:
                ans.append(x)
    return ans


def dataframe_maker():
    """
    Making a pandas dataframe with two columns: the name of the movie and
    its shooting location
    :return: pd.Dataframe
    """
    ans = []
    lst = read_file()
    for i in lst:
        ans.append(i.split('" '))
        # splitting the movies and the locations
    df = pd.DataFrame(ans)
    df.rename(columns={0: "Names_of_movies", 1: "Locations"}, inplace=True)
    try:
        df.drop(columns=2, inplace=True)
        # removing extra columns
        return df
    except KeyError:
        return df


def coordinate_columns():
    """
    Making two additional columns in the Dataframe with
    latitude and longitude of the coordinates.
    :return: pd.Dataframe
    """
    df = dataframe_maker()
    loc = df["Locations"]
    geolocator = Nominatim(user_agent="PyCharm")
    latitude, longitude = [], []
    # has to be changed if another application is used!
    for i in range(len(loc)):
        try:
            location = geolocator.geocode(loc[i])
            latitude.append(location.latitude)
            longitude.append(location.longitude)
        except AttributeError:
            # in case coordinates cannot be found by the module
            df.drop(index=[i], inplace=True)
            continue
    df["Latitude"] = latitude
    df["Longitude"] = longitude
    return df


def distance_column():
    """
    Adding a distance column to the dataframe
    which has the haversine distance from the given
    coordinates to every film location.
    :return: pd.Dataframe
    """
    df = coordinate_columns()
    lst = []
    input_coordinates = float(arguments.latitude), float(arguments.longitude)
    movie_coordinates = list(zip(list(df["Latitude"]), list(df["Longitude"])))
    # making two coordinate tuples
    for i in range(len(movie_coordinates)):
        lst.append(haversine.haversine(input_coordinates, movie_coordinates[i]))
        # appending the list for the new column
    df["Distance"] = lst
    return df.sort_values("Distance")  # .iloc[0:10, :]


def map_maker():
    """
    Function that makes the map with 10 of the closest locations with films
    :return: folium map
    """
    df = distance_column()
    input_coordinates = float(arguments.latitude), float(arguments.longitude)
    coordinates_tpl = list(zip(list(df["Latitude"]), list(df["Longitude"])))
    m = folium.Map(location=[float(arguments.latitude), float(arguments.longitude)], zoom_start=4)
    fg_sl = folium.FeatureGroup(name="Short location")
    fg_ll = folium.FeatureGroup(name="Long location")
    for i in range(len(coordinates_tpl)):
        if haversine.haversine(coordinates_tpl[i], input_coordinates) <= 1000:
            fg_sl.add_child(
                folium.Marker(list(coordinates_tpl[i]), popup=coordinates_tpl[i], icon=folium.Icon(color="red"),
                              tooltip="Not too far!"))
        elif haversine.haversine(coordinates_tpl[i], input_coordinates) > 1000:
            fg_ll.add_child(
                folium.Marker(list(coordinates_tpl[i]), popup=coordinates_tpl[i], icon=folium.Icon(color="orange"),
                              tooltip="A little bit further!"))
    m.add_child(fg_sl)
    m.add_child(fg_ll)
    m.add_child(folium.LayerControl())
    m.save("Map3.html")


map_maker()
