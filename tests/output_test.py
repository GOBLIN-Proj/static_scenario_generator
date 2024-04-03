import unittest
import os
from tempfile import TemporaryDirectory
from static_scenario_generator.scenarios import ScenarioGeneration

class TestGenerateScenarioDataFrame(unittest.TestCase):
    def test_generate_scenario_dataframe_creates_file(self):
        # Use a temporary directory
        with TemporaryDirectory() as tmp_dir:
            path = "./data" # Use the temporary directory
            json_file = "config_1.json"
            csv_file = "csv_load_input.csv"
            expected_file_name = "generated_scenario.csv"
            expected_file_path_json = os.path.join(tmp_dir, expected_file_name)
            expected_file_path_csv = os.path.join(tmp_dir, csv_file)

            # Instantiate your ScenarioGeneration class
            scenario_class = ScenarioGeneration()

            # Call the method under test
            scenario_class.generate_scenario_dataframe(os.path.join(path, json_file)).to_csv(expected_file_path_json)
            
            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path_json), f"File {expected_file_name} was not created in temporary directory.")

            # Call the method under test
            scenario_class.generate_scenario_dataframe(os.path.join(path, csv_file)).to_csv(expected_file_path_csv)
            
            # Check if the file was created as expected
            self.assertTrue(os.path.exists(expected_file_path_csv), f"File {expected_file_name} was not created in temporary directory.")

# Running the tests
if __name__ == '__main__':
    unittest.main()
