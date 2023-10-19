Please Note that some of files in this repository are a part of the UNICEF proof of concept, namely ```export_dashboard.py```, ```api_request_handler.py```, ```create_derived_dashboard.py```, ```duplicate_chart.py```, ```create_empty_dashboard.py``` and ```superset_constants.py```.

The code written by our group members is in the following files: ```views.py```, ```main.py```, ```api_helpers.py```, ```index.html```, ```clone.html```, ```styles.css```, ```script.js``` and ```test_api.py```. We also made some edits to ```export_dashboard.py``` to fix the proof of concept, however we still need to talk to our partner for this first.


We have made a demo video that showcases our work: https://www.loom.com/share/313f3af5cae74cd7894e1832628ac7fb?sid=f6ce5dbe-ee9e-49fb-8970-dd4c2ccba697. 

For our subteam, to run the code a local instance of Apache Superset is required, which is quite difficult to set up. We are currently working with our partner to get an instance of superset hosted on the cloud for future submissions. 

Setup Instructions

(Superset is not supported by Windows so these steps are exclusively for MacOS and Linux. There are workarounds for Windows in the following links as well but we were not able to get it to work for some of our members)

To set up superset locally, execute the steps on this website: https://superset.apache.org/docs/installation/installing-superset-from-scratch/ 

Note that you may have to do some configuration for superset first, such as setting the secret key and the python path. Follow the steps on this website: https://superset.apache.org/docs/installation/configuring-superset/ 

To generate a secret key, use the following command:

`openssl rand -base64 42` 

To set the `PYTHONPATH`, use the following commands:

`export PYTHONPATH=/path/to/superset_config.py:$PYTHONPATH`

Finally, to run superset, run:

`superset run -p 8088 --with-threads --reload --debugger`


You can also try to set it up using docker compose: https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/

Unfortunately, since we require superset for the API calls to succeed, we cannot deploy the application. This is because it requires environemnt variables that point to a local instance of superset. You must clone our repository to run our code. Alternatively, you can also watch the demo video using the link at the top of the Readme. 

After cloning this repository, run the following command to install all the dependencies:

```pip install -r requirements.txt ``` 

Then, run ```python3 main.py``` to run the code. You can also use the command ```gunicorn main:app```
