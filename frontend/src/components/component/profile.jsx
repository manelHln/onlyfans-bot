import profil from "../../assets/LOTO 2 - Copie.jpg";

const Profile = () => {
  return (
    <div className="flex flex-col space-y-4">
      <div className="h-20 rounded-xl font-semibold">
        <img src={profil} alt="Profile Image" className="h-20 rounded-xl " />
      </div>
      <h1 className="text-3xl text-white font-bold ">Tajj Bot </h1>
      <p className="text-gray-400 text-md">Tajj@gmail.com</p>
    </div>
  );
};

export default Profile;
