import folium
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='parsing of arguments')
parser.add_argument('year', help='The year of the movies', type=int)
parser.add_argument('latitude', help='The latitude of the location', type=str)
parser.add_argument('longitude', help='The longitude of the location', type=str)
parser.add_argument('file_path', help='Path to the chosen file', type=str)
arguments = parser.parse_args()


def read_file():
    path = arguments.file_path
    return path
