# Covid-19 Global Dashboard
Covid-19 Global Dashboard provides an interactive visualization of the current spread of COVID-19 around the world. You can find an overview of both worldwide & country specific statistics. 

The app is deployed using Heroku and is created with streamlit using altair, plotly and matplotlib for visualization. 

The sources of the data used for this app are:
1. [covid.ourworldindata.org](https://ourworldindata.org/coronavirus)
2. [api.covid19india.org](https://api.covid19india.org)
3. [https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv)

Contributors: Niegil, Praneetha and Sakthisree.

Link to access the app: [Covid_app](https://guarded-island-68370.herokuapp.com/).

In order to run the app locally:
1. Install streamlit: pip install streamlit
2. Clone the repository: git clone https://github.com/Niegil-Francis/Covid_App.git
3. Install the required packages present in requirements.txt
4. Change the directory to Covid_App and run: streamlit run Covid_dash.py 
