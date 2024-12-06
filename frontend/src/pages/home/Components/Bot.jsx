import { Bot1 } from "../../../assets/Bot (1).png";
import { Bot2 } from "../../../assets/Bot (2).png";
const Bot = ({ title, data }) => {
  return (
    <div className="bg-gray-400/20 rounded-[xl] ">
      <div>
        <img src={title === "Twitter" ? Bot1 : Bot2} />
      </div>
      <h1>
        {title} Bot pour vous aider a ramener du trafique sur vos compte {title}
      </h1>
      <div>
        <button className="">Lancer le bot</button>
      </div>
    </div>
  );
};

export default Bot;
