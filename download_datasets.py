import requests
import os
import sys

DATAGOUV_URL = "https://www.data.gouv.fr/api/1/datasets/"


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.makedirs(folder_name + '/files')
        os.makedirs(folder_name + '/documentation')
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists. Quit script")
        sys.exit()


def get_datasets_metadata(url):
    if "data.gouv.fr/" in url and "datasets" in url:
        id =  url.split("/")[-1]
        if id == "":
            id = url.split("/")[-2]
        r = requests.get(DATAGOUV_URL + id)
        if r.status_code == 200:
            print("Data found - retrieving metadata first")
            data = r.json()
            return data
        else:
            print("Data not found - please enter valid url")
            sys.exit()
    else:
        print("Not a valid url of a specific dataset")



def get_resources(resources, slug):
    for res in resources:
        if res["type"] == "documentation":
            path = slug + "/documentation/"
        else:
            path = slug + "/files/"
        title = res["title"].replace(" ", "_") + "." + res["format"]
            
        response = requests.get(res["url"])
        if response.status_code == 200:
            with open(path + title, 'wb') as file:
                file.write(response.content)
            print(f"File '{title}' downloaded successfully'.")
        else:
            print(f"Failed to download the file {title}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: download_datasets.py <datagouv_url_dataset>")
    else:
        url = sys.argv[1]
        data = get_datasets_metadata(url)
        if data:
            create_folder(data["slug"])
            get_resources(data["resources"], data["slug"])
