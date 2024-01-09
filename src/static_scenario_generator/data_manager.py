import os
import yaml
from static_scenario_generator.config import get_local_dir


class DataManager:
    def __init__(self):
        self._config = self.get_config_data(os.path.join(get_local_dir(), "config.yaml"))
        self.common_columns = self._config.get("common_columns", {})
        self.animal_systems = self._config.get("systems", {})
        self.animal_columns = self._config.get("animal_columns", {})



    def get_config_data(self, config_file):
        """
        Load and return the configuration data from the specified file.

        Args:
            config_file (str): The path to the configuration file.

        Returns:
            dict: The configuration data loaded from the file.
        """
        with open(config_file, "r") as file:
            config_data = yaml.safe_load(file)

        return config_data
    
    def get_common_columns(self):
        return self.common_columns
    
    def get_animal_columns(self):
        return self.animal_columns
    
    def get_systems(self):
        return [list(system.keys())[0] for system in self.animal_systems]

    
    def get_system(self, system_name):
        for system in self.animal_systems:
            if system_name in system:
                return system[system_name]
        return {}  # Return an empty dictionary if the system name is not found


    


