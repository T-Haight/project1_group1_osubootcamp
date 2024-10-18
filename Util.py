import pandas as pd

def merge_with_taxi_data(df):
    """
    This function merges the given dataframe with the taxi data.
    """
    Taxi_Zone_Lookup_df = pd.read_csv("Resources/taxi_zone_lookup.csv")

    # merge the two dataframes based on pickup locations
    lyft_PU_locations_df = pd.merge(df, Taxi_Zone_Lookup_df, left_on="PULocationID", right_on="LocationID")
    
    # Rename the columns to match the schema
    lyft_PU_locations_df.rename(columns={"Borough": "Pickup_Borough", "Zone": "Pickup_Zone"}, inplace=True)

    # Drop the LocationID and service_zone columns
    lyft_PU_locations_df = lyft_PU_locations_df.drop(columns=["LocationID", "service_zone"])

    # Reorder the columns
    lyft_PU_locations_df = lyft_PU_locations_df[["pickup_datetime", "dropoff_datetime", "PULocationID", "Pickup_Borough", "Pickup_Zone", "DOLocationID", "trip_miles", "trip_time", "base_passenger_fare", "tolls", "bcf", "sales_tax", "congestion_surcharge", "airport_fee", "tips", "driver_pay", "Total_Passenger_Cost"]]

    # merge  lyft_PU_locations_df with Taxi_Zone_Lookup_df based on drop-off locations
    lyft_locations_df = pd.merge(lyft_PU_locations_df, Taxi_Zone_Lookup_df, left_on="DOLocationID", right_on="LocationID")

    # Rename the columns to match the schema
    lyft_locations_df.rename(columns={"Borough": "Dropoff_Borough", "Zone": "Dropoff_Zone"}, inplace=True)

    # Drop the LocationID and service_zone columns
    lyft_locations_df = lyft_locations_df.drop(columns=["LocationID", "service_zone"])

    # Reorder the columns
    lyft_locations_df = lyft_locations_df[["pickup_datetime", "dropoff_datetime", "PULocationID", "Pickup_Borough", "Pickup_Zone", "DOLocationID", "Dropoff_Borough", "Dropoff_Zone", "trip_miles", "trip_time", "base_passenger_fare", "tolls", "bcf", "sales_tax", "congestion_surcharge", "airport_fee", "tips", "driver_pay", "Total_Passenger_Cost"]]

    return lyft_locations_df
