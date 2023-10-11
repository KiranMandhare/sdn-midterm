from flask import Flask,render_template, request
import datetime
from collections import deque

app = Flask(__name__)
showdatapoints = 10
timestamps = deque(maxlen=showdatapoints)
counts = deque(maxlen=showdatapoints)

totalCount = 0

@app.route("/updatePacketInCount", methods=["POST"])
def updatePacketInCount():
    timestamp = request.json['timestamp']
    count = request.json['count']
    timestamps.append(timestamp)
    counts.append(int(count))
    global totalCount
    totalCount = totalCount + int(count)
    return '',200
@app.route("/", methods=["GET"])
def indexPage():
    return render_template("index.html",totalCount=totalCount, timestamps=list(timestamps), counts=list(counts))

if __name__ == "__main__":
    time = datetime.datetime.now()

    for i in range(0,showdatapoints):
        timestamps.appendleft(time.strftime("%H:%M:%S"))
        counts.append(0)
        time = time - datetime.timedelta(seconds=5)
    app.run(host='0.0.0.0',port=9000)