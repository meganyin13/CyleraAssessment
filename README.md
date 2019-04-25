# interview-platform-take-home
Take-home test for platform development candidates

This test should take about 1-4 hours.

### Resources

`bandwidths.py` - Listing of bandwidth entry for devices, values are "bytes_ts" (bytes to server) and "bytes_fs" (bytes from server)

### Part 1
Using the Python framework of your choice (e.g. Flask, Django) create an API endpoint to display the data from `bandwidths.py`.

The values for bandwidth should be aggregated by `window_time` (default 60 seconds) in order to limit the data we send to the front end and the number of points we display.

*Parameters:*

    device_uuid (required)
    end_time (epoch timestamp of the last time we want to return, default now)
    window_time (window in seconds, default 60 seconds)
    num_windows (number of windows i.e., data points, to return, default 10)
    
    For example,
    device_uuid = "abc", end_time = 1546300800, window_time = 60, num_windows = 10
    would return 10 data points (timestamp, value) where each value would be the sum of bytes in that 60 second window, with the last window ending on 1546300800 (Jan 1st 2019 GMT).

The format of the response of this call is up to you so long as it properly powers the component you'll build in part 2.

### Part 2
Using the JS framework of your choice (e.g. React, Vue) consume the API endpoint you created in Part 1 and use it to render a chart using the charting library of your choice (e.g. FusionCharts, Chart.js).  This chart should consist of two lines - one for bandwidth to the server (`bytes_ts` in `bandwidths.py`) and one for bandwidth from the server (`bytes_fs` in `bandwidths.py`).

The API endpoint should accept 4 GET request parameters, allowing you to alter the chart window via address bar:
   ```
   device_uuid (required)
   end_time (optional, default now)
   window_time (optional, default 60)
   num_windows (optional, default 10)
   ```

### Running your Solution
Include a README.md with instructions to setup (e.g. `yarn install`) and run (e.g. `yarn start`) your solution
