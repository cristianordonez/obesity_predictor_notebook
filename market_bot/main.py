import os
import warnings

from dotenv import load_dotenv
from elasticsearch import Elasticsearch, helpers

warnings.filterwarnings("ignore")
load_dotenv(override=True)

def main():
    try:
        client_local = Elasticsearch("http://localhost:9200")
    except Exception as err:
        print("Unable to connect to local Elasticsearch db: ", err)
        client_local = None

    if client_local != None: 
        print(client_local.info())
        
        local_indices = client_local.indices.get_alias(index="*")
        print('local_indices: ', local_indices)

        local_client_docs = client_local.search(index="market-data")

        print('local client: ', local_client_docs['hits']['total']['value'])
if __name__ == "__main__":
    main()