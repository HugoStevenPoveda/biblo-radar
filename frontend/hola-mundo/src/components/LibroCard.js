import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

const LibroCard = ({ libro, onSelectLibrary }) => {
  const handleClick = () => {
    onSelectLibrary(libro.id);
  };

  return (
    <Card style={{ width: '18rem' }}>
      <Card.Body>
        <Card.Title>{libro.titulo}</Card.Title>
        <Card.Subtitle className="mb-2 text-muted">{libro.fecha_publicacion}</Card.Subtitle>
        <Card.Text>{libro.descripcion}</Card.Text>
        <Button variant="primary" onClick={handleClick}>Buscar Bibliotecas</Button>
      </Card.Body>
    </Card>
  );
};

export default LibroCard;
