from static_scenario_generator.scenario_data_manager import DataManager
import pandas as pd
import json


class ScenarioGeneration:
    def __init__(self):
        self.data_manager_class = DataManager()


    def generate_scenario_dataframe(self, path):

        with open(path) as config_file:
            config = json.load(config_file)

        columns = self.data_manager_class.scenario_columns

        scenario_df = pd.DataFrame(config, columns=columns)

        return scenario_df
