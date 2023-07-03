import pandas as pd

def clean(filepath, filename):
	filepathtotal = filepath + filename
	df = pd.read_csv(filepathtotal)
	# print(df.head())

	print(df.shape)

	# print(df.describe)

	# df2 = df.drop_duplicates()

	# null_values = df.isnull().sum()
	# print(null_values)

	# Print the columns with null values
	# print("Columns with null values:")
	# print(null_values[null_values > 0])

	df = df.dropna()

	df[['latitude', 'longitude']] = df['currentLocation'].str.extract(r'POINT \((-?\d+\.?\d+) (-?\d+\.?\d+)\)')
	df = df.drop('currentLocation', axis=1)

	# print(df.head())
	df.to_csv('cleaned_participant_logs/'+filename+'.csv', index=False)

	print(filename+"===done")


filepath = "D:/RIT Studies/Sem 4 - Summer 2023/Project/data/Datasets/Activity Logs/"

for i in range(2, 73):
	filename = "ParticipantStatusLogs"+str(i)+".csv"
	clean(filepath, filename)