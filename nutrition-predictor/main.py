import warnings

import utils
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

warnings.filterwarnings("ignore")
load_dotenv(override=True)

def main():
    try:
        client_local = Elasticsearch("http://localhost:9200")
    except ConnectionError as err:
        print("Unable to connect to local Elasticsearch db: ", err)
        client_local = None
    if client_local != None: 
        utils.read_data()
        # local_indices = client_local.indices.get_alias(index="*")
        # local_client_docs = client_local.search(index="market-data")

if __name__ == "__main__":
    main()