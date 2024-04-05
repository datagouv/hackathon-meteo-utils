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
        if res["title"].split(".")[-1] != res["format"]:
            format = "." + res["format"]
        else:
            format = ""
        title = res["title"].replace(" ", "_") + format
            
        response = requests.get(res["url"])
        if response.status_code == 200:
            with open(path + title, 'wb') as file:
                file.write(response.content)
            print(f"File '{title}' downloaded successfully'.")
        else:
            print(f"Failed to download the file {title}.")


def filter_res_by_date(data, run):
    resources = []
    for res in data["resources"]:
        if run in res["title"]:
            resources.append(res)
    data["resources"] = resources
    return data


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: download_datasets.py <mot-cle-pnt>")
    else:
        motscles = sys.argv[1]
        for item in motscles.split(","):
            if item == "arpege01":
                url = "https://meteo.data.gouv.fr/datasets/65bd13b2eb9e79ab309f6e63"
            if item == "arpege025":
                url = "https://meteo.data.gouv.fr/datasets/65bd13e557b26b467363b521"
            if item == "arome001":
                url = "https://meteo.data.gouv.fr/datasets/65bd1247a6238f16e864fa80"
            if item == "arome0025":
                url = "https://meteo.data.gouv.fr/datasets/65bd12d7bfd26e26804204cb"
            if item == "arome-om-antil":
                url = "https://meteo.data.gouv.fr/datasets/65bd162b9dc0d31edfabc2b9"
            if item == "arome-om-indien":
                url = "https://meteo.data.gouv.fr/datasets/65bd1560c73941a5e0ec1891"
            if item == "arome-om-ncaled":
                url = "https://meteo.data.gouv.fr/datasets/65bd14cca6919e97e9699b09"
            if item == "arome-om-polyn":
                url = "https://meteo.data.gouv.fr/datasets/65bd1509cc112e6a1458ab95"
            if item == "arome-om-guyane":
                url = "https://meteo.data.gouv.fr/datasets/65e0bd4b88e4fd88b989ba46"

            data = get_datasets_metadata(url)
            if len(sys.argv) > 2:
                data = filter_res_by_date(data, sys.argv[2])
            if data["resources"]:
                create_folder(data["slug"])
                get_resources(data["resources"], data["slug"])
            else:
                print("Run non disponible")
