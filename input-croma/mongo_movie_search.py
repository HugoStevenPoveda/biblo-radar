# mongo_movie_search.py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

class MongoMovieSearch:
    def __init__(self, uri, db_name, collection_name):
        self.uri = uri
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.df = pd.DataFrame(list(self.collection.find({})))
        self._check_connection()

    def _check_connection(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def search_movie_by_plot(self, query):
        pelicula_sobre_libro = self.df[self.df['plot'].str.contains(query, case=False, na=False)]
        if not pelicula_sobre_libro.empty:
            return pelicula_sobre_libro['plot_embedding'].tolist()[0]
        else:
            return None

    def run_pipeline(self, pipeline):
        result = self.collection.aggregate(pipeline)
        return list(result)

    def get_similar_movies(self, query, index_name, num_candidates=200, limit=3):
        embedding = self.search_movie_by_plot(query)
        if embedding is None:
            print("No movies found with the given plot query.")
            return []

        pipeline = [
            {
                '$vectorSearch': {
                    'index': index_name,
                    'path': 'plot_embedding',
                    'queryVector': embedding,
                    'numCandidates': num_candidates,
                    'limit': limit
                }
            },
            {
                '$project': {
                    '_id': 0,
                    'title': 1,
                    'genres': 1,
                    'plot': 1,
                    'fullplot': 1,
                    'year': 1,
                    'released': 1,
                    'score': {
                        '$meta': 'vectorSearchScore'
                    }
                }
            }
        ]

        return self.run_pipeline(pipeline)

# Example usage
