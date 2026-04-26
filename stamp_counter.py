#Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.


no_country=5
stamp=['UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France']

def stamp_counter(no_country,stamp):
    print(len(set(stamp)))
    
stamp_counter(no_country,stamp)
