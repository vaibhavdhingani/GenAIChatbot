from setuptools import find_packages,setup

setup(
    name = 'GenAI Chatbot',
    version= '0.0.0',
    author= 'Vaibhav Dhingani',
    author_email= 'vaibhavdhingani@gmail.com',
    packages= find_packages(),
    install_requires = ["ctransformers","sentence-transformers","pinecone-client","langchain","flask","pypdf","python-dotenv"]
)