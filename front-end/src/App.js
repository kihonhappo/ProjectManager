import {Routes,Route} from 'react-router-dom';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.js';
import Header from './components/Header';
import Footer from './components/Footer';
import Dash from './components/Dash';
import ListView from './components/ListView';
import Nav from './components/Nav';
import Frame from './components/Frame';
import Form from './components/Form';

function App() {

  return (
      <>
      <Header />
      
      <main className="">
        <div className="container-fluid">
          <div class="row">
        <Nav dir='vert'></Nav>
        
      <Routes>
        <Route path='/dash/*' element = {<Dash />}></Route>
        <Route path='/list/*' element = {<ListView />}></Route>
        <Route path='/frame/*' element = {<Frame  />}></Route>
        <Route path='/form/*' element = {<Form  />}></Route>
      </Routes>
      </div>
      </div>
      </main>
      <Footer />
      </>
  );
}

export default App;
