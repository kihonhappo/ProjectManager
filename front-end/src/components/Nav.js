import {useState,useEffect} from 'react';

function Nav({dir}){
    //alert(dir);
    const [items,setItems]=useState([]);
    const url = "http://127.0.0.1:8000/api/";

    useEffect(() => {
        fetchData();
    },[]);

    function capFirst(word){
       return word.charAt(0).toUpperCase() + word.slice(1);
    }

    function fetchData(){
        fetch(url)
        .then((response) => response.json())
        .then((data) => {
           //alert("data: " + JSON.stringify(data));
           let converted = Object.keys(data)
                   .map(key => ({title: key, url: data[key]}));
              setItems(converted);
        });
    }
    return (
        <div class="flex-shrink-0 p-3 col-md-2">
    <a href="/dash/" class="d-flex align-items-center pb-3 mb-3 link-body-emphasis text-decoration-none border-bottom">
     
      <span class="fs-5 fw-semibold">Collapsible</span>
    </a>
    <ul class="list-unstyled ps-0">
      <li class="mb-1">
        <button class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse" aria-expanded="false">
          Dashboard
        </button>
        <div class="collapse" id="dashboard-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
            <li><a href="/dash/lifecycle" class="link-body-emphasis d-inline-flex text-decoration-none rounded">LifeCycle Board</a></li>
            <li><a href="/dash/kanban" class="link-body-emphasis d-inline-flex text-decoration-none rounded">Kanban</a></li>
            <li><a href="/dash/scrum" class="link-body-emphasis d-inline-flex text-decoration-none rounded">Scrum Board</a></li>
          </ul>
        </div>
      </li>
      <li class="border-top my-3"></li>
      <li class="mb-1">
        <button class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed" data-bs-toggle="collapse" data-bs-target="#list-collapse" aria-expanded="false">
        ListViews
        </button>
        <div class="collapse" id="list-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
          <li className="nav-item">
            
          </li>
            {
              items.map((item) => 
                <li className="nav-item">
                  <a data-page={item.title} className="link-dark d-inline-flex text-decoration-none rounded" href={"/list/" + item.title}>{capFirst(item.title) + ' List View'}</a>
                </li>
              )
            }
          </ul>
        </div>
      </li>
      <li class="border-top my-3"></li>
      <li class="mb-1">
        <button class="btn btn-toggle d-inline-flex align-items-center rounded border-0 collapsed" data-bs-toggle="collapse" data-bs-target="#api-collapse" aria-expanded="false">
        API Documentation
        </button>
        <div class="collapse" id="api-collapse">
          <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
          <li className="nav-item">
            <a className="link-dark d-inline-flex text-decoration-none rounded" href="/frame/">API List</a>
          </li>
            {
                    items.map((item) => <li className="nav-item">
                        <a data-page={item.title} className="link-dark d-inline-flex text-decoration-none rounded" href={"/frame/" + item.title}>{capFirst(item.title)}</a>
                        </li>)
                }
          </ul>
        </div>
      </li>
    </ul>

  </div>
     
            
        
        
    )
};

export default Nav;