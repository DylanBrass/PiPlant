import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios'
const testGet = () =>{
  axios
        .get(`http://127.0.0.1:5000`)
        .then(function (response) {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
      })
}


function MainPage() {
  return (
    <div>
      <Navbar />
      <h1>Home Page</h1>
      <p>This is the home page.</p>
      <button onClick={()=> testGet()}>Test Get</button>
    </div>
  );
}

export default MainPage;