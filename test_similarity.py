#embeddings.npy and tesco_groceries.csv are in the data folder
#they both have the same number of rows that correspond to each other
#load the embeddings.npy file and the tesco_groceries.csv file
#and create an embeddings column in the tesco_groceries.csv file with its respective embedding

import numpy as np
import pandas as pd
from InstructorEmbedding import INSTRUCTOR
from sklearn.metrics.pairwise import cosine_similarity

model = INSTRUCTOR('hkunlp/instructor-large')

embeddings = np.load('data/embeddings.npy')
df = pd.read_csv('data/tesco_groceries.csv')
df['embeddings'] = embeddings.tolist()

while True:
    #take input from user and run similarity search against the embedding column, return the top 5 results for the cols title and price
    #if the user enters 'exit' then break the loop

    user_input = input("Enter a search term or 'exit' to quit: ")
    if user_input == 'exit':
        break
    else:
        #encode the user input
        query_embedding = model.encode([["Represent the Grocery question for retrieving supporting titles: ",user_input]])
        #create a temporary similarity column in the df
        df['similarity'] = cosine_similarity(df['embeddings'].values.tolist(),query_embedding)
        #sort the df by the similarity column
        df.sort_values(by=['similarity'],ascending=False,inplace=True)
        #print the top 5 results
        print(df[['title','price']].head(5))
        #remove the temporary similarity column
        df.drop(columns=['similarity'],inplace=True)
        
