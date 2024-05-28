import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';
import L from 'leaflet';
import axios from 'axios';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

// Importar los archivos de iconos locales
import blueMarkerIcon from '../assets/images/blue-marker-icon.png';
import redMarkerIcon from '../assets/images/red-marker-icon.png';

// Definir iconos personalizados
const blueIcon = new L.Icon({
  iconUrl: blueMarkerIcon,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
  shadowSize: [41, 41],
});

const redIcon = new L.Icon({
  iconUrl: redMarkerIcon,
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
  shadowSize: [41, 41],
});

const MapView = ({ libraries = [], userLatitud = 4.666198, userLongitud = -74.074892 }) => {
  const [defaultPosition, setDefaultPosition] = useState([userLatitud, userLongitud]);
  const [route, setRoute] = useState([]);
  const [positionObtained, setPositionObtained] = useState(false);
  const [libraryInfo, setLibraryInfo] = useState(null);

  useEffect(() => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition((position) => {
        const newPosition = [position.coords.latitude, position.coords.longitude];
        setDefaultPosition(newPosition);
        setPositionObtained(true);
      });
    }
  }, []);


  const handleClick = async (library_id) => {
    console.log("!!!!!!!!!!!!!!!!!!!!!!");
    console.log(library_id);




    try {
      const path = `http://localhost:7000/movies?query=bandits&index_name=vector-search-tutorial`
      const response = await axios.get(path);
      console.log(response)
      setLibraryInfo(response.data);






    } catch (error) {
      console.error('Error al obtener la información de la biblioteca:', error);
    }

  };






  const getRoute = async (start, end) => {
    const apiKey = '5b3ce3597851110001cf6248025237e292724238a88897c43b50327c'; // Reemplaza con tu clave de OpenRouteService
    // const apiKey = '5aaaaaaaa'; // Reemplaza con tu clave de OpenRouteService
    const url = `https://api.openrouteservice.org/v2/directions/driving-car?api_key=${apiKey}&start=${start}&end=${end}`;



    try {
      const response = await axios.get(url);

      const coordinates = response.data.features[0].geometry.coordinates;
      const routePoints = coordinates.map(coord => [coord[1], coord[0]]);
      setRoute(routePoints);
    } catch (error) {
      console.error('Error fetching route:', error);
    }
  };

  useEffect(() => {
    if (defaultPosition && libraries.length > 0) {
      const nearestLibrary = libraries[0];
      const start = `${defaultPosition[1]},${defaultPosition[0]}`; // Longitud, Latitud
      const end = `${nearestLibrary.longitud},${nearestLibrary.latitud}`; // Longitud, Latitud
      getRoute(start, end);
    }
  }, [defaultPosition, libraries]);

  return (

    <div>
      {positionObtained && (

        <MapContainer center={defaultPosition} zoom={13} style={{ height: '100vh', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          />

          <Marker position={defaultPosition} icon={blueIcon}>
            <Popup>Tu posición actual</Popup>
          </Marker>
          {libraries.map(library => (


            <Marker
              position={[parseFloat(library.latitud), parseFloat(library.longitud)]}
              icon={redIcon}
            >
              {
                <Popup >
                  <Card>
                    <Card.Body>
                      <Card.Title>{library.nombre}</Card.Title>
                      <Card.Text>
                        Distancia: {library.distancia.toFixed(2)} metros
                      </Card.Text>
                      <Card.Text  className="text-center font-weight-bold" >
                       Movies similares al libro 
                      </Card.Text>
                      {libraryInfo && (
                          <div>
                          {libraryInfo.map(movie => (
                            <div key={movie.title}>
                              <p>Título: {movie.title}</p>
                              <p>Año: {movie.year}</p>
                              <p>Argumento: {movie.plot}</p>
                              <hr />
                            </div>
                          ))}
                        </div>
                      )}



                      <Button variant="primary" onClick={() => handleClick(library.nombre)}>Más información</Button>

                    </Card.Body>
                  </Card>
                </Popup>
              }
            </Marker>
          ))}
          {route.length > 0 && <Polyline positions={route} color="blue" />}
        </MapContainer>

      )}

    </div>



  );
};

export default MapView;
