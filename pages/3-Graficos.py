import streamlit as st
import pandas as pd 
import requests

# API URL
url = "https://api-colombia.com/api/v1/President"

# Get response
response = requests.get(url)

# Check status code
if response.status_code == 200:

    # Get data
    data = response.json()
    
    # Create list of dicts from data 
    presidents = [{
        "name": d["name"],
        "lastName": d["lastName"],
        "startPeriodDate": d["startPeriodDate"],
        "endPeriodDate": d["endPeriodDate"],  
    } for d in data]
    
    # Create DataFrame 
    df = pd.DataFrame(presidents)
    df    
    
else:
    st.error("Ocurrió un error")
