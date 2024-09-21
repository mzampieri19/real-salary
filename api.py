import pandas as pd
import requests
import time


data = pd.read_csv('df_filtered_country.csv')
api_key = '66dc9396a4017137098674csy2f4d8a'

def main():
    # Loop through the data
    for index, row in data.iterrows():
        print(f"Processing row {index}")
        # Get the data
        lat = data['latitude'][index]
        lon = data['longitude'][index]

        # Call the API
        url = f"https://geocode.maps.co/reverse?lat={lat}&lon={lon}&api_key=66dc9396a4017137098674csy2f4d8a"
        print(f"Calling API")
        response = requests.get(url)
        time.sleep(2)

        if response.status_code == 200:
            try:
                response_json = response.json()

                # Save the data
                if 'address' in response_json:
                    address_info = response_json['address']
                    data.at[index, 'address'] = address_info.get('road', '')
                    data.at[index, 'county'] = address_info.get('county', '')
                    data.at[index, 'city'] = address_info.get('village', '')  # 'village' used in the example response
                    data.at[index, 'state'] = address_info.get('state', '')
                    data.at[index, 'country'] = address_info.get('country', '')
                else:
                    data.at[index, 'address'] = ''
                    data.at[index, 'county'] = ''
                    data.at[index, 'city'] = ''
                    data.at[index, 'state'] = ''
                    data.at[index, 'country'] = ''
            except ValueError:
                print(f"Error decoding JSON for row {index}")
                data.at[index, 'address'] = ''
                data.at[index, 'county'] = ''
                data.at[index, 'city'] = ''
                data.at[index, 'state'] = ''
                data.at[index, 'country'] = ''
        else:
            print(f"Error with API request for row {index}: {response.status_code}")
            data.at[index, 'address'] = ''
            data.at[index, 'county'] = ''
            data.at[index, 'city'] = ''
            data.at[index, 'state'] = ''
            data.at[index, 'country'] = ''

        # Wait for 1 second to avoid hitting the rate limit
        time.sleep(1)

    # Save the data after the loop
    data.to_csv('filtered_country_with_address.csv', index=False)
    print("Data saved")

main()
