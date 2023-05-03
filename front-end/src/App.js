import {Routes,Route} from 'react-router-dom';
//import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.js';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';

function App() {
  return (
      <>
      <Header />
      <Routes>
        <Route path='/' element = {<Home />}>
          
        </Route>
      </Routes>
      
      <Footer />
      </>
  );
}

export default App;
