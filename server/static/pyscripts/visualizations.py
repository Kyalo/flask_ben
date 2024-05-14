import matplotlib.pyplot as plt
import requests
# from fetch import get_data

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
 



def get_genders(json_data):
    gender_counts = {'Male': 0, 'Female': 0, 'Other': 0}  # Initialize counts for each gender
    for entry in json_data:
        gender = entry.get('gender', 'Other')  # Get the 'gender' value from each entry or default to 'Other'
        if gender in gender_counts:
            gender_counts[gender] += 1  # Increment the count for the corresponding gender
        else:
            gender_counts['Other'] += 1  # Increment the count for 'Other' if gender is not in predefined options
    return gender_counts


def get_age_data(json_data):
    age_ranges = {
        '18-24': 0,
        '25-34': 0,
        '35-44': 0,
        '45-54': 0,
        '55+': 0
    }
    for entry in json_data:
        age = entry.get('age', 0)  # Get the 'age' value from each entry or default to 0
        if 18 <= age <= 24:
            age_ranges['18-24'] += 1
        elif 25 <= age <= 34:
            age_ranges['25-34'] += 1
        elif 35 <= age <= 44:
            age_ranges['35-44'] += 1
        elif 45 <= age <= 54:
            age_ranges['45-54'] += 1
        else:
            age_ranges['55+'] += 1
    return age_ranges


def get_location_data(json_data):
    location_counts = {}
    for entry in json_data:
        location = entry.get('location')  # Get the 'location' value from each entry
        if location:
            location_counts[location] = location_counts.get(location, 0) + 1  # Increment count for location or initialize count to 1 if location is encountered for the first time
    return location_counts


data = get_data('users')

gender_data = get_genders(data)
age_data = get_age_data(data)
location_data = get_location_data(data)

# User Demographics Analysis Visualization

# Gender Distribution
plt.figure(figsize=(8, 6))
plt.bar(gender_data.keys(), gender_data.values(), color=['blue', 'pink', 'green'])
plt.title('Gender Distribution of Users')
plt.xlabel('Gender')
plt.ylabel('Number of Users')
plt.show()

# Age Distribution
plt.figure(figsize=(8, 6))
plt.bar(age_data.keys(), age_data.values(), color='orange')
plt.title('Age Distribution of Users')
plt.xlabel('Age Group')
plt.ylabel('Number of Users')
plt.show()

# Location Distribution
plt.figure(figsize=(10, 6))
plt.bar(location_data.keys(), location_data.values(), color='purple')
plt.title('Location Distribution of Users')
plt.xlabel('Location')
plt.ylabel('Number of Users')
plt.xticks(rotation=45)
plt.show()