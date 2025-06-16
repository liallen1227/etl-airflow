import os
from pathlib import Path

import googlemaps
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MySQL_host")
gmaps_client = googlemaps.Client(key=API_KEY)
data_dir = Path("data", "spot")


def get_place_info(row, gmaps_client):
    """
    Retrieve Google Maps place details for a given row of data.

    Args:
        row (_PandasNamedTuple): A row from a DataFrame, typically passed from data.itertuples().
        gmaps_client (googlemaps.Client): An initialized Google Maps client instance.
            Make sure the API key is loaded from the .env file.

    Returns:
        dict: A dictionary containing place information (e.g. place_id, name, rating, address, etc.),
              and optionally an error message if the query fails.
    """
    # data.itertuples()的用法，只能讀取不能修改值，但是速度比較快
    id_open = row.Id
    name_open = row.Name
    region_open = row.Region
    town_open = row.Town
    add_open = row.Add
    query = f"{town_open} {name_open}"
    search_result = gmaps_client.places(query=query, language="zh-TW")
    # search_result可能包含多個json，也可能一個都沒有
    if not search_result["results"]:
        err_msg = f"{name_open} couldn't find the result.\n"
        return [], err_msg

    info_sublist = []
    for place in search_result["results"]:
        location = place.get("geometry", {}).get("location", {})
        info = {
            "id_open": id_open,
            "name_open": name_open,
            "region_open": region_open,
            "town_open": town_open,
            "add_open": add_open,
            "place_id": place.get("place_id", ""),
            "s_name": place.get("name", ""),
            "rate": place.get("rating", None),
            "comm": place.get("user_ratings_total", None),
            "types": place.get("types", []),
            "address": place.get("formatted_address", ""),
            "lng": location.get("lng", ""),
            "lat": location.get("lat", ""),
            "business_status": place.get("business_status", ""),
        }
        info_sublist.append(info)

    return info_sublist, ""


def main():
    read_file = data_dir / "spot02_added_rows_from_newdata_filtered.csv"
    save_file = data_dir / "spot03_googleapi_newdata.csv"
    err_log_file = data_dir / "spot03_googleapi_newdata_err_log.txt"
    data = pd.read_csv(
        read_file,
        encoding="utf-8",
        engine="python",
    )
    info_list = []
    err_log = ""
    for row in data.itertuples():
        info, err_msg = get_place_info(row, gmaps_client)
        info_list += info
        err_log += err_msg
        print(info)

    info_data = pd.DataFrame(info_list)
    info_data.to_csv(
        save_file,
        encoding="utf-8",
        header=True,
        index=False,
    )
    with open(err_log_file, "a", encoding="utf-8") as f:
        f.write(err_log)


if __name__ == "__main__":
    main()
