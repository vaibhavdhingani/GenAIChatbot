from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone as PineconeClient
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
import time
import torch

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
PROXY_URL = os.environ.get('PROXY_URL')
PINECONE_CLOUD = os.environ.get('PINECONE_CLOUD')
PINECONE_REGION = os.environ.get('PINECONE_REGION')


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


#Initializing the Pinecone
pc = PineconeClient(api_key=os.environ.get('PINECONE_API_KEY'),
                    proxy_url=os.environ.get('PROXY_URL'))

cloud = os.environ.get('PINECONE_CLOUD') or 'aws'
region = os.environ.get('PINECONE_REGION') or 'us-east-1'
spec = ServerlessSpec(cloud=cloud, region=region)

index_name="genaichatbot"

# check if index already exists (it shouldn't if this is first time)
if index_name not in pc.list_indexes().names():
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=384,  # dimensionality of text-embedding-ada-002
        metric='cosine',
        spec=spec
    )
    # wait for index to be initialized
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)

# connect to index
index = pc.Index(index_name)
# view index stats
index.describe_index_stats()

#Creating Embeddings for Each of The Text Chunks & storing
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2').to(device)
sentences = [t.page_content for t in text_chunks]
embeddings_sentences =  model.encode(sentences)  

id = 0
vectors = []
for d, e in zip(text_chunks, embeddings_sentences):
    id = id+1
    vectors.append({
        "id": str(id),
        "values": e,
        "metadata": {'page_content': d.page_content}
    })

index.upsert(
    vectors=vectors,
    namespace="nschatbot"
)