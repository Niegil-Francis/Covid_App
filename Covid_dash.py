
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



# Covid 19 Global Dashboard title formatting with markdown
st.markdown(
'''
    <link rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Suez+One">

    <div style="font-family: 'Suez One';font-size:70px; background-color:white; color:black"><center>Covid-19 Global Dashboard</center></div>
''',unsafe_allow_html=True
)

st.header(" ")


# Reading the world data from covid.ourworldindata.org
# The data is cumulative, so the total_cases for a day sums up the cases per day  
df1= pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")


#Getting the unique dates present in the dataset
dates=list(set(df1.date))
#Sorting the dates to get the most recent date
#If we use datetime to get the current day, at 12am there will be no data to show as the data for the day would not be updated yet
dates.sort()
dt_tday=dates[-1]

#Getting the data for the most recent date 
td = df1[df1['date'] ==  dt_tday]

#Resetting the index
td=td.reset_index(drop=True)

#This the text used for the hover data, anything to be added to it should be done here
#Add a '<br>' after each name and data to move to the next line
txt= ' Country: ' + td['location'].astype(str) + '<br>' + ' Cases: ' + td['total_cases'].astype(str) + '<br>'+ ' Deaths: ' + td['total_deaths'].astype(str)  

#The country names are converted to lowercase for compatibility with the inbuilt location names in graph_object plotting
td['location']=td['location'].str.lower()

#Saving the world data from the dataset 
world= td[td['location']=='world']

#Removing the world data from the dataset
td=td[td['location']!='world']


#This is to plot the global map
fig1 = go.Figure(data=go.Choropleth(
    locations = td['location'],
    locationmode='country names',
    z = td['total_cases'],   #Colour of the countries are based on this value
    colorbar_title = "Total Cases",
    text = txt, #Hoverdata 
    colorbar = {'len':0.75,'lenmode':'fraction'},
    marker_line_color='black',
    marker_line_width=0.5))


fig1.update_layout(
    title={                           #This is to set the size and location of the title of the map 
        'text':'Global Covid Data',
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    'font':{ 'color':'Black', 'size':50}},
    geo=dict(                         #Removing the frame borders and giving the projection type
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ))


st.plotly_chart(fig1)

#Printing out the statistics of the world for the most recent date
st.header("World Statistics")
c=world['total_cases'].iloc[0]
d=world['total_deaths'].iloc[0]

st.write("Confirmed Cases:",c)
st.write("Confirmed Deaths:",d)
    
st.write("Fatality Rate:",round((d/c)*100,2),'%')

#Getting a list of all the unique contries present after removing 'World'
countries=list(set(df1.location))
countries.remove('World')
countries.sort()
#The dropdown for selecting the country 
option1 = st.selectbox("Country",countries)


#Checking if there is a country selected and if there is, give its information
if( len(option1) != 0):
    
    #This is to pull out the day and total cases for the selected country 
    day_data={}
    temp=df1[df1['location']==option1]
    day_data[f'{option1} date']=temp['date']
    day_data[f'{option1} cases']=temp[['total_cases']].diff(axis=0).fillna(0).astype(int)
    day_data[f'{option1} deaths']=temp[['total_deaths']].diff(axis=0).fillna(0).astype(int)
    
    #Plot used for the Univ.ai Covid dashboard question
    fig = plt.figure(figsize = (8,6))
    ax = fig.add_subplot(211)
    ef=pd.DataFrame()
    
    ef['date']=day_data[f'{option1} date'].astype('datetime64[ns]')
    ef['cases']=day_data[f'{option1} cases']
    

    ax.bar(ef.date,ef.cases,color = '#007acc',alpha=0.3)
    ax.plot(ef.date,ef.cases,marker='o',color='#007acc')
    
    #ax.text(0.01,1,f'{option1} daily case count',transform = ax.transAxes, fontsize = 23);
    ax.set_title(f'{option1} daily case count',fontsize=23)
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
    ax.tick_params(rotation=60)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    
    ax1 = fig.add_subplot(212)
    ef['deaths']=day_data[f'{option1} deaths']
    

    ax1.bar(ef.date,ef.deaths,color = '#007acc',alpha=0.3)
    ax1.plot(ef.date,ef.deaths,marker='o',color='#007acc')
    
    ax1.set_title(f'{option1} daily death count',fontsize=23)
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
    ax1.tick_params(rotation=60)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    fig.tight_layout()
    st.plotly_chart(fig)
    
    # Printing out information for the country for the most recent date
    c=td[td['location']==option1.lower()]['total_cases'].iloc[0]
    d=td[td['location']==option1.lower()]['total_deaths'].iloc[0]
    st.write("Confirmed Cases:",c)
    st.write("Confirmed Deaths:",d)
    
    st.write("Fatality Rate:",round((d/c)*100,2),'%')


#Repeating the same for India 
st.title('Covid Analysis for India')

#Reading the data from covid19india.org
data=pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")

#The data contains an unassigned state which is removed
df = data[data['State'] != 'State Unassigned']

#Removing unnecessary columns
df=df[['Date','State','Confirmed','Recovered','Deceased']]

#Renaming the columns since the hover data is based on the column names
df.columns=['Date','State','Confirmed Cases','Recovered','Deceased']

#Getting a list of all dates
dates=list(set(df.Date))
dates.sort()

#Getting a list of all States
states=list(set(df.State))

#Findingtodays date
dt_tday=dates[-1]
#Finding yesterdays date
dt_yday=dates[-2]


#Getting todays data for all states available
dfc=df[df['Date']==dt_tday]

#This is done for compatibility of state names with the geojson 
dfc=dfc.replace("Andaman and Nicobar Islands",'Andaman & Nicobar')

#Saving the data for India
India=dfc[dfc['State'] == 'India']

#Removing India's data from the dataset 
dfc = dfc[dfc['State'] != 'India']

#Link to the geojson
gj="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
fig2 = px.choropleth(
    dfc,
    geojson=gj,
    featureidkey='properties.ST_NM',
    locations='State',
    color='Confirmed Cases',
    color_continuous_scale="Blues",
    projection="mercator",
    hover_data=['State','Confirmed Cases','Deceased','Recovered'] #The data is pulled out from the dataframe dfc in this case
)
fig2.update_geos(fitbounds="locations", visible=False)
fig2.update_layout(
    autosize=False,
    width=700,    #Here I am able to change the height and width of the graph unlike before
    height=700,
    title={
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
    'font':{ 'color':'blue', 'size':40}}
)
st.plotly_chart(fig2)

#Printing out India's stats 
st.header("India Statistics")
c=India['Confirmed Cases'].iloc[0]
d=India['Deceased'].iloc[0]
r=India['Recovered'].iloc[0]
st.write("Confirmed Cases:",c)
st.write("Confirmed Deaths:",d)
st.write("Recovered:",r)
st.write("Current Cases:",c-d-r)

st.write("Fatality Rate:",round((d/c)*100,2),'%')
st.write("Recovery Rate:",round((r/c)*100,2),'%')


#Removing India from the list of states
states.remove('India')
states.sort()
option = st.selectbox("State", states)


#Giving the information for each state similar to info for each country
if( len(option) != 0):
    day_data={}
    temp=df[df['State']==option]
    day_data[f'{option} date']=temp['Date']
    day_data[f'{option} cases']=temp[['Confirmed Cases']].diff(axis=0).fillna(0).astype(int)
    day_data[f'{option} recovered']=temp[['Recovered']].diff(axis=0).fillna(0).astype(int)
    day_data[f'{option} deaths']=temp[['Deceased']].diff(axis=0).fillna(0).astype(int)
    
    fig = plt.figure(figsize = (8,9))
    ax = fig.add_subplot(311)
    ef=pd.DataFrame()
    
    ef['date']=day_data[f'{option} date'].astype('datetime64[ns]')
    ef['cases']=day_data[f'{option} cases']
    

    ax.bar(ef.date,ef.cases,color = '#007acc',alpha=0.3)
    ax.plot(ef.date,ef.cases,marker='o',color='#007acc')
    
    ax.set_title(f'{option} daily case count', fontsize = 23);
    ax.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
    ax.tick_params(rotation=60)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    
    
    ax1 = fig.add_subplot(312)
    ef['deaths']=day_data[f'{option} deaths']

    ax1.bar(ef.date,ef.deaths,color = '#007acc',alpha=0.3)
    ax1.plot(ef.date,ef.deaths,marker='o',color='#007acc')
    
    ax1.set_title(f'{option} daily death count',fontsize=23)
    ax1.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
    ax1.tick_params(rotation=60)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    
    
    ax2 = fig.add_subplot(313)
    ef['recovered']=day_data[f'{option} recovered']
    
    ax2.bar(ef.date,ef.recovered,color = '#007acc',alpha=0.3)
    ax2.plot(ef.date,ef.recovered,marker='o',color='#007acc')
    
    ax2.set_title(f'{option} daily recovery count',fontsize=23)
    ax2.xaxis.set_major_locator(mdates.WeekdayLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b%d'))
    ax2.tick_params(rotation=60)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    
    
    fig.tight_layout()
    st.plotly_chart(fig)
    
    dfc=dfc.replace("Andaman & Nicobar",'Andaman and Nicobar Islands')
    
    c=dfc[dfc['State']==option]['Confirmed Cases'].iloc[0]
    d=dfc[dfc['State']==option]['Deceased'].iloc[0]
    r=dfc[dfc['State']==option]['Recovered'].iloc[0]
    st.write("Confirmed Cases:",c)
    st.write("Confirmed Deaths:",d)
    st.write("Recovered:",r)
    st.write("Current Cases:",c-d-r)
    
    st.write("Fatality Rate:",round((d/c)*100,2),'%')
    st.write("Recovery Rate:",round((r/c)*100,2),'%')

    



