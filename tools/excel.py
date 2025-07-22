import pandas as pd

# Load the dataset
df = pd.read_excel("training_data_100.xlsx")

# Update the 'RecommendedServer' column based on specific conditions
for i in df.index:
    match df.loc[i, 'RecommendedServer']:
        case 'IELTS Support':
            df.loc[i, 'RecommendedServer'] = 'English Hub'
            df.loc[i, 'RecommendedServerURL'] = 'https://discord.gg/enghub'
        case 'English Reading Club':
            df.loc[i, 'RecommendedServer'] = 'English'
            df.loc[i, 'RecommendedServerURL'] = 'https://discord.gg/english'
        case 'Work English':
            df.loc[i, 'RecommendedServer'] = 'The Entrepreneur Network'
            df.loc[i, 'RecommendedServerURL'] = 'https://discord.gg/the-entrepreneur-network-beta-1164702592241238178'
        case 'English Travel':
            df.loc[i, 'RecommendedServer'] = 'Travel Hub'
            df.loc[i, 'RecommendedServerURL'] = 'Placeholder'

# Save the updated dataset back to the Excel file
df.to_excel("training_data_100.xlsx")

