# Covid-19 Global Dashboard

Amidst the unfortunate chaos of COVID-19 around the world, there has been an overload of information regarding the pandemic present online. With such massive amounts of data, it is crucial not only to identify and collect verified information, but to also structure it in a way that allows us to pick worthy insights. In this context, data visualization is perfect for enabling quick and accurate comprehension of information, whilst providing the relevant insights into our current global situation.

For this exact purpose, we have created a "Covid-19 Global Dashboard" that provides an interactive visualization of the current spread of COVID-19 around the world. Within this dashboard, you can find an overview of both worldwide & country specific statistics.

The dashboard is created with Streamlit using Altair, Plotly and Matplotlib for visualization and deployed using Heroku. 

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
