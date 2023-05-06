/* This component is used to create the left side navbar. The component makes a fetch call to the api root and recieves a list 
    of all the api endpoints. The component then loops through the list of endpoints and injects the endpoint into the nav links.
*/

import {useState,useEffect} from 'react';
import {useParams} from 'react-router-dom'; // The useParams object allows the app to parse the url string from the route



function Nav({dir}){
    // The useState is used for state management, it handles the callbacks for await and async functions like fetch.
    const [items,setItems]=useState([]); 
    const url = "http://127.0.0.1:8000/api/";
    let params = useParams();
    let api = params["*"];
    let br = window.location.href;
    const base_back_end = "http://127.0.0.1:8000/api/";
    const base_front_end = "http://localhost:3000/";
    br = br.split(base_front_end)[1];
    const nav_item = br.split('/')[0];
    

    useEffect(() => {
        fetchData();
    },[]);

    function capFirst(word){ // this function capitalizes the first character of a word
       return word.charAt(0).toUpperCase() + word.slice(1);
    }

    function fetchData(){
        fetch(url)
        .then((response) => response.json())
        .then((data) => {
           /* The api list is returned by the server an object and each endpoint is a property of the object and not an array.
              the converted object takes the api object and turns it into an array of endpoint objects so I can iterate it easier */
           let converted = Object.keys(data)
                   .map(key => ({title: key, url: data[key]}));
              setItems(converted); //
        });
    }
    return (
        <div className="flex-shrink-0 p-3 col-md-2">
          
    <a href="/dash/" className="d-flex align-items-center pb-3 mb-3 link-body-emphasis text-decoration-none border-bottom">
     
      <span className="fs-5 fw-semibold">Collapsible</span>
    </a>
    <ul class="nav flex-column">
      <li class="nav-item">
          <button className="btn btn-toggle rounded collapsed" data-bs-toggle="collapse" data-bs-target="#dashboard-btn" aria-expanded="false">
            Dashboard
          </button>
        <div className="collapse" id="dashboard-btn"> {/* This section will show the different Management Boards right now they just list projects */}
          <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li><a href="/dash/lifecycle" className="link-dark rounded active">LifeCycle Board</a></li>
            <li><a href="/dash/kanban" className="link-dark rounded">Kanban</a></li>
            <li><a href="/dash/scrum" className="link-dark rounded">Scrum Board</a></li>
          </ul>
        </div>
      </li>
      <li class="border-top my-3"></li>
      <li class="nav-item">
          <button className="btn btn-toggle rounded collapsed" data-bs-toggle="collapse" data-bs-target="#list-btn" aria-expanded="false">
            ListViews
          </button>
        <div className="collapse" id="list-btn">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">{/* This section will loops throught the api endpoints and creates the hyperlink for the listviews
              that corresponds with each python-django data model and db table*/}

              {
                items.map((item) =>          
                  <li>
                    <a data-page={item.title} className="link-dark rounded" href={"/list/" + item.title}>{capFirst(item.title) + ' List View'}</a>
                  </li>
                )
              }
            </ul>
        </div>
      </li>
      <li class="border-top my-3"></li>
      <li class="nav-item">
          <button className="btn btn-toggle rounded collapsed" data-bs-toggle="collapse" data-bs-target="#api-btn" aria-expanded="false">
            API Documentation   {/* This section will loops throught the api endpoints and creates the src attribute for the iframe component
              that corresponds with each python-django data model and db table. Next steps will add a new + link to create a new record.*/}
          </button>
          <div className="collapse" id="api-btn">
            <ul className="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li>
                <a className="dropdown-item" href="/frame/">API List</a>
              </li>
                {
                items.map((item) => 
                  <li className="nav-item">
                    <a data-page={item.title} className="link-dark rounded" href={"/frame/" + item.title}>{capFirst(item.title)}</a>
                  </li>
                  )
                }
            </ul>
        </div>
        <li class="border-top my-3"></li>
        <li class="mb-1">
          <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
            Account  {/* This section will be used for user management. Login, logout, profile, user settings or preferences, registration. API key management. Next steps*/}
          </button>
          <div class="collapse" id="account-collapse">
            <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
              <li><a href="#" class="link-dark rounded">New...</a></li>
              <li><a href="#" class="link-dark rounded">Profile</a></li>
              <li><a href="#" class="link-dark rounded">Settings</a></li>
              <li><a href="#" class="link-dark rounded">Sign out</a></li>
            </ul>
          </div>
        </li>
      </li>         
      <li class="border-top my-3"></li>
      </ul>
  </div>
    )
};

export default Nav;