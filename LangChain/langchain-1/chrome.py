from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
  separator='\n',
  chunk_size=200,
  chunk_overlap=0
)

loader = TextLoader("facts.txt", encoding='utf-8')
docs = loader.load_and_split(
  text_splitter=text_splitter
)

db = Chroma.from_documents(
  docs,
  embedding=embeddings,
  persist_directory="emb"
)

# results = db.similarity_search_with_score(
#   "What is an interesting fact about the English language?"
# )

# for rst in results:
#   print('\n')
#   print(rst[1])
#   print(rst[0].page_content)

results = db.similarity_search(
    "What is an interesting fact about the English language?"
)

for rst in results:
    print("\n")
    print(rst.page_content)
