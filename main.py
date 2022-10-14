#!/usr/local/bin/python3

import webbrowser
import datetime 

start_time=[9,50]
class_period=40
class_number=9

Leisure_link = "https://youtube.com"

now = datetime.datetime.now()

time_table= {
            "Monday": ["IT","Civ", "Eng", "Lunch", "Eco", "SL", "Math", "Geo", "Civ"],
            "Tuesday": ["IT", "Eng", "Eng", "Lunch", "Chem", "Chem", "Math", "SL", "Phy"],
            "Wednesday": ["Eng", "Civ", "Geo", "Math", "Lunch", "PE", "Chem", "Math", "Civ"],
            "Thursday": ["Math", "Chem", "Eng", "Civ", "Lunch", "SL", "Phy", "IT", "CCA"],
            "Friday": ["Eng", "Civ", "Chem", "Eco", "Lunch", "Chem", "SL", "Math", "Phy"]
            }
links = {
        "IT": "https://zoom.us/IT",
        "Civ": "https://meet.google.com/Civ",
        "Math": "https://zoom.us/Math",
        "Chem": "https://zoom.us/Chem",
        "Eco": "https://zoom.us/Eco",
        "Phy": "https://zoom.us/Phy",
        "SL": "https://zoom.us/SL",
        "Eng": "https://zoom.us/Eng",
        "Geo": "https://zoom.us/Geo",
        "Phy": "https://zoom.us/Phy"
        }

def class_info():
        school_start_time = datetime.datetime(now.year, now.month, now.day, start_time[0], start_time[1], 0) 
        
        try:
                time_delta_elements = [int(x) for x in str(now-school_start_time).split(":")[:2]]
                time_delta_mins = time_delta_elements[0]*60 + time_delta_elements[1]
                if time_delta_mins//class_period >= class_number:
                        time_delta_mins= (class_number-1)*class_period                               
        except ValueError:
                time_delta_mins = 0
        finally:
                return int(time_delta_mins//class_period)
                

def open_req_link():
        try:
                webbrowser.open(links[time_table[now.strftime("%A")][class_info()]])
        except KeyError:
                webbrowser.open(Leisure_link)
        
class_counter = -1

while True: 
        if (class_info() != class_counter):
                print([time_table[now.strftime("%A")][class_info()]])
                open_req_link()
                class_counter=class_info()