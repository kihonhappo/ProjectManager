/* This component sets the API Documentation Iframe src dynamically after the user clicks a link in the API Docuentation 
section of the left side navbar. The idea is to allow a user easy access to the api demos after they have signed up to get 
their user profile and their JWT token. 
*/

import {useParams} from 'react-router-dom'; // The useParams object allows the app to parse the url string from the route


function Frame(){
    //alert(JSON.stringify(url));
   
        let params = useParams();
        let url = params["*"]; // "one/two"
  
   
    const base = "http://127.0.0.1:8000/api/";
   
    
    return (
        <div class="col-10">
            <div className="row">
                <iframe className="api-frame" title="test" src={base + url}></iframe>
            </div>
        </div>
    )
};

export default Frame;