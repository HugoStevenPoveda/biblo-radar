import Card from 'react-bootstrap/Card';



const CardBooks = ({ libro }) => {
    return (
        <Card style={{ width: '18rem' }}>
            <Card.Body>
                <Card.Title>{libro.titulo}</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">{libro.fecha_publicacion}</Card.Subtitle>
                <Card.Text>
                    {libro.descripcion}
                </Card.Text>
                <Card.Link href="#">Card Link</Card.Link>
            </Card.Body>
        </Card>
    );




}

export default CardBooks;