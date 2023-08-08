from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb+srv://Rishika:taylorswift@cluster0.acug8d2.mongodb.net/?retryWrites=true&w=majority")
db = client["railwaystation_timetable"]

# Schedule Collection Schema: {
#    "train_number": ...,
#    "train_name": ...,
#    "seq": ...,
#    "station_code": ...,
#    "station_name": ...,
#    "arrival_time": ...,
#    "departure_time": ...,
#    "distance": ...,
#    "source_station": ...,
#    "source_station_name": ...,
#    "destination_station": ...,
#    "destination_station_name": ...
# }

@app.route("/trains_at_midnight")
def trains_at_midnight():
    trains = db.schedules.find({"arrival_time": "00:00:00"})
    result = [{"train_number": train["train_number"], "train_name": train["train_name"]} for train in trains]
    return render_template("trains_at_midnight.html", trains=result)
    #return jsonify(result)

@app.route("/halt_stats")
def halt_stats():
    halt_times = []
    schedules = db.schedules.find()
    
    for schedule in schedules:
        arrival_time = datetime.strptime(schedule["arrival_time"], "%H:%M:%S")
        departure_time = datetime.strptime(schedule["departure_time"], "%H:%M:%S")
        
        # Handling midnight cases
        if arrival_time > departure_time:
            departure_time = departure_time.replace(day=departure_time.day + 1)
            
        halt_time = departure_time - arrival_time
        halt_times.append(halt_time.seconds // 60)  # Convert to minutes
    
    max_halt = max(halt_times)
    min_halt = min(halt_times)
    avg_halt = sum(halt_times) / len(halt_times)
    
    return render_template("halt_stats.html", max_halt=max_halt, min_halt=min_halt, avg_halt=avg_halt)
    #return jsonify({"max_halt": max_halt, "min_halt": min_halt, "avg_halt": avg_halt})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trains_between_stations")
def trains_between_stations():
    start_station = request.args.get("start_station")
    end_station = request.args.get("end_station")
    
    # Find the sequences of start and end stations
    start_station_seq = db.schedules.find_one({"station_name": start_station})["seq"]
    end_station_seq = db.schedules.find_one({"station_name": end_station})["seq"]
    
    # Determine the direction based on sequence numbers
    direction_condition = "$gt" if start_station_seq < end_station_seq else "$lt"
    
    # Query for trains passing between start and end stations in one direction
    trains = db.schedules.aggregate([
        {"$match": {
            "station_name": {"$in": [start_station, end_station]},
            "seq": {direction_condition: start_station_seq, "$lte": end_station_seq}
        }},
        {"$group": {"_id": "$train_number"}},
        {"$project": {"_id": 0, "train_number": "$_id"}}
    ])
    
    result = list(trains)
    num_trains = len(result)
    
    response = {
        "num_trains": num_trains,
        "trains": result
    }
    return render_template("result.html", num_trains=num_trains, trains=result)
    #return render_template("index.html")
    #return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)


