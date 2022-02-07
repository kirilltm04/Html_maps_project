import folium
import pandas as pd
import argparse
import geopy

parser = argparse.ArgumentParser(description='parsing of arguments')
parser.add_argument('year', help='The year of the movies', type=int)
parser.add_argument('latitude', help='The latitude of the location', type=str)
parser.add_argument('longitude', help='The longitude of the location', type=str)
parser.add_argument('file_path', help='Path to the chosen file', type=str)
arguments = parser.parse_args()
# python3 main.py 1990 49.83826 24.02324 "loc_short.list


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


print(read_file())