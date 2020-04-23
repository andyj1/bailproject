var ctx = document.getElementById("mixed2-chart").getContext("2d");

// Define the data
var barTotalPopulationData = [29, 18, 11, 14, 14]; // Add data values to array
var lineExample1 = [10, 15, 14, 24, 32];
var lineExample2 = [53, 20, 21, 45, 58];

var labels = ["Tokyo", "Mumbai", "Mexico City", "Shanghai", "Sao Paulo"]; // Add labels to array
// End Defining data

// End Defining data
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Population", // Name the series
        data: barTotalPopulationData, // Specify the data values array
        backgroundColor: [
          // Specify custom colors
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
          "rgba(75, 192, 192, 0.2)",
          "rgba(153, 102, 255, 0.2)"
        ],

        borderWidth: 1 // Specify bar border width
      },
      {
        label: "ExampleLine1", // Name the series
        data: lineExample1, // Specify the data values array
        backgroundColor: "#f443368c",
        borderColor: "#f443368c",

        borderWidth: 1, // Specify bar border width
        type: "line", // Set this data to a line chart
        fill: false
      },
      {
        label: "ExampleLine2", // Name the series
        data: lineExample2, // Specify the data values array
        backgroundColor: "#2196f38c",
        borderColor: "#2196f38c",

        borderWidth: 1, // Specify bar border width
        type: "line", // Set this data to a line chart
        fill: false
      }
    ]
  },
  options: {
    responsive: true, // Instruct chart js to respond nicely.
    maintainAspectRatio: false // Add to prevent default behaviour of full-width/height
  }
});
