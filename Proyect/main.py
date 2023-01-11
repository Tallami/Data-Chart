import read_csv
import charts

def run():
    data = read_csv.read_csv("./Proyect/data.csv")
    countries = list(map(lambda x: x["Country"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    charts.generate_pie_chart(countries, percentages)
       
if __name__ == "__main__":
    run()