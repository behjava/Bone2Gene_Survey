import pandas as pd
import plotly.express as px

# Sample DataFrame based on the data you provided
data = {
    'Value': [
        "Neonates and infants (0-1 year old),1 to 10 years old,10 to 18 years old,Greater than 18 years old",
        "Neonates and infants (0-1 year old),1 to 10 years old,10 to 18 years old",
        "Greater than 18 years old",
        "10 to 18 years old,Greater than 18 years old",
        "1 to 10 years old,10 to 18 years old",
        "Neonates and infants (0-1 year old),Greater than 18 years old",
        "1 to 10 years old,10 to 18 years old,Greater than 18 years old",
        "Neonates and infants (0-1 year old)",
        "10 to 18 years old"
    ],
    'Count': [50, 34, 7, 5, 4, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Split the 'Value' column into a list of age groups for each row to create hierarchical paths
df['Value'] = df['Value'].str.split(',')

# Create separate columns for each level in the hierarchy and replace missing levels with a placeholder
df['Level_1'] = df['Value'].apply(lambda x: x[0] if len(x) > 0 else None)
df['Level_2'] = df['Value'].apply(lambda x: x[1] if len(x) > 1 else '')
df['Level_3'] = df['Value'].apply(lambda x: x[2] if len(x) > 2 else '')
df['Level_4'] = df['Value'].apply(lambda x: x[3] if len(x) > 3 else '')

# Create the Treemap using Plotly Express
fig = px.treemap(df,
                 path=['Level_1', 'Level_2', 'Level_3', 'Level_4'],  # Define the hierarchical path
                 values='Count',   # Use the 'Count' column for the size of each section
                 title="Age Group Combinations in Survey Responses")

# Show the plot
fig.show()
# fig.write_image("Patients_age_group_Treemap.png", width=800, height=600, scale=6)
