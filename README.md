Please Note that some of files in this repository are a part of the UNICEF proof of concept, namely ```export_dashboard.py```, ```api_request_handler.py```, ```create_derived_dashboard.py```, ```duplicate_chart.py```, ```create_empty_dashboard.py``` and ```superset_constants.py```.

The code written by our group members is in the following files: ```views.py```, ```main.py```, ```api_helpers.py```, ```index.html```, ```clone.html```, ```styles.css``` and ```script.js```. We also made some edits to ```export_dashboard.py``` to fix the proof of concept, however we still need to talk to our partner for this first.


For our subteam, a local instance of Apache Superset is required. We are currently working with our partner to get an instance of superset hosted on the cloud for future submissions.
Since superset is difficult to set up, we have also included a demo video here: https://www.loom.com/share/313f3af5cae74cd7894e1832628ac7fb?sid=f6ce5dbe-ee9e-49fb-8970-dd4c2ccba697

To set up superset locally, execute the steps on this website: https://superset.apache.org/docs/installation/installing-superset-from-scratch/

Note that you may have to do some configuration for superset first, such as setting the secret key and the python path. Follow the steps on this website: https://superset.apache.org/docs/installation/configuring-superset/ 

To generate a secret key, use the following command:

`openssl rand -base64 42` 

To set the `PYTHONPATH`, use the following commands:

`export PYTHONPATH=/path/to/superset_config.py:$PYTHONPATH`

Finally, to run superset, run:

`superset run -p 8088 --with-threads --reload --debugger`




Unfortunately, since we require superset for the API calls to succeed, we cannot deploy the application. You must clone our repository to run our code. Alternateively, you can also watch the demo video using the link at the top of the Readme. 

After cloning this repository, run the following command to install all the dependencies:

```pip install -r requirements.txt ``` 

Then, run ```python3 main,py``` to run the code. You can also use the command ```gunicorn main:app ```.
