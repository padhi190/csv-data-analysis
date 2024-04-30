from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd

def query_agent(data, llm, query):
    df = pd.read_csv(data)
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    return agent.run(query)