import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

// Enregistrement des composants nécessaires
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);
const MyChart = () => {
  // Data for the chart
  const data = {
    labels: ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""], // X-axis labels
    datasets: [
      {
        label: "",
        data: [10, 10, 15, 8, 12, 20, 18, 10, 15, 8, 12, 20, 18, 15, 8, 12, 20, 18], // Data points
        borderColor: "rgba(75, 192, 192)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        tension: 0.4,
      },
    ],
  };

  // Chart options
  const options = {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: "Messages par mois",
      },
    },
  };

  return <Bar data={data} options={options} />;
};

export default MyChart;
