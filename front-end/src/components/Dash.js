import logo from '../logo.svg';
import {useState,useEffect} from 'react';

function Dash(){

  const [items,setItems]=useState([]);
    const url = "http://127.0.0.1:8000/api/project/";

    useEffect(() => {
        fetchData();
    },[]);

    function fetchData(){
      fetch(url)
      .then((response) => response.json())
      .then((data) => {
         //alert("data: " + JSON.stringify(data));
         setItems(data.data);
      });
    }

  return (
      <div class="col-10">
        <div className="row">
          {
             items.map((item) =>
                <div className="card col-12 col-md-3 mb-2">
                  <img src={logo} className="card-img-top" alt="..." />
                  <div className="card-body">
                    <h5 className="card-title">{item.Title}</h5>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="/" className="btn btn-primary">Go somewhere</a>
                  </div>
                </div>
             )
          }
          
        </div>
      </div>
    )
};

export default Dash;