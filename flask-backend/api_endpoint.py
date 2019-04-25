from flask import Flask, jsonify
from flask_cors import CORS

import bandwidths
import time
import functools

app = Flask(__name__)
CORS(app)


@app.route('/<string:device_uuid>/<int:end_time>/<int:window_time>/<int:num_windows>', methods=['GET'])
def index(device_uuid, end_time = time.time(), window_time = 60, num_windows = 10):
    right_device = list(filter(lambda x: x['device_id'] == device_uuid, bandwidths.BANDWIDTHS))
    result = []
    for i in range(0,num_windows):
        end_time_interval = end_time - (i)*window_time
        begin_time= end_time - (i+1)*window_time
        time_interval = list(filter(lambda x: (x['timestamp'] >= begin_time) and (x['timestamp'] <= end_time_interval), right_device))

        bytes_fs = sum(time_interval[i]['bytes_fs'] for i in range(len(time_interval)))
        bytes_ts = sum(time_interval[i]['bytes_ts'] for i in range(len(time_interval)))

        # if (len(time_interval) > 0):

        t = {
            'ts': end_time_interval,
            'bytes_fs': bytes_fs,
            'bytes_ts': bytes_ts,
        }
        result.append(t)
        # else:
        #     t = {
        #         'ts': end_time_interval,
        #         'bytes_fs': 0,
        #         'bytes_ts': 0,
        #     }
        #     result.append(t)
    return jsonify({"result": result})



@app.route('/<string:device_uuid>/.../<int:window_time>/<int:num_windows>', methods=['GET'])
def opt1(device_uuid, window_time, num_windows):
    return index(device_uuid=device_uuid, window_time=window_time, num_windows=num_windows)

@app.route('/<string:device_uuid>/.../.../<int:num_windows>', methods=['GET'])
def opt2(device_uuid, num_windows):
    return index(device_uuid=device_uuid, num_windows=num_windows)

@app.route('/<string:device_uuid>/.../<int:window_time>', methods=['GET'])
def opt3(device_uuid, window_time):
    return index(device_uuid=device_uuid, window_time=window_time)

@app.route('/<string:device_uuid>/<int:end_time>/.../...', methods=['GET'])
def opt4(device_uuid, end_time):
    return index(device_uuid=device_uuid, end_time=end_time)

@app.route('/<string:device_uuid>/<int:end_time>/<int:window_time>', methods=['GET'])
def opt5(device_uuid, end_time, window_time):
    return index(device_uuid=device_uuid, end_time=end_time, window_time=window_time)

@app.route('/<string:device_uuid>/<int:end_time>/.../<int:num_windows>', methods=['GET'])
def opt6(device_uuid, end_time, num_windows):
    return index(device_uuid=device_uuid, end_time=end_time, num_windows=num_windows)

@app.route('/<string:device_uuid>/<int:end_time>/<int:window_time>/...', methods=['GET'])
def opt7(device_uuid, end_time, num_windows):
    return index(device_uuid=device_uuid, end_time=end_time, window_time=window_time)



if __name__ == '__main__':
    app.run(debug=True)
