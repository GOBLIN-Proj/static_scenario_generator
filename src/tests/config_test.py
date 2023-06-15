from static_scenario_generator.scenarios import ScenarioGeneration

def main():
    scenario_class = ScenarioGeneration()

    print(scenario_class.generate_scenario_dataframe("./data/config.json"))

if __name__ == "__main__":
    main()