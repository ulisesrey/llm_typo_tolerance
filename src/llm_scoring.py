import pandas as pd
import csv
from langchain_ollama import ChatOllama 
from pathlib import Path
from tqdm import tqdm

# read csvs
df = pd.read_csv("data/typos.csv")
df_source = pd.read_csv("data/source.csv")
llm_scores = Path("data/llm_scores.csv")
model = "mistral:latest"
temp = 0.0


with llm_scores.open("w", newline="") as f:
    writer = csv.writer(f)
    #output will be
    writer.writerow(["question_id", "typo_method", "iteration", "llm_model", "temperature", "llm_answer", "score"])
    
    # create llm
    llm = ChatOllama(model=model,
                     temperature=temp,
                     num_predict=50,
                     reasoning=False)

    for idx, series in tqdm(df.iterrows()):
        round = series["round"]
        question_id = series["question_id"]
        typo_method = series["typo_method"]
        iteration = series["iteration"]
        question = series["question_with_typo"]
        answer = df_source["answer"][question_id]
        # add question mark
        question = question + "?"

        response = llm.invoke(question)
        #print(response.content)
        if answer in response.content.lower():
            score=1        
        else:
            score=0
        # write result
        writer.writerow([
            question_id,
            typo_method,
            iteration,
            model,
            temp,
            response.content,
            score
        ])