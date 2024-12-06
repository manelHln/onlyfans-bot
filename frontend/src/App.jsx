import "./App.css";
import { Route, Routes } from "react-router";
import InsatgramBot from "./pages/instagramBot/InsatgramBot";

import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import Home from "./pages/home/Home";
import Layout from "./components/Layout/Layout";
import Twitter from "./pages/twitterBot/Twitter";
import AuthReguired from "./config/AuthReguired";
import Setting from "./pages/setting/Setting";
import Account from "./pages/setting/Account";

function App() {
  return (
    <>
      <Routes>
        <Route path="login" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route element={<AuthReguired />}>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="instagramBot" element={<InsatgramBot />} />
            <Route path="twitterBot" element={<Twitter />} />
            <Route path="account" element={<Account />} />
            <Route path="setting" element={<Setting />} />
          </Route>
        </Route>
      </Routes>
    </>
  );
}

export default App;
// loader={async ({ request }) => await requireAuth(request)}
// loader={async ({ request }) => await requireAuth(request)}
// loader={async ({ request }) => await requireAuth(request)}
// loader={async ({ request }) => await requireAuth(request)}
// loader={async ({ request }) => await requireAuth(request)}
