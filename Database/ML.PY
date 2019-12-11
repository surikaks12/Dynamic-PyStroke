import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json


data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["subject", "DU time o", "DU time r", "DU time a", "DU time n", "DU time g", "DU time shift", "DU time E", "DU time 2", "DU time 0", "DU time 1", "DU time 9", "DU time shift (2)", "DU time !", "UD time o", "UD time r", "UD time a", "UD time n", "UD time g", "UD time shift", "UD time E", "UD time 2", "UD time 0", "UD time 1", "UD time 9", "UD time shift (2)", "UD time !", "3GRAM1", "3GRAM2", "3GRAM3", "3GRAM4", "3GRAM5", "3GRAM6", "3GRAM7", "3GRAM8", "3GRAM9", "TOTAL TIME"],
                    "Values": [ [ "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], [ "value", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/3043ecf6e20c4e99a737ae96b99c0738/services/27b486e9443046edb210a535f9d51840/execute?api-version=2.0&details=true'
api_key = 'abc123' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
