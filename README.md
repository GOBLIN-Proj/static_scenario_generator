# 💻 Static Scenario Generator, for the generation of non randomised scenarios for GOBLIN

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
Firstly, the config.json file should look like the following. The example shows a single scenario. 

To add additional scenarios, simply repeat the inputs given here, update the values, including the sceanrio numbers. 

Remember that each scenario takes 4 rows, 1 for each livestock system.
```python
[{
    "Scenarios": 0,
    "Cattle systems": "Dairy",
    "Manure management": "tank liquid",
    "Dairy pop": 1060000,
    "Beef pop":0,
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
    "Grass management":0,
    "Upland sheep pop": 0,
    "Lowland sheep pop": 0,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Afforest year": 2080   
},
{
    "Scenarios": 0,
    "Cattle systems": "Beef",
    "Manure management": "tank liquid",
    "Dairy pop": 0,
    "Beef pop":1128000,
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
    "Grass management":0,
    "Upland sheep pop": 0,
    "Lowland sheep pop": 0,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Afforest year": 2080   
},
{
    "Scenarios": 0,
    "Cattle systems": "Lowland sheep",
    "Manure management": "tank solid",
    "Dairy pop": 0,
    "Beef pop":0,
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
    "Grass management":0,
    "Upland sheep pop": 2036000,
    "Lowland sheep pop": 0,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Afforest year": 2080   
},
{
    "Scenarios": 0,
    "Cattle systems": "Upland sheep",
    "Manure management": "tank solid",
    "Dairy pop": 0,
    "Beef pop":0,
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
    "Grass management":0,
    "Upland sheep pop": 0,
    "Lowland sheep pop": 509000,
    "Dairy Pasture fertilisation": 150,
    "Beef Pasture fertilisation": 110,
    "Afforest year": 2080   
},
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


if __name__ == "__main__":
    main()
    
```
## License
This project is licensed under the terms of the MIT license.
