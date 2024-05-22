import React from 'react';
import LibroCard from './LibroCard';

const ListaLibros = ({ libros }) => {
  return (
    <div className="row row-cols-md-4">
      {libros.map(libro => (
        <div key={libro.id} className="col mb-4">
          <LibroCard libro={libro} />
        </div>
      ))}
    </div>
  );
};

export default ListaLibros;
