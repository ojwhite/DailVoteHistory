# Dáil Data Download

Using the Oireachtas API at https://api.oireachtas.ie/:
1. Query the API using date range parameters
2. Traverse the JSON tree and append some key information to pandas dataframe
3. Output the file as .csv (UTF-8)

Currently only set up to extract **Divisions** and **Members**