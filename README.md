# Leanspace Entertainment #2

This repo has Python code to launch a local server, and using Flask to set up some API endpoints.

It also has Python code to submit an API call to the server. 

It uses the column titles in constructing the key:value JSON data.

Added validation and first cut of try-catch error handling.

Added command line parameter to input different csv files for testing. See below.

Added api key submission. This is sent in the header. This is in test-mode so the API keys are hard coded for ease of testing. When placed into production, remove this hard coding and use ENV vars, some secret file, or Kubernetes.

## Running

There are two python files of note:
1. app.py - this is the server I wrote to simulate API endpoint.
1. leanspace.py - this is the sample code for a client to run.

Here is how to run them:
1. First launch the server: **python3 app.py**
1. Run the code for client: **python3 leanspace.py [csv filename]**
	1. Good data: **python3 leanspace.py leanspace.title.csv**
	1. Bad data:  **python3 leanspace.py leanspace.bad.csv**