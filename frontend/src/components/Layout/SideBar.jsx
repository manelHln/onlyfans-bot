import { NavLink } from "react-router";
import Profile from "../component/profile";

const SideBar = () => {
  const url = [
    {
      id: "1",
      link: "",
      Title: "Tableau de bord",
      icone: <icon />,
    },

    {
      id: "2",
      link: "instagramBot",
      Title: "Instagram",
      icone: <icon />,
    },
    {
      id: "3",
      link: "twitterBot",
      Title: "Twitter",
      icone: <icon />,
    },
    {
      id: "4",
      link: "account",
      Title: "Comptes",
      icone: <icon />,
    },
    {
      id: "5",
      link: "setting",
      Title: "Paramètre",
      icone: <icon />,
    },
  ];

  return (
    <div className="h-screen  p-20">
      <Profile />
      <nav className="text-gray-400">
        <ul className="flex flex-col space-y-4 text-2xl font-bold py-24">
          {url.map((item, index) => {
            return (
              <li key={index} className="text-nowrap">
                <NavLink to={item.link} className={({ isActive }) => (isActive ? "text-white" : "")} state>
                  {item.Title}
                </NavLink>
              </li>
            );
          })}
        </ul>
      </nav>
    </div>
  );
};

export default SideBar;
