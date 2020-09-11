from tkinter import *
import requests
import json

root=Tk()
root.title('weather')
root.geometry('600x100')

entry_label=Label(root,text="Enter zipCode:").grid(row=0,column=0)
entry=Entry(root)
entry.grid(row=0,column=1)
def weather():
	#create your own API_KEY and insert it at API_KEY
	api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+entry.get()+"&distance=25&API_KEY=")
	api=json.loads(api_request.content)
	city=api[0]['ReportingArea']
	quality=api[0]['AQI']
	category=api[0]['Category']['Name']
	#latitude=api[0]['Latitude']
	#longitude=api[0]['Longitude']

	if category == "Good":
			weather_color = "#0C0"
	elif category == "Moderate":
			weather_color = "#FFFF00"
	elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff9900"
	elif category == "Unhealthy":
			weather_color = "#FF0000"
	elif category == "Very Unhealthy":
			weather_color = "#990066"
	elif category == "Hazardous":
			weather_color = "#660000"
	root.configure(bg=weather_color)


	label=Label(root,text=city + "  Air Quality:" + str(quality) + "  " +category,font=("Helvectica",20),bg=weather_color).grid(row=1,column=0,columnspan=3)
button=Button(root,text="submit",command=weather).grid(row=0,column=3)
mainloop()
