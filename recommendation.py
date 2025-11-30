import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.DataFrame({
    "user": [1,1,1,2,2,3,3,4,4],
    "item": ["A","B","C","A","C","B","C","A","B"],
    "rating": [5,3,4,4,5,2,5,4,3]
})

items = ratings.pivot_table(index="user", columns="item", values="rating")
items_filled = items.fillna(0)

similarity = cosine_similarity(items_filled)
similarity_df = pd.DataFrame(similarity, index=items.index, columns=items.index)

def recommend(user_id):
    scores = similarity_df[user_id].drop(user_id)
    best_user = scores.idxmax()
    user_items = set(ratings[ratings.user == user_id].item)
    best_items = ratings[ratings.user == best_user]
    rec = best_items[~best_items.item.isin(user_items)]
    return rec.item.tolist()

print(recommend(1))
