import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function Home({ row_1, row_2, row_3 }) {
    return (
        <Container>
            <Row>

                <Col>{row_1}</Col>
            </Row>
            <Row>
                <Col>{row_2}</Col>
                <Col>{row_3}</Col>
            </Row>
        </Container>
    );
}

export default Home;