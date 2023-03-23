import tkinter as tk
import requests

def weather_data(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273)
    temp_max = int(json_data['main']['temp_min']-273)
    temp_min = int(json_data['main']['temp_max']-273)
    pressure = int(json_data['main']['pressure']-273)
    humidity = json_data['main']['humidity']
    speed = json_data['wind']['speed']

    finalinfo = condition +"\n" +str(temp) + "F"
    finaldata =  "\n" " Min temp " + str(temp_min) + " F" + "\n" + " Max temp " + str(temp_max) + " F" + "\n" " Pressure " + str(pressure) + "\n" " Humadity " + str(humidity) + "\n" " speed " + str(speed)
    label1.config(text = finalinfo)
    label2.config(text = finaldata)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Mb Weather App")
f = ( "Arial" ,15 , "bold" )
t = ( "Arial" ,35 , "bold"  )
 
textField = tk.Entry( canvas , justify='center' , width= 20 , font = t )
textField.pack(pady = 20)
textField.focus()
textField.bind( '<Return>' , weather_data )


label1 = tk.Label( canvas , font = t)
label1.pack()
label2 = tk.Label( canvas , font = f)
label2.pack()

canvas.mainloop() 




     
