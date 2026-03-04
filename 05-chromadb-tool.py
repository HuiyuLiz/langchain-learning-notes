import collections
import chromadb


# list verctor data base collections and records
def list_collection(db_path):
    client = chromadb.PersistentClient(db_path)
    collections = client.list_collections()
    print(f"chromadb:{db_path} has {len(collections)} collections")

    for i, collection in enumerate(collections):
        print(f"collection {i}:{collection.name}, total {collection.count()} records")


# delete collection
def delete_collection(db_path, collection_name):
    try:
        client = chromadb.PersistentClient(db_path)
        client.delete_collection(collection_name)
    except Exception as e:
        print(f"delete {collection_name} failed. Error:{e}")


db_path = "./chroma_langchain_db"
collection_name = "example_collection"

list_collection(db_path)
# delete_collection(db_path, collection_name)
