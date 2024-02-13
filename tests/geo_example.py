from geo_static_scenario_generator.geo_scenarios import ScenarioGeneration
import os 

def main():

    path = "./geo_data"

    json_file = "config_1.json"
    csv_file = "csv_load_input.csv"

    scenario_class = ScenarioGeneration()

    scenario_class.json_load(os.path.join(path,json_file)).to_csv(os.path.join(path,"json_load.csv"))

    scenario_class.csv_load(os.path.join(path,csv_file)).to_csv(os.path.join(path,"csv_load.csv"))

    print(scenario_class.generate_scenario_dataframe(os.path.join(path,json_file)))

if __name__ == "__main__":
    main()