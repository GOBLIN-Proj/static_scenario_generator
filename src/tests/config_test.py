from static_scenario_generator.scenarios import ScenarioGeneration
import os 

def main():

    path = "./data"

    json_file = "config_1.json"
    csv_file = "csv_load_input.csv"

    scenario_class = ScenarioGeneration()

    scenario_class.json_load(os.path.join(path,json_file)).to_csv(os.path.join(path,"json_load.csv"))

    scenario_class.csv_load(os.path.join(path,csv_file)).to_csv(os.path.join(path,"csv_load.csv"))

if __name__ == "__main__":
    main()