from InstructorEmbedding import INSTRUCTOR
import pandas as pd
import numpy as np

print("Loading embedding model...")
model = INSTRUCTOR('hkunlp/instructor-large')
instruction = "Represent the Grocery title for retrieval:"

df = pd.read_csv('data/tesco_groceries.csv')

titles = df['title'].values

instructions_pairs = [
    [instruction,title] for title in titles
]

print("Calculating embeddings...")
embeddings = model.encode(instructions_pairs,show_progress_bar=True)

print("Saving embeddings...")
#write the embeddings array as is to a file in data/embeddings.txt
np.save('data/embeddings.npy', embeddings)