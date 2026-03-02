# references: https://docs.langchain.com/oss/python/langchain/knowledge-base

from langchain_core.documents.base import Document


from codecs import charmap_build
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from typing import List
from langchain_core.documents import Document
from langchain_core.runnables import chain

# Embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Vector stores
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# 1.Return documents based on similarity to a string query
print("===== Return documents based on similarity to a string query: =====")
results = vector_store.similarity_search(
    "How many distribution centers does Nike have in the US?"
)

for index, result in enumerate(results):
    print(f"{index, result.page_content}")

# 2.Return scores:
# Note that providers implement different scores; the score here
# is a distance metric that varies inversely with similarity.
print("===== Return scores: =====")
results = vector_store.similarity_search_with_score("What was Nike's revenue in 2023?")

# doc, score = results[0]
# print(f"Score: {score}\n")
# print(doc)

for doc, score in results:
    print(f"score: {score}\n {doc.page_content}")

# Return documents based on similarity to an embedded query:
print("===== Return documents based on similarity to an embedded query: =====")
embedding = embeddings.embed_query("How were Nike's margins impacted in 2023?")

results = vector_store.similarity_search_by_vector(embedding)
print(results[0])


# Retrievers
print("===== Retrievers: =====")


@chain
def retriever(query: str) -> List[Document]:
    return vector_store.similarity_search(query, k=1)


results = retriever.batch(
    [
        "How many distribution centers does Nike have in the US?",
        "When was Nike incorporated?",
    ],
)

for index, result in enumerate(results):
    print(f"index:{index} {result}")
