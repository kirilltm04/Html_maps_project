import folium
import pandas as pd
import argparse
import sys
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
    Reading the file and returning the list with movies only of the right year.
    :return: list
    """
    path = arguments.file_path
    lst, ans = [], []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for i in lines:
            lst.append(i.replace("\t", ""))
        for j in lst:
            if "(" + str(arguments.year) + ")" in j:
                ans.append(j)
    return ans


def dataframe_maker():
    pass


