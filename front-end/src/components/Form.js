/* This component will be used to view, edit and create new records based on the listview or menu item clidked 
    I will build this out on the next module
*/

import {useParams} from 'react-router-dom'; // The useParams object allows the app to parse the url string from the router 


function Form(){
    
    let params = useParams();
    let url = params["*"]; // Anything after the * will be passed into the url parameter
  
   
    const base = "http://127.0.0.1:8000/api/"; // Base api url
   
    
    return (
        <div class="col-10">
            <div className="row">
                <form className="api-frame" title="test">
                
                </form> 
            </div>
        </div>
    )
};

export default Form;