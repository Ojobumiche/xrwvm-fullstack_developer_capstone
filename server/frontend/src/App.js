
import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";
import Register from "./components/Register/register";
import Login from "./components/Login/Login";

function App() {
  return (
    <div>
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
    </Routes>
    <Register />
    <Login/>
    </div>
  
  );
}
export default App;
