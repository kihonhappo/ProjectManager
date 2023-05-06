import {useParams} from 'react-router-dom'; // The useParams object allows the app to parse the url string from the route

function Pagination(cnt, dest){
    //alert('Pagination: ' + dest);
    let params = useParams();
    let api = params["*"];
    let br = window.location.href;
    let base_back_end = "http://127.0.0.1:8000/api/";
    let base_front_end = "http://localhost:3000/";
    br = br.split(base_front_end)[1];
    br = br.split('/')[0];


    //+ api + "/?format=json";
    let links = [];
    cnt = parseInt(cnt.cnt);

    for(let i = 1; i <= cnt; i++){
       links.push(<li className="page-item"><a className="page-link" href="#">{i}</a></li>);
    }
    return (

            <nav aria-label="Page navigation example">
                <ul className="pagination">
                    {links}
                </ul>
            </nav>
    )
};

export default Pagination;