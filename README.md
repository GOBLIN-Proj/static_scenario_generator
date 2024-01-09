# 💻 Static Scenario Generator (v1.0.0), for the generation of non randomised scenarios for GOBLIN 

 Based on the [GOBLIN](https://gmd.copernicus.org/articles/15/2239/2022/) (**G**eneral **O**verview for a **B**ackcasting approach of **L**ivestock **IN**tensification) Scenario module

 The package is simple. It defines the columns for scenario inputs. A user provided json file is used to generate rows for each scenario and each corresponding livestock system. Each scenario requires 4 rows for each of the livestock systems.  

 Currently parameterised for Ireland, but the database can be updated with additional emissions factor contexts, which are selected able with an emissions factor key. 

 Final result is a pandas dataframe of sceanrio inputs that can be read by numerous GOBLIN packages.

## Installation

Install from git hub. 

When prompted enter your ```<username>``` and password, which is your ```<access_token>```.

```<access_token>``` is provided by the repo manager.

```<username>``` pass your own github username.


```bash
pip install "static_scenario_generator@git+https://github.com/colmduff/static_scenario_generator.git@main" 

```

## Usage
Firstly, the config.json file should look like the following. The example shows two scenarios. 

To add additional scenarios, simply repeat the inputs given here, update the values, including the sceanrio numbers. 

In the previous version (v0.1.0) each scenario took 4 rows, 1 for each livestock system. However, this was cumbersome to deal with, and has now been refactored so that the input data does not require repition. The module will still create the 4 rows in the final dataframe for each entry. But the user only needs a single block to achieve this. 

In addition, the module has been updated to allow the user to use csv files for data input. Each row in the csv file corresponds to a scenario with the same keys as columns. The ordering of the keys does not matter. 

Finally, additional variables related to clover (clover proportion & clover fertilisation) and grass use efficiency (Dairy GUE and Beef GUE) have been added. 

This addition makes the module incompatible with GOBLIN lite v0.1.0. 

```python
[{
    "Scenarios": 0,
    "Manure management cattle": "tank liquid",
    "Manure management sheep": "tank solid",
    "Dairy pop": 1060000,
    "Beef pop":1000,
    "Upland sheep pop": 3000,
    "Lowland sheep pop": 50000,
    "Dairy prod":0,
    "Beef prod":0,
    "Lowland sheep prod": 0,
    "Upland sheep prod": 0,
    "Forest area":1,
    "Conifer proportion":0.7,
    "Broadleaf proportion": 0.3,
    "Conifer harvest": 0.05,
    "Conifer thinned": 0.1,
    "Broadleaf harvest": 0,
    "Crop area": 0,
    "Wetland area":0,
    "Dairy GUE":0,
    "Beef GUE":0,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Clover proportion": 0.5,
    "Clover fertilisation": 0,
    "Urea proportion": 0.2,
    "Urea abated proportion": 0,
    "Afforest year": 2080   
},
{
    "Scenarios": 1,
    "Manure management cattle": "tank liquid",
    "Manure management sheep": "tank solid",
    "Dairy pop": 1060000,
    "Beef pop":1000,
    "Upland sheep pop": 0,
    "Lowland sheep pop": 0,
    "Dairy prod":0,
    "Beef prod":0,
    "Lowland sheep prod": 0,
    "Upland sheep prod": 0,
    "Forest area":1,
    "Conifer proportion":0.7,
    "Broadleaf proportion": 0.3,
    "Conifer harvest": 0.05,
    "Conifer thinned": 0.8,
    "Broadleaf harvest": 0,
    "Crop area": 0,
    "Wetland area":0,
    "Dairy GUE":0,
    "Beef GUE":0,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Clover proportion": 0.5,
    "Clover fertilisation": 0,
    "Urea proportion": 0.2,
    "Urea abated proportion": 0,
    "Afforest year": 2080  
}
]
```

To generate the dataframe, follow the example below.

```python
from static_scenario_generator.scenarios import ScenarioGeneration

def main():
    #instantiate the class 
    scenario_class = ScenarioGeneration()
    
    #pass the configuration file and return a pandas dataframe. 

    print(scenario_class.generate_scenario_dataframe("./data/config.json"))

if __name__ == "__main__":
    main()
    
```
## License
This project is licensed under the terms of the MIT license.
