**1. A summary of your decisions and the options you considered for your component(s) (UI/frontend, logic/backend, database) so your TA knows what you have built and why.**

Since our subteam was focused on the backend, we chose to use Flask and Python. This is because the proof of concept made by the UNICEF team was also built in Python. 
We used Flask since Apache Superset is also built using Flask. Additionally, within Python, we made API calls to the Apache Superset API using the Python requests library. 
No other options were truly considered as we wanted to be consistent with the choices that have been made by previous teams. 

For the frontend, we chose to use HTML, CSS, and JS, as it was the simplest choice to create a fully functional frontend mockup.
Additionally, an additional benefit is that it should be relatively simple to switch from HTML to React when we merge with the dedicated frontend sub-team.

**2. Individual contributions explaining who did what. You can keep it to at most one paragraph per person to highlight any work that is not captured in any of the repos.**

_Andrew_

My first responsibility was to come up with an initial design for the backend for the subteam to follow. When that was complete, I ended up focusing on creating 
the server and the frontend mockups to test whether the backend was working. When creating the initial files for the server, I made sure to keep clear instructions 
of how to connect the backend to the server. Then I created the HTML, CSS, and JS files that would be used to display the data that the backend retrieves from the 
Apache Superset API calls. Just to note, ChatGBT was used to create the dynamic functionality of the dropdown menus, as I have no prior experience working with JS, 
as well as for a template CSS file. Upon completing my part, I worked with Manya to debug certain issues with the backend. This includes retrieving the charts through 
the API calls, and merging our separate branches together. As my laptop cannot run Superset, the scope of my work was limited to anything that did not involve having Superset.

_Manya_

Manya focused on the backend of the user story. She first did a lot of set up, including installing a local instance of superset, and loading it with sample data. She then 
handled the HTTPs responses made by the front end when the user lands on the home page, and when they press “clone”. Manya used the python requests library to make API calls 
to the Apache Superset API using multiple endpoints to get access tokens, as well as all the information for the dashboards, charts and datasets that would be sent to the 
frontend. She used Postman to test the API responses as well. Manya also worked with the existing proof of concept code, and found some issues that need to be discussed with 
our partner. She attempted to fix the issue by converting the yaml file into json, however more time and input from UNICEF is needed for this. 

**3. All the details and instructions needed for your TA to see and verify your work. You need to provide enough documentation so your TA can confirm:**

All relevant information on this topic is located in README.md

**4. Your application (see deployment section below for details)**

Unfortunately, since we require superset for the API calls to succeed, we cannot deploy the application. We are currently not able to host a version of superset for others to use.
You must clone our repository to run our code (assuming you have a local instance of Superset). Alternatively, you can also watch the demo video using the link at the top of the Readme.
This issue will be rectified after meeting with our contact at UNICEF, as he has said he would be able to host a version of Superset for the team to use.
