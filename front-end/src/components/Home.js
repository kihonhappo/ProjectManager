import logo from '../logo.svg';

function Home(){
    return (
        <main className="4">
        <div className="container">
          <div className="row">
            <div className="card col-12 col-md-3 mb-2">
              <img src={logo} className="card-img-top" alt="..." />
              <div className="card-body">
                <h5 className="card-title">Card title</h5>
                <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="/" className="btn btn-primary">Go somewhere</a>
              </div>
            </div>
          </div>
        </div>
      </main>
    )
};

export default Home;