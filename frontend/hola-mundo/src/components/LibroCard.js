import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import axios from 'axios';

const LibroCard = ({ libro }) => {
  const handleClick = async () => {
    if ("geolocation" in navigator) {
      // La geolocalización está disponible
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          const { latitude, longitude } = position.coords;
          console.log("Latitud:", latitude);
          console.log("Longitud:", longitude);
          try {
            const url = `http://localhost:8000/bibliotecas/${libro.id}/${longitude}/${latitude}`;
            const response = await axios.get(url);
            console.log(response.data);
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
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Title>{libro.titulo}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">{libro.fecha_publicacion}</Card.Subtitle>
        <Card.Text>{libro.descripcion}</Card.Text>
        <Button variant="primary" onClick={handleClick}>Guardar Título</Button>
      </Card.Body>
    </Card>
  );
};

export default LibroCard;
