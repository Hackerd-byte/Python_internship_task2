import requests
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
cityname="Erode"
API_Key="0673a03098dc1a3c4fa2c761c56abcc2"
url=f'https://api.openweathermap.org/data/2.5/forecast?q={cityname}&appid={API_Key}&units=metric'
response=requests.get(url)
data=response.json()
tempratures=[item['main']['temp'] for item in data['list']]
times=[item['dt_txt'] for item in data['list']]
x=np.array(times)
y=np.array(tempratures)
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xticks(rotation=45)
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title(f"5-Day Forecast Temperature for {cityname}")
plt.tight_layout()
plt.grid(True)
plt.savefig("first.png")
plt.show()

