#Write a Python program that reads JSON file containong NASA APOD data and prints the keys: "explanation","Title"
#Use this link to copy your json data (do not use request module, just save the JSON to the variable then do the json operation)
#Json Data url: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

import json

jsondata = '''
{
  "copyright": "Massimo Di Fusco",
  "date": "2024-07-06",
  "explanation": "Found among the rich starfields of the Milky Way, star cluster NGC 7789 lies about 8,000 light-years away toward the constellation Cassiopeia. A late 18th century deep sky discovery of astronomer Caroline Lucretia Herschel, the cluster is also known as Caroline's Rose. Its visual appearance in small telescopes, created by the cluster's complex of stars and voids, is suggestive of nested rose petals. Now estimated to be 1.6 billion years young, the galactic or open cluster of stars also shows its age. All the stars in the cluster were likely born at the same time, but the brighter and more massive ones have more rapidly exhausted the hydrogen fuel in their cores. These have evolved from main sequence stars like the Sun into the many red giant stars shown with a yellowish cast in this color composite. Using measured color and brightness, astronomers can model the mass and hence the age of the cluster stars just starting to \\\"turn off\\\" the main sequence and become red giants. Over 50 light-years across, Caroline's Rose spans about half a degree (the angular size of the Moon) near the center of the sharp telescopic image.",
  "hdurl": "https://apod.nasa.gov/apod/image/2407/NGC7789_difusco2048.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "NGC 7789: Caroline's Rose",
  "url": "https://apod.nasa.gov/apod/image/2407/NGC7789_difusco1024c.jpg"
}
'''

data = json.loads(jsondata)

print("Explanation:", data["explanation"])
print()
print("Title:", data["title"])