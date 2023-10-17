document.addEventListener("DOMContentLoaded", function() {
    const dashboardSelect = document.getElementById("dashboard_source");
    const chartSelection = document.getElementById("chart-selection");

    dashboardSelect.addEventListener("change", function() {
        const selectedDashboard = dashboardSelect.value;
        chartSelection.innerHTML = ""; // Clear previous chart selections

        if (selectedDashboard) {
            // Assuming /get_dataset_chart_mapping endpoint returns the JSON data
            fetch("/get_dataset_chart_mapping")
                .then(response => response.json())
                .then(data => {
                    const datasetChartMapping = data[selectedDashboard];

                    if (datasetChartMapping) {
                        datasetChartMapping.charts.forEach((chart, index) => {
                            const chartLabel = document.createElement("label");
                            chartLabel.innerText = `Select Dataset for Chart ${index + 1}: ${chart}`;
                            chartSelection.appendChild(chartLabel);

                            const datasetSelect = document.createElement("select");
                            datasetSelect.name = `dataset${index}`;
                            datasetSelect.id = `dataset${index}`
                            datasetChartMapping.datasets.forEach((dataset) => {
                                const option = document.createElement("option");
                                option.value = dataset;
                                option.innerText = dataset;
                                datasetSelect.appendChild(option);
                            });

                            chartSelection.appendChild(datasetSelect);

                            // Add a text field for each chart
                            const chartTextField = document.createElement("input");
                            chartTextField.type = "text";
                            chartTextField.name = `chart${index}`;
                            chartTextField.id = `chart${index}`;
                            chartTextField.placeholder = `Chart Name for Chart ${index + 1}`;
                            chartSelection.appendChild(chartTextField);
                        });
                    }
                });
        }
    });
});
