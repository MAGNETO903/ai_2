# import
import uvicorn
from fastapi import FastAPI

from langchain.llms import LlamaCpp
from huggingface_hub import hf_hub_download

import time

print(time.ctime(), "app launched")




# read, parse and split documents

# our LLM
model_name_or_path = "TheBloke/Llama-2-7b-Chat-GGUF"
model_basename = "llama-2-7b-chat.Q4_K_M.gguf"
MODEL_PATH = hf_hub_download(repo_id=model_name_or_path, filename=model_basename)

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.2,
    max_tokens=2000,
    n_ctx = 1024*3,
    top_p=0.9, # Verbose is required to pass to the callback manager
    lang="ru",
)
app = FastAPI()
@app.get("/message")
def message(user_id: str, message: str):
    
    return {"message": llm(mesage)}

if __name__ == '__main__':
    uvicorn.run(app)
