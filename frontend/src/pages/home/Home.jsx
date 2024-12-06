import { InstaCompte } from "../../Models/AccountData";
import MyChart from "./Components/Chart";
import Liste from "./Components/Liste";

const Home = () => {
  return (
    <div className="flex">
      <div className="flex flex-col space-y-4 w-full">
        <h1 className="text-4xl font-bold">Recap</h1>
        <div className="w-full h-[300px] ">
          <MyChart />
        </div>
        <div>
          <Liste titles={"Instagram"} data={InstaCompte} />
        </div>
        <div>
          <Liste titles={"Twitter"} data={InstaCompte} />
        </div>
      </div>
    </div>
  );
};

export default Home;
