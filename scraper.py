import requests
from jikanpy import Jikan
from os import path
from configparser import *
from pathlib import Path
from termcolor import colored
import os, jikanpy, wget, os.path
jikan = Jikan()

range_current = 0
range_end = int(input("Ending ID: "))
data_list = []
mal_directory = "E:\\Python Projects\\MAL\\resources\\myanimelist\\"

def main():
    global range_current, range_end, data_list
    range_current += 1
    data_list = []
    if range_current < range_end:
        try:
            mal_data_raw = str(jikan.anime(range_current)).replace('"', "'")

            #Image URL
            try:
                data_image_url0 = mal_data_raw.split("'image_url': '")[1]
                data_image_url = data_image_url0.split("', '")[0]
                data_list.append(data_image_url)
            except IndexError:
                data_image_url = "https://cdn.myanimelist.net/images/anime/4/19644.jpg"
                print("Error: Image URL not found")

            #Title (Japanese)
            try:
                data_title0 = mal_data_raw.split("'title': '")[1]
                data_title = data_title0.split("', '")[0]
                data_list.append(data_title)
            except IndexError:
                data_title = "Not Found"
                print("Error: Japanese Title not found")

            #Title (English)
            try:
                data_title_english0 = mal_data_raw.split("'title_english': '")[1]
                data_title_english = data_title_english0.split("', '")[0]
                data_list.append(data_title_english)
            except IndexError:
                data_title_english = "Not Found"
                print("Error: English Title not Found: " + str(range_current))

            #Score
            try:
                data_score0 = mal_data_raw.split("'score': ")[1]
                data_score = data_score0.split(", ")[0]
                data_list.append(data_score)
            except IndexError:
                data_score = "Not Found"
                print("Error: Score not found" + range_current)

            #MAL ID
            try:
                data_mal_id0 = mal_data_raw.split("'mal_id': ")[1]
                data_mal_id = data_mal_id0.split(", ")[0]
                data_list.append(data_mal_id)
            except IndexError:
                data_mal_id = "Not Found"
                print("Error: MAL ID not found" + range_current)

            #Source
            try:
                data_source0 = mal_data_raw.split("'source': '")[1]
                data_source = data_source0.split("', '")[0]
                data_list.append(data_source)
            except IndexError:
                data_source = "Not Found"
                print("Error: Source not found" + range_current)

            #Type
            try:
                data_type0 = mal_data_raw.split("'type': '")[1]
                data_type = data_type0.split("', '")[0]
                data_list.append(data_type)
            except IndexError:
                data_type = "Not Found"
                print("Error: Type not found" + range_current)

            #Episodes
            try:
                data_episodes0 = mal_data_raw.split("'episodes': ")[1]
                data_episodes = data_episodes0.split(", ")[0]
                data_list.append(data_episodes)
            except IndexError:
                data_episodes = "Not Found"
                print("Error: Episode Count not found" + range_current)

            #Rank
            try:
                data_rank0 = mal_data_raw.split("'rank': ")[1]
                data_rank = data_rank0.split(", ")[0]
                data_list.append(data_rank)
            except IndexError:
                data_rank = "Not Found"
                print("Error: Rank not found" + range_current)

            #Popularity
            try:
                data_popularity0 = mal_data_raw.split("'popularity': ")[1]
                data_popularity = data_popularity0.split(", ")[0]
                data_list.append(data_popularity)
            except IndexError:
                data_popularity = "Not Found"
                print("Error: Popularity not found" + range_current)

            #Synopsis
            try:
                data_synopsis0 = mal_data_raw.split("'synopsis': '")[1]
                data_synopsis = data_synopsis0.split("', '")[0]
                data_list.append(data_synopsis)
            except IndexError:
                data_synopsis = "Not Found"
                print("Error: Synopsis not found" + range_current)

            #Download
            bad_characters = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]
            for item in bad_characters:
                data_title = data_title.replace(item, "")
            if not path.exists(mal_directory + data_title + "\\"):
                os.mkdir(mal_directory + data_title + "\\")
            if not path.isfile(mal_directory + data_title + "\\boxart.jpg"):
                wget.download(data_image_url, mal_directory + data_title + "\\boxart.jpg")
            if path.isfile(mal_directory + data_title + "\\data.ini"):
                os.remove(mal_directory + data_title + "\\data.ini")
            Path(mal_directory + data_title + "\\data.ini").touch()
            config = ConfigParser()
            config.read(mal_directory + data_list[1] + "\\data.ini")
            config.add_section('data')
            config.set('data', 'title_jp', data_title)
            config.set('data', 'title_en', data_title_english)
            config.set('data', 'score', data_score)
            config.set('data', 'mal_id', data_mal_id)
            config.set('data', 'source', data_source)
            config.set('data', 'type', data_type)
            config.set('data', 'episodes', data_episodes)
            config.set('data', 'rank', data_rank)
            config.set('data', 'popularity', data_popularity)
            config.set('data', 'synopsis', data_synopsis)
            with open(mal_directory + data_title + "\\data.ini", 'w') as configfile:
                config.write(configfile)

            data_list = []
            print(colored(data_title, "green"))
        except jikanpy.exceptions.APIException:
            print(colored("oof", "red"))
    else:
        print("Finished Successfully")
        quit()

for x in range(1, range_end):
    main()