import {useParams} from 'react-router-dom';
import {useState,useEffect} from 'react';
import Pagination from './Pagination';

function ListView(){
    const [items,setItems]=useState([]);
    const [headers,setHeaders]=useState([]);
    const [totalResult,setTotalResults] = useState();
    let params = useParams();
    let api = params["*"];
    let url = "http://127.0.0.1:8000/api/" + api + "/?format=json";
    


    useEffect(() => {
        fetchData();
    });

    //let headers = Object.keys(items)

    function capFirst(word){
        return word.charAt(0).toUpperCase() + word.slice(1);
     }

     function lower(word){
        return word.toLowerCase();
     }
    
    function fetchData(){
        fetch(url)
        .then((response) => response.json())
        .then((data) => {
           // alert("data: " + JSON.stringify(data));
            setItems(data.data);
            setTotalResults(data.count);
            setHeaders(data.data[0]);
        });
    }
    return (
        
        <div className="col-md-10">
            <div class="table-responsive">
                <h3 className="text-align-center">{capFirst(api)} </h3>
                <table class="table table-striped table-sm">
                    <thead>
                        <tr>
                        <th>
                            <div className="btn-group btn-group-sm" role="group" aria-label="Basic example">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"/>
                                    <label class="form-check-label" for="flexCheckDefault"></label>
                                </div>
                                <button type="button" className="btn btn-default"><i className="fa fa-plus green"></i></button>
                                <button type="button" className="btn btn-default"><i className="fa fa-copy blue"></i></button>
                                <button type="button" className="btn btn-default"><i className="fa fa-trash red"></i></button>
                            </div>
                        </th>
                        {
                            Object.keys(headers).map((key, index) => 
                            index > 0 &&
                            <th scope="col">
                                {key}
                            </th>)
                        }
                        
                        </tr>
                    </thead>
                    <tbody>
                        
                        {
                            items.map((item) => 
                            <tr className="nav-item">                                
                                {
                                    Object.keys(item).map((key, index) => 
                                        index === 0 ?
                                            <td>
                                                <div className="btn-group btn-group-sm" role="group" aria-label="Basic example">
                                                    <div class="form-check">
                                                        <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"/>
                                                        <label class="form-check-label" for="flexCheckDefault"></label>
                                                    </div>
                                                    <button type="button" className="btn btn-default"><i className="fa fa-pencil green"></i></button>
                                                    <button type="button" className="btn btn-default"><i className="fa fa-copy blue"></i></button>
                                                    <button type="button" className="btn btn-default"><i className="fa fa-trash red"></i></button>
                                                </div>
                                            </td>
                                            :
                                            <td>
                                                {
                                                    typeof item[key] === 'object' &&
                                                    !Array.isArray(item[key]) &&
                                                    item[key] !== null ? <span>
                                                            <a href={"/list/" + lower(key)}>{item[key]['Title']}</a> 
                                                        </span>
                                                    :
                                                    item[key]
                                                    
                                                }
                                            </td>
                                        
                                    )
                                }
                            </tr>)
                        }
                    </tbody>
                </table>
                <Pagination />
            </div>
        </div>
       
    )
};

export default ListView;