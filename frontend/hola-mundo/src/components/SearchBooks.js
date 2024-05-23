import React, { useState } from 'react';
import axios from 'axios';
import ListaLibros from './ListaLibros';
import MapView from './MapView';
import Header from './Header';
import ListAccordion from './ListAccordion';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function SearchBooks() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [libraries, setLibraries] = useState([]);




    const handleSearch = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await axios.get(`http://localhost:8000/libro/${query}`);
            setResults(response.data);
        } catch (err) {
            setError('Error fetching data. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const handleSelectLibrary = async (libroId) => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                async (position) => {
                    const { latitude, longitude } = position.coords;
                    try {
                        const url = `http://localhost:8000/bibliotecas/${libroId}/${longitude}/${latitude}`;
                        const response = await axios.get(url);
                         setLibraries(response.data);
                        
                    } catch (err) {
                        console.error("Error en la petición:", err);
                    }
                },
                (error) => {
                    console.error("Error al obtener la geolocalización:", error);
                }
            );
        } else {
            console.log("La geolocalización no está disponible en este dispositivo.");
        }
    };

    return (
      
            <Container>
                <Row>
                    <Col>
                        <Header />
                    </Col>

                </Row>
                <Row>
                    <Col>

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


                        <ListAccordion libros={results} onSelectLibrary={handleSelectLibrary} />

                    </Col>

                    <Col>

                        <MapView libraries={libraries} />
                    </Col>
                </Row>
            </Container>






      
    );
}

export default SearchBooks;
