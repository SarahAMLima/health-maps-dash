# Interactive Health Maps for RMPA

This repository contains a **Dash-based application** for visualizing health-related geospatial data in the **Porto Alegre Metropolitan Region (RMPA)**. The project combines choropleth maps and histograms to provide interactive insights into the distribution of healthcare facilities, such as **UBS (Primary Healthcare Units)**, **hospitals**, and **CAPS (Psychosocial Care Centers)**.

## Features

- **Choropleth Map**: Displays spatial distributions of selected healthcare facilities across RMPA.
- **Interactive Dropdown**: Easily switch between different variables to analyze (e.g., UBS, hospitals, CAPS).
- **Histogram**: Offers additional insights into the distribution of the selected variable.
- **Responsive Design**: Side-by-side visualizations for comparative analysis.

## Libraries Used

- **Dash**: For creating the interactive web application.
- **GeoPandas**: For handling and transforming geospatial data.
- **Plotly Express**: For generating maps and histograms.

## Setup and Usage

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/dash-choropleth-health-rmpa.git
   cd dash-choropleth-health-rmpa](https://github.com/SarahAMLima/health-maps-dash/new/main?filename=README.md)

2. Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:8050/ to interact with the app.

3. Data Source
The geospatial data (saude_rmpa.geojson) includes information on healthcare facilities in the Porto Alegre Metropolitan Region. It is read and processed using GeoPandas.

![choropleth](https://github.com/user-attachments/assets/f121746d-b757-426a-a55a-ea3e9f54c622)

4. Future Enhancements
Add more datasets and variables for deeper insights.
Include time-series data for tracking changes over time.
Implement additional interactive features, such as tooltips and advanced filtering.

5. Contributing
Feel free to fork this repository and contribute! Open a pull request with your changes.
