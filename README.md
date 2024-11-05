# Project 1: NYC Taxi Data Analysis for Starting a RoboTaxi Company
![image](https://github.com/user-attachments/assets/085a74c0-f00d-4abe-bcdb-dcdf708a12e7?w=800&h=450)

## Overview
This project will be preforming Data Analysis and Predicting future sales of LYFT taxi service in New York City, ultimately answering the question which part of NYC has the highest sales and trips. We will be exploring the raw data to determine which data need to be spliced, grouped. The results found will be visualized to give a better understanding.

## Table of Contents
1. [Introduction](#Introduction)
2. [Assumptions](#Assumptions)
3. [Cleaning Up Data](#Cleaning-up-Data)
4. [Visualizing the Data](#Visualizing-the-Data)
5. [Conclusion](#Conclusion)

## Introduction
In New York City, all taxi vehicles are managed by TLC(Taxi and Limousine Commission) which is responsible for licensing and regulating taxi cabs (Yellow), for-hire (community-based liveries, black cars and luxury limousines), commuter vans and paratransit vehicles. This TLC will record all data for every vehicle licensed as a taxi, this data is divided into Yellow Taxi, Green Taxi, For-Hire and High Volume For-Hire (HVFH). This data includes type of vehicles, location, time, trip miles, trip time, tolls, taxes, fees etc.

## Assumptions
This Project will making the following assumptions to better understanding of the data to answer the main question.
1. From the HVFH data only looking at LYFT data for the month of Decemeber 2023 as a representative sample.
2. We will be looking at total sales without taking into account share of the company vs share of the driver.

## Cleaning Up Data
As per the assumptions made above, we will performing the following actions to get the appropriate data we will be working on 
```python
nyctaxi_lyft = nyctaxi[nyctaxi['hvfhs_license_num'] == 'HV0005']
```
After slicing the data for Lyft, then we have to create a column for airport_visit as a boolean to understand which trips are to and from airport. While we are doing this we are also doing some timeseries data to find out which day of the week these trips were made so that we can an idea of how many taxi fares each day. The code for this as follows

```python
nyctaxi_lyft.loc[:,'pickup_datetime'] = pd.to_datetime(nyctaxi_lyft['pickup_datetime'])
nyctaxi_lyft.loc[:,'day_of_week'] = nyctaxi_lyft['pickup_datetime'].dt.day_name()
```
After we findout what day these trips are made, now we have to findout at what time of day these trips are requested. For this we do the following 

```python
###Define a function to return what time of day
def time_of_day(x):
    if x in range(6,12):
        return 'Morning'
    elif x in range(12,17):
        return 'Afternoon'
    elif x in range(17,22):
        return 'Evening'
    else:
        return 'Late night'
nyctaxi_lyft['pickup_datetime'] = pd.to_datetime(nyctaxi_lyft['pickup_datetime'])
nyctaxi_lyft['dropoff_datetime'] = pd.to_datetime(nyctaxi_lyft['dropoff_datetime'])

nyctaxi_lyft['pickup_hour'] = nyctaxi_lyft['pickup_datetime'].dt.hour
nyctaxi_lyft['dropoff_hour'] = nyctaxi_lyft['dropoff_datetime'].dt.hour

nyctaxi_lyft['pickup_timeday'] = nyctaxi_lyft['pickup_hour'].apply(time_of_day)
nyctaxi_lyft['dropoff_timeday'] = nyctaxi_lyft['dropoff_hour'].apply(time_of_day)
```
Here we are answering a question: ***what time of day do we have the highest number of rides?*** This gets into a granularity of time and day to better understand the business of LYFT. This will put the robot taxi company to better position their assets for biggest ROI.
After this we are combining multiple columns that represent fare into single column called 'total_ride_cost' 

```python
nyctaxi_lyft.loc[:,'Total_Passenger_Cost'] = (
    nyctaxi_lyft['base_passenger_fare'] + 
    nyctaxi_lyft['tolls'] + 
    nyctaxi_lyft['bcf'] +
    nyctaxi_lyft['sales_tax'] +
    nyctaxi_lyft['congestion_surcharge'] +
    nyctaxi_lyft['airport_fee'] +
    nyctaxi_lyft['tips'] )
```
After performing all these above iteration we arrive at a data set we can use to perform our analysis on.

## Visualizing the Data
The best way to understand and visualize is to first find common trends in the data where we 
1. Identify shared patterns or trends among multiple economic time series
2. Extract underlying common factors that drive the behavior of various economic indicators.
3. Visualize the relationship between different economic variables and their contributions to common trends.

<p align="center">
  <img width="1000" height="450" src="https://github.com/user-attachments/assets/17ded101-360a-439a-8f71-6defb193c93e" alt="Description" width="1000">
</p>

After finding the trends we have determine which areas of NYC are frequent pickup's by travellers to get a better understanding of where we can get more trips which result in more revenue.

<p align="center">
  <img width="1000" height="450" src="https://github.com/user-attachments/assets/9dd61fe1-305b-4a50-9767-1c091b4a7400" alt="Description" width="1000">
</p>

Now we know the trends and frequent pickup location, we move onto economics of the rides, where we have to categorise the data to geographical points. Meaning since NYC is divided into Boroughs we have to find where each data points represents each borough of NYC, findout which borough has the hightest number of trips. After that we concentrate on which areas in this borough are more profitable. 

After doing the analysis in the direction mentioned above we arrive at the following graph

<p align="center">
  <img width="1000" height="450" src="https://github.com/user-attachments/assets/94e3d78d-179f-4b76-90df-85f2ad5a547d" alt="Description" width="1000">
</p>

Lets put some numbers to the picture above to better understand what we are trying to convey:
* Queens Borough is the most frequented by travellers of LYFT more than 100,000 trips.
* In the Queens, both airports ***JFK*** and ***LaGuardia*** are the most profitable pickup with Total sales of ~$7.4 M to ***JFK*** and ~$6.9 M to ***LaGuardia***
* Similarly, both airports ***JFK*** and ***LaGuardia*** are the most profitable dropoff with Total sales of ~$11 M to ***JFK*** and ~$7.8 M to ***LaGuardia***

 ## Visualizing JFK and LaGuardia Airport
 </p>
  <img  width="500" height="400" src="https://github.com/user-attachments/assets/0c4cedcd-5d7e-4950-b53a-d90c3e587e51" alt="Description" width="500">
  <img  width="500" height="400" src="https://github.com/user-attachments/assets/a75cbcdb-1395-4155-886f-945ebfc83b0e" alt="Description" width="500">
 </p>
 
Looking both Airport data side by side we can see more travellers are going outisde NYC who are pickup from JFK than compared to LaGuardia. We can clearly see that there has been a clear difference from the drop off zones depicted in these two diagrams above let's go into a couple of metrics regarding a drop off zones of JFK and drop off zones of la Guardia airport the average ride for JFK is close to 3000 per day in compared to LaGuardia is 3400 per day average trip times is 43.2 minutes compared to 34.5 minutes in la Guardia average strip miles is 17.3 miles compared to 11.1 miles and the average customer cost is $77.90 compared to $64.58.
Given the information that we have deducted from these two pie charts here we can clearly say that setting up our company at JFK would be more profitable than LaGuardia

## Making Future Predictions Using Prophet.
Here we did something different rather than using just the 2023 December data we also used 2022 December data and 2021 December data concatenated them and came up with a new data set to use it for this prediction model. As you can see from the gas graph of placed below the prediction model goes up until 20/25/01 and we can clearly see that there has been an increase in the daily number of trips in relation to the previous data. Using this prediction we can clearly say that if we establish our company around any time in next year of 2025 by the time we get to the end of 2025 we will definitely see a market share and also see an increase in overall trips from the starting point to the end of the year even though there is a slowdown during the new year time but we can still see that it's going to be profitable
<p align="center">
    <img width="1000" height="450" src="https://github.com/user-attachments/assets/8323571c-a515-40e3-9e9d-04e162b8726f" alt="Description" width="1000">
</p>

## Conclusion
New York City is a great hub for starting any taxi business with 5 million plus rides per month which has multiple tourist locations scenic locations and also multiple events all around the year it is a prime location for anyone to start a taxi company the airport locations have the highest pickup and drop off rate of any location ID in the data set weekends and late hours of the day are usually higher traffic times at the end we think JFK airport is a better first location to start our Robo taxi business taking into account the infrastructure and the charging equipment that requires and also over the time profitability that we can attain if we do the starting point as JFK airport then expand it beyond.



