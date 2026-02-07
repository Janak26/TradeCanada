import pandas as pd
from datetime import datetime



def convert_date(value):
	value = datetime.strptime(value, "%Y-%m")
	return value


def processDataframe(dataf):
	dataf['Principal trading partners'] = dataf['Principal trading partners'].replace('Türkiye', 'Turkey')
	dataf = dataf[['REF_DATE', 'GEO', 'DGUID', 'Trade',
	'North American Product Classification System (NAPCS)', 'Principal trading partners',
	'VECTOR', 'COORDINATE', 'VALUE']]
	dataf['REF_DATE'] = dataf['REF_DATE'].apply(convert_date)
	return dataf



if __name__ == "__main__":
	df = pd.read_csv(r"12100175.csv")
	df = processDataframe(df)
	df.to_csv(r"processed.csv", index=False)