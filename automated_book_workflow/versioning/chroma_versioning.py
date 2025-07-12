import chromadb
import uuid

def save_version(text, metadata):
    print("[ChromaDB] Saving version...")
    client = chromadb.Client()
    collection = client.get_or_create_collection("book_versions")
    collection.add(documents=[text], metadatas=[metadata], ids=[str(uuid.uuid4())])

def query_versions(query_text):
    print("[ChromaDB] Querying versions...")
    client = chromadb.Client()
    collection = client.get_collection("book_versions")
    results = collection.query(query_texts=[query_text], n_results=3)
    return results
