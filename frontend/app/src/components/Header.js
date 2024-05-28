import '../App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Library from '../assets/images/library.svg'

function Header() {
  return (

    <Navbar className="navbar bg-body-tertiary"  style={{ height: '65px' }}>
    <Container>
      <Navbar.Brand className="mx-auto">
        <h1>Radar Bibliotecas</h1>
      </Navbar.Brand>
      <Navbar.Toggle />
      <Navbar.Collapse className="justify-content-end">
        <Navbar.Text>
         
          <img src={Library} alt="Icono de libro" className="img-fluid" style={{ height: '50px' }}  />
        </Navbar.Text>
      </Navbar.Collapse>
    </Container>
  </Navbar>
  


  );
}

export default Header;