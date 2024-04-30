import pandas as pd

def transform_csv_data(df):
    """
    A function to transform the provided DataFrame by splitting and reorganizing columns based on certain patterns and dropping unnecessary columns.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the data to be transformed.
    
    Returns:
    pandas.DataFrame: The transformed DataFrame after performing the specified operations.
    """
    # Add your data transformation code from sup_peak.ipynb here
    df[['Date', 'timestamp']] = df['@timestamp'].str.split('@', expand=True)
    df = df[['Date', 'timestamp','message']].copy()
    df[['0', '1', '2','3','4','5','6','7','8', '9', '10','11', '12','13','14', '15', '16','17']] = df['message'].str.split(':', expand=True)
    df.drop(columns= ['message','0', '1', '2','3','6','7','8', '9', '10','11', '12','13','14', '15'], inplace=True)
    df['userSessionType'] = df['4'].str.split(',', expand=True)[0]
    df['userName'] = df['5'].str.split(',', expand=True)[0]
    df['stationType'] = df['16'].str.split(',', expand=True)[0]
    df['station'] = df['17'].str.split(',', expand=True)[0]
    df.drop(columns = ['4', '5', '16', '17'], inplace=True)
    # Add more transformation steps as needed

    return df
