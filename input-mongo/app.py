from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from mongo_movie_search import MongoMovieSearch

class MovieDetails(BaseModel):
    title: str
    genres: List[str]
    plot: str
    full_plot: str
    year: int
    released: Optional[datetime]
    score: float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos (GET, POST, etc.)
    allow_headers=["*"],  # Headers permitidos
)


# Replace this with your actual MongoDB URI
uri = "mongodb+srv://hugostevenpoveda:BoPmztTv1J7YndQj@cluster0.71qynzg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_search = MongoMovieSearch(uri, 'sample_mflix', 'embedded_movies')

@app.get("/movies", response_model=List[MovieDetails])
def get_similar_movies(query: str, index_name: str = "vector-search-tutorial"):
    similar_movies = mongo_search.get_similar_movies(query, index_name)
    if not similar_movies:
        raise HTTPException(status_code=404, detail="No movies found with the given plot query.")
    
    movie_details_list = [
        MovieDetails(
            title=movie['title'],
            genres=movie['genres'],
            plot=movie['plot'],
            full_plot=movie['fullplot'],
            year=movie['year'],
            released=movie['released'],
            score=movie['score']
        ) for movie in similar_movies
    ]
    return movie_details_list

# To run the FastAPI app using Uvicorn:
# uvicorn main:app --reload
