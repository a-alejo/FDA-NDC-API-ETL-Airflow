import requests
import time
from config import api_key


def extract_data(**context):
    limit = 1000  # I got this number by testing on Postman
    all_results = []
    response = requests.get("https://api.fda.gov/drug/ndc.json")

    # get the total number of results from the request
    if response.status_code == 200:
        data = response.json()
        total_results = data["meta"]["results"]["total"]

        # print out the count
        print(f"Total results: {total_results}")

    else:
        print("Failed to fetch data", response.status_code)
        
    #  Limit the number of records to fetch to set maximum
    max_total = 10000
    max_records = min(total_results, max_total)

    # # loop through all the data and add to it the 'all_results' open list
    # for x in range(0, total_results, limit):
    #     if x >= total_results:
    #         break  # this is to prevent the issue of skipping past the results

    # Loop through the "maximum" amount
    for x in range(0, max_records, limit):
        site_map = requests.get(
            f"https://api.fda.gov/drug/ndc.json?api_key={api_key}&limit={limit}&skip={x}"
        )

        if site_map.status_code == 200:
            data = site_map.json()
            if "results" in data:
                all_results.extend(data["results"])


        else:
            print(
                f"failed to get data starting at {x} with a status code of {site_map.status_code}"
            )
            print(site_map.text)
            break

        # short delay to avoid rate limit
        time.sleep(1)

    # print out the count
    print(f"Final total results: {len(all_results)}")

    # Push results to XCom
    context["ti"].xcom_push(key="extracted_data", value=all_results)