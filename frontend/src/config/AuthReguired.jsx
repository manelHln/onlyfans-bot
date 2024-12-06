import { Navigate, Outlet } from "react-router";

const AuthReguired = () => {
  //   const isLoggedIn = localStorage.getItem("token");
  const isLoggedIn = "login";

  if (!isLoggedIn) {
    return <Navigate to="/login" state />;
  } else {
    return <Outlet />;
  }
};

export default AuthReguired;
