# Megan Yin FrontEnd Take Home Assessment

## Start Flask Python Backend Endpoint
1. `cd flask-backend`
2. `python api_endpoint.py`

## Start Frontend
1. `cd frontend`
2. `yarn install` 
3. `yarn start`

## Change Data Displayed
1. go into `frontend/src/components/data.jsx`
2. change the url in `componentDidMount()` to `http://localhost:5000/<device_uuid>/<end_time>/<window_time>/<num_windows>`
   where `device_uuid` is the desired device id, `end_time` is the epoch timestamp of the last time 
   we want to return, `window_time` is window in seconds, `num_windows` is number of windows i.e., data points.
   For optional parameters, enter `...` in the place of that parameter in the url. For example, optional `end_time` would be
   `http://localhost:5000/<device_uuid>/.../<window_time>/<num_windows>`
