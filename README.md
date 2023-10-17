[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/AvkT738V)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12294978&assignment_repo_type=AssignmentRepo)

For our subteam, a local instance of Apache Superset is required. We are currently working with our partner to get an instance of superset hosted on the cloud for future submissions.
Since superset is difficult to set up, we have also included a demo video here: [INSERT LINK]

To set up superset locally, execute the steps on this website: https://superset.apache.org/docs/installation/installing-superset-from-scratch/

Note that you may have to do some configuration for superset first, such as setting the secret key and the python path. Follow the steps on this website: https://superset.apache.org/docs/installation/configuring-superset/ 

To generate a secret key, use the following command:
`openssl rand -base64 42` 

To set the `PYTHONPATH`, use the following commands:
`export PYTHONPATH=/path/to/superset_config.py:$PYTHONPATH`

Finally, to run superset, run:
`superset run -p 8088 --with-threads --reload --debugger`
