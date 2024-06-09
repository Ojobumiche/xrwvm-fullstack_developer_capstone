
import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div>
    <Routes>
    <Route path="/login" element={<LoginPanel />} />
    </Routes>
   
    </div>
  
  );
}
export default App;
