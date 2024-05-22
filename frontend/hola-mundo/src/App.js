
import './App.css';


import MapView from './components/MapView';
import SearchBooks from './components/SearchBooks';
import Container from 'react-bootstrap/Container';

const App = () => (

  <Container className="p-3">

    <h1 className="header">Bienvenido biblioteca radar.</h1>
    <SearchBooks />
    <MapView />

  </Container>
);


export default App;
