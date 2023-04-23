import numpy as np
import pandas as pd
from InstructorEmbedding import INSTRUCTOR
from sklearn.metrics.pairwise import cosine_similarity

model = INSTRUCTOR('hkunlp/instructor-large')

embeddings = np.load('data/embeddings.npy')
df = pd.read_csv('data/tesco_groceries.csv')
df['embeddings'] = embeddings.tolist()

while True:
    user_input = input("Enter a search term or 'exit' to quit: ")
    if user_input == 'exit':
        break
    else:
        query_embedding = model.encode([["Represent the Grocery question for retrieving supporting titles: ",user_input]])
        df['similarity'] = cosine_similarity(df['embeddings'].values.tolist(),query_embedding)
        df.sort_values(by=['similarity'],ascending=False,inplace=True)
        print(df[['title','price']].head(5))
        df.drop(columns=['similarity'],inplace=True)
        
