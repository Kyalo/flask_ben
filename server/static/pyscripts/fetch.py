import requests

# URL of the endpoint you want to make a GET request to
url = 'http://127.0.0.1:5000/'

endpoints = {
    'users': f'{url}/users',
    'chat_data': f'{url}/chat_data',
    'user_conditions': f'{url}/user_conditions'
}

def get_data(endpoint):
    # GET data
    response = requests.get(endpoints[endpoint])

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the response content
        # Store JSON data in API_Data 
        API_Data = response.json() 
        
        # # Print json data using loop 
        # for key in API_Data:{ 
        #     print(key,":", API_Data[key]) 
        # }
        # print(API_Data)
        return(API_Data)
    else:
        # Print an error message if the request was not successful
        print(f'Error: {response.status_code}')
        return(f'Error: {response.status_code}')
 
