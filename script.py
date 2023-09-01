import requests
from tkinter import *

def get_country(data):
    if data['country'] == "None":
        return "Country is not available"
    else:
        return data['country']
def get_city(data):
    if data['city'] == "None":
        return "City is not available"
    else:    
        return data['city']
def get_location(data):
    if data['lat'] == "None" or data['lon'] == "None":
        return "Location is not available"
    else:    
        return f"Latitude=>{data['lat']} and Longitude=>{data['lon']}"

def get_timezone(data):
    if data['timezone'] == "None":
        return "Timezone is not available"
    else:
        return data['timezone']
def get_isp(data):
    if data['isp'] == "None":
        return  "ISP is not available"
    else:
        return data['isp']



def fetch_ip_address():
    try:
        response =  requests.get("https://api.ipify.org/?format=json")
        data =  response.json()
        return data["ip"]
    except Exception as error:
        print(f"Error happened while fetching IP Address: {error}")

def fetch_info(ip_address):
    try: 
        response=requests.get(f"http://ip-api.com/json/{ip_address}")
        data=response.json()
        return data
    except Exception as error:
        print(f"Error happened while fetching IP Address Information: {error}")


def show_data():
    final_data = fetch_info(fetch_ip_address())

    window = Tk()
    window.title("IP Address Information")

    Label(window, text="Your IP Address is:").grid(row=0, column=0)
    Label(window, text=fetch_ip_address()).grid(row=0, column=1)

    Label(window, text="Your Country is:").grid(row=1, column=0)
    Label(window, text=get_country(final_data)).grid(row=1, column=1)

    Label(window, text="Your City is:").grid(row=2, column=0)
    Label(window, text=get_city(final_data)).grid(row=2, column=1)

    Label(window, text="Your Location is:").grid(row=3, column=0)
    Label(window, text=get_location(final_data)).grid(row=3, column=1)

    Label(window, text="Your Timezone is:").grid(row=4, column=0)
    Label(window, text=get_timezone(final_data)).grid(row=4, column=1)

    Label(window, text="Your ISP is:").grid(row=5, column=0)
    Label(window, text=get_isp(final_data)).grid(row=5, column=1)

    window.mainloop()

show_data()