from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

emb = embeddings.embed_query("hi there")

print(emb)

text_splitter = CharacterTextSplitter(
  separator='\n',
  chunk_size=200,
  chunk_overlap=100
)

loader = TextLoader("facts.txt", encoding='utf-8')
docs = loader.load_and_split(
  text_splitter=text_splitter
)

for doc in docs:
  print(doc.page_content)
  print("")

