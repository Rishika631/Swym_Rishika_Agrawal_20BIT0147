import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://Rishika:taylorswift@cluster0.acug8d2.mongodb.net/?retryWrites=true&w=majority")
db = client["railwaystation_timetable"]

# Load CSV into a DataFrame
df = pd.read_csv("DE_Assignment.csv")

# Insert data into MongoDB collections
for _, row in df.iterrows():
    train = {
        "train_number": row["Train No"],
        "train_name": row["Train Name"]
    }
    station = {"station_name": row["Station Name"]}
    schedule = {
        "train_number": row["Train No"],
        "train_name": row["Train Name"],
        "seq": row["SEQ"],
        "station_code": row["Station Code"],
        "station_name": row["Station Name"],
        "arrival_time": row["Arrival time"],
        "departure_time": row["Departure Time"],
        "distance": row["Distance"],
        "source_station": row["Source Station"],
        "source_station_name": row["Source Station Name"],
        "destination_station": row["Destination Station"],
        "destination_station_name": row["Destination Station Name"]
    }
    
    db.trains.insert_one(train)
    db.stations.insert_one(station)
    db.schedules.insert_one(schedule)

print("Data loaded into MongoDB collections.")
