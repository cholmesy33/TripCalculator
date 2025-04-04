import googlemaps 
import datetime

API_KEY = 'AIzaSyAKtpjaZ9RczgTiu2u7kWslmo6LhYVaxsg'

gmaps = googlemaps.Client(key=API_KEY)

def get_time(start, finish, departure_time="now", arrival_time="now", mode="driving"):

    traffic_models = ["best_guess", "optimistic", "pessimistic"]

    call = gmaps.directions(
        start,
        finish,
        mode=mode,
        arrival_time=arrival_time,
        traffic_model=traffic_models[0]   
        )
    
    leg = call[0]['legs'][0]

    duration = leg['duration']['text']
    print(leg.keys())

    return(duration)

home = "52A Alexandra Place, Bentley, 6102"
work = "222 Fulham Street, Cloverdale, Perth"

goal_arrival_time = datetime.datetime(2025, 5, 5, 12, 0, 0)

duration = get_time(home, work, arrival_time=goal_arrival_time)

# output1 = output[0]['legs'][0]

# output2 = output1['duration']

print(duration)
# print(departure_time)



if __name__ == "__main__":
    print("Run Successfully")