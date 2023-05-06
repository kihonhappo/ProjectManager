import {useParams} from 'react-router-dom';


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