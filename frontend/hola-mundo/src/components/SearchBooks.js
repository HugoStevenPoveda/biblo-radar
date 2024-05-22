import React, { useState } from 'react';
import axios from 'axios';
import ListaLibros from './ListaLibros';



function SearchBooks() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSearch = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await axios.get(`http://localhost:8000/libro/${query}`);
            console.log(response.data);
            setResults(response.data);
            console.log("///////////////////////////");
            console.log({ results });

        } catch (err) {
            setError('Error fetching data. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h3>Buscar Libro Deseado</h3>
            <form onSubmit={handleSearch}>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Ingrese el nombre del libro"
                />
                <button type="submit">Buscar</button>
            </form>
            {loading && <p>Cargando...</p>}
            {error && <p>{error}</p>}
            <div>
                <ListaLibros libros={results} />
            </div>


        </div>
    );
}

export default SearchBooks;
