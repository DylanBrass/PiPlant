import Navbar from "./NavigationBar";
import './HomePage.css';
import axios from 'axios'

function MainPage() {
  return (
    <div>
      <Navbar />
      <h1>Home Page</h1>
      <p>This is the home page.</p>
      <button onClick={axios
        .get(`https://localhost:5000`)
        .then(function (response) {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
      })
  
      }>Test Get</button>
    </div>
  );
}

export default MainPage;