from static_scenario_generator.data_manager import DataManager
import pandas as pd
import json


class ScenarioGeneration:
    def __init__(self):
        self.data_manager_class = DataManager()
        self.common_columns = self.data_manager_class.get_common_columns()
        self.animal_columns = self.data_manager_class.get_animal_columns()
        self.animal_systems = self.data_manager_class.get_systems()


    def generate_scenario_dataframe(self, path):

        if path.endswith(".json"):
            config = self.json_load(path)

        elif path.endswith(".csv"):
            config = self.csv_load(path)


    def json_load(self, path):
        with open(path) as config_file:
            config = json.load(config_file)

        scenario_df = pd.DataFrame(columns=self.common_columns)
        rows = []  # List to store each row dictionary

        for index, sc in enumerate(config):
            for system in self.animal_systems:
                # Initialize a row with default values
                row = {"Scenarios": index, "Cattle systems": system}

                # Fetch system data which is a list of dictionaries
                system_data = self.data_manager_class.get_system(system)

                # Initialize a dictionary to hold the merged key-values from system_data list
                merged_system_data = {}
                for item in system_data:
                    merged_system_data.update(item)


                # Check if the key is in the merged system data and add them to the row
                for key in self.animal_columns:
                    row_key = merged_system_data.get(key, None)
                    if row_key:
                        row[key] = sc.get(row_key, None)  # Use 0 as default if the key is not in the scenario
                    else: 
                        row[key] = 0

                for key in self.common_columns:
                    if key not in self.animal_columns:
                        row[key] = sc.get(key, None)

                rows.append(row)

        # Concatenate all rows into a DataFrame
        scenario_df = pd.concat([scenario_df, pd.DataFrame(rows)], ignore_index=True)

        return scenario_df


    def csv_load(self, path):
        # Read data from CSV file
        config = pd.read_csv(path)

        scenario_df = pd.DataFrame(columns=self.common_columns)
        rows = []  # List to store each row dictionary

        # Iterate over the rows of the CSV data
        for index, sc in config.iterrows():
            for system in self.animal_systems:
                # Initialize a row with default values
                row = {"Scenarios": index, "Cattle systems": system}

                # Fetch system data which is a list of dictionaries
                system_data = self.data_manager_class.get_system(system)

                # Initialize a dictionary to hold the merged key-values from system_data list
                merged_system_data = {}
                for item in system_data:
                    merged_system_data.update(item)

                # Check if the key is in the merged system data and add them to the row
                for key in self.animal_columns:
                    row_key = merged_system_data.get(key, None)
                    if row_key and row_key in sc:
                        row[key] = sc[row_key] if pd.notnull(sc[row_key]) else 0  # Use 0 as default if the key is not in the scenario or value is NaN
                    else:
                        row[key] = 0
                        
                for key in self.common_columns:
                    if key not in self.animal_columns:
                        row[key] = sc[key] if pd.notnull(sc[key]) else 0
                        
                rows.append(row)

        # Concatenate all rows into a DataFrame
        scenario_df = pd.concat([scenario_df, pd.DataFrame(rows)], ignore_index=True)

        return scenario_df
