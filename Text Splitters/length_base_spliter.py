from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

doc = loader.load()

text_splitters = TokenTextSplitter(
    encoding_name='cl100k_base',
    chunk_size = 100,
    chunk_overlap = 22
)

text = text_splitters.split_documents(doc)
print(text[0].page_content)