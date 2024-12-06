/* eslint-disable react/prop-types */
const Liste = ({ data, titles }) => {
  return (
    <div>
      <h1>Compte {titles} de cette semaine</h1>
      <div>
        {data.map((item, index) => {
          return (
            <div key={index} className="flex m-5 relative space-x-4">
              <div className="h-full p-1 bg-gray-400/30 rounded-full">
                <img src={item?.profile} alt="profile" className="max-h-8 rounded-full" />
              </div>
              <div className="flex flex-col w-full ">
                <div className="flex justify-between">
                  <h1 className="text-sm font-bold">{item?.name}</h1>
                  <span className="text-red-500 text-sm font-bold bg-red-200 rounded-full px-1">ban</span>
                </div>
                <p className="text-gray-400/30 text-sm ">{item?.email}</p>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Liste;
