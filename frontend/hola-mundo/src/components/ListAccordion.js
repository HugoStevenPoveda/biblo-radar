import React from 'react';
import Accordion from 'react-bootstrap/Accordion';
import Button from 'react-bootstrap/Button';

const ListAccordion = ({ libros, onSelectLibrary }) => {
  const handleSelect = (libroId) => {
    onSelectLibrary(libroId);
  };

  return (
    <Accordion defaultActiveKey="0">
      {libros.map((libro, index) => (
        <Accordion.Item eventKey={index.toString()} key={libro.id}>
          <Accordion.Header>{libro.titulo}</Accordion.Header>
          <Accordion.Body>
            <p><strong>Autor:</strong> {libro.autor}</p>
            <p><strong>Fecha de Publicación:</strong> {libro.fecha_publicacion}</p>
            <p>{libro.descripcion}</p>
            <Button variant="primary" onClick={() => handleSelect(libro.id)}>Buscar Bibliotecas</Button>
          </Accordion.Body>
        </Accordion.Item>
      ))}
    </Accordion>
  );
};

export default ListAccordion;
