# End-to-end-Chatbot-using-Llama2
![Alt text](static/images/architecture.png)
# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```

### STEP 01- Create a python environment after opening the repository

```bash
python -m venv chatbotenv
```

```bash
source chatbotenv/Scripts/activate
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PROXY_URL = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_CLOUD = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_REGION = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open http://localhost:8080/
```

![Alt text](static/images/example.png)

### Stack Used:

- Python
- LangChain
- Flask
- Meta Llama2
- Pinecone