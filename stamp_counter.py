no_country=5
stamp=['UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France']

def stamp_counter(no_country,stamp):
    print(len(set(stamp)))
    
stamp_counter(no_country,stamp)