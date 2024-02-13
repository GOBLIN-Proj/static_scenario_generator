from resource_manager.data_manager import DataManager

def main():
    dm = DataManager()
    
    print(dm.get_common_columns())
    
    print(dm.get_systems())

    print(dm.get_system("Dairy"))

if __name__ == "__main__":
    main()