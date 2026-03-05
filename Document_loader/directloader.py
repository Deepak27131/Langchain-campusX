from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path = 'book',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# doc = loader.load()

doc = loader.lazy_load()

for document in doc:
    print(document.metadata)

# print(len(doc))

# print(doc[0].page_content)
# print(doc[0].metadata)
