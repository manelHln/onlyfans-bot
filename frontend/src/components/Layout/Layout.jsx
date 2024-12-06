import { Outlet } from "react-router";
import SideBar from "./SideBar";

const Layout = () => {
  return (
    <div className="h-full w-full bg-gray-950/90 flex backdrop-blur-sm">
      <SideBar />
      <div className=" bg-white w-full  my-5 mr-10 rounded-[30px] pt-5 px-24">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
