import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    API_KEY = "f34d06ee4573c6af18fe05b14ba1614b"

    # Use Current Weather Data API (Free tier)
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)
    data = response.json()

    print("Request URL:", response.url)
    print("Response Code:", response.status_code)
    print("Response JSON:", data)

    if response.status_code != 200 or 'main' not in data: 
        messagebox.showerror("Error", "City not found or weather data unavailable.")
        return

    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    result_label.config(text=f"{city.title()}: {temp}°C, {desc}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="lightblue")

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack(pady=20)

root.mainloop()
