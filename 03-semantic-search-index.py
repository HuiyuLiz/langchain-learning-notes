# references: https://docs.langchain.com/oss/python/langchain/knowledge-base

# from langchain_core.documents import Document

# documents = [
#     Document(
#         page_content="Dogs are great companions, known for their loyalty and friendliness.",
#         metadata={"source": "mammal-pets-doc"},
#     ),
#     Document(
#         page_content="Cats are independent pets that often enjoy their own space.",
#         metadata={"source": "mammal-pets-doc"},
#     ),
# ]

# print(documents)

# 1.Documents and document loaders;
from langchain_community.document_loaders import PyPDFLoader

file_path = "./example_data/nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

# print(len(docs))  # 107
# print(type(docs[0]))  # <class 'langchain_core.documents.base.Document'>
# print(docs[0])
# page_content='Table of Contents...'
# metadata={
# 'producer': 'EDGRpdf Service w/ EO.Pdf 22.0.40.0',
# 'creator': 'EDGAR Filing HTML Converter',
# 'creationdate': '2023-07-20T16:22:00-04:00',
# 'title': '0000320187-23-000039',
# 'author': 'EDGAR Online, a division of Donnelley Financial Solutions',
# 'subject': 'Form 10-K filed on 2023-07-20 for the period ending 2023-05-31',
# 'keywords': '0000320187-23-000039; ; 10-K', 'moddate': '2023-07-20T16:22:08-04:00',
# 'source': './example_data/nke-10k-2023.pdf',
# 'total_pages': 107,
# 'page': 0,
# 'page_label': '1'
# }

# Splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

# print(len(all_splits))  # 516
# print(all_splits[0])
# page_content='Table of Contents...'
# metadata={
# 'producer': 'EDGRpdf Service w/ EO.Pdf 22.0.40.0',
# 'creator': 'EDGAR Filing HTML Converter',
# 'creationdate': '2023-07-20T16:22:00-04:00',
# 'title': '0000320187-23-000039',
# 'author': 'EDGAR Online, a division of Donnelley Financial Solutions',
# 'subject': 'Form 10-K filed on 2023-07-20 for the period ending 2023-05-31',
# 'keywords': '0000320187-23-000039; ; 10-K',
# 'moddate': '2023-07-20T16:22:08-04:00',
# 'source': './example_data/nke-10k-2023.pdf',
# 'total_pages': 107,
# 'page': 0,
# 'page_label': '1',
# 'start_index': 0
# }

# 2. Embeddings
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_1 = embeddings.embed_query(all_splits[0].page_content)
vector_2 = embeddings.embed_query(all_splits[1].page_content)

assert len(vector_1) == len(vector_2)
# Generated vectors of length 4096
# print(f"Generated vectors of length {len(vector_1)}\n")
# [-0.0035884362, -0.029454533, -0.014293394, 0.0035685922, -0.0046553, -0.02508996, -0.0057297293, -0.007226704, -0.034405187, -0.00084568025]
# print(vector_1[:10])

# 3. Vector stores
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

ids = vector_store.add_documents(documents=all_splits)

print(f"id length {len(ids)}")  # id length 516
print(f"ids: {ids}")  # ids: ['08200420-911a-4f6d-b0af-d3b541ca7e8c'...]
