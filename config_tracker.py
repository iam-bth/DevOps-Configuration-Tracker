
#Importing json and os 
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "config_items.json")

from config_item import ConfigItem

#Empty list
config_items = []

#function to save configuration items to a file
def save_to_file():
    with open(FILE_PATH, "w") as f:
        json.dump([item.to_dict() for item in config_items], f, indent = 4)
    print("Configuration items saved to file.")

#function to load configuration items from a file 
def load_from_file():
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            for item_dict in data:
                item = ConfigItem(**item_dict)
                config_items.append(item)
    except FileNotFoundError:
        pass

#function to display the menu
def display_menu(): 
    print("\n===== DevOps Configuration Tracker =====")
    print("1. Add Configuration Item")
    print("2. View Configuration Items")
    print("3. Update Configuration Status")
    print("4. Delete Configuration Item")
    print("5. Search Configuration Item")
    print("6. EXIT")
   
#function to get input from the user to add a configuration item 
def add_config_item():
    name = input("Enter the configuration name: ")
    version = input("Enter the version: ")
    environment = input("Enter the environment (Dev / Staging / Prod): ") #Dev - Development, Staging - Testing, Prod - Production
    status = input("Enter the status (Active / Inactive): ")
    
    item = ConfigItem(name, version, environment, status)
    config_items.append(item)
    print("Confiuration item added successfully.")
    save_to_file()

#function to view all configuration items    
def view_config_items():
    if not config_items:
        print("No configuration items found.")
        return
    
    print("\n----Configuration Items----")
    for idx, item in enumerate(config_items, 1):
        print(f"{idx}. Name: {item.name}, Version: {item.version}, Environment: {item.environment}, Status: {item.status}")    

#function to update the status of a configuration item
def update_config_status():
    if not config_items:
        print("No configuration items to update.")
        return
    
    view_config_items()
    try:
        choice = int(input("Enter the number of the item to update: "))
        if 1 <= choice <= len(config_items):
            new_status = input("Enter new status (Active / Inactive): ")
            config_items[choice - 1].status = new_status
            print("Status updated successfully!")
            save_to_file()
            
        else:
            print("Invalid choice. Please try again.")
            
    except ValueError:
        print("Please enter a valid number.")
   
#function to delete a configuration item     
def delete_config_item():
    if not config_items:
        print("No configuration items to delete.")
        return
    
    view_config_items()
    try:
        choice = int(input("Enter the number you want to delete: "))
        if 1 <= choice <= len(config_items):
            item =  config_items[choice - 1]
            print(f"You selected: {item.name}, {item.environment}, {item.version}")
            
            #adding a confirmation check before deleting
            confirm = input("Are you sure you want to delete this item? (y/n): ").lower()
            
            if confirm == 'y':
                del config_items[choice - 1]
                print("Configuration item deleted successfully.")
                save_to_file()
                
            else:
                print("Deletion cancelled.")
                
        else:
            print("Invalid choice. Please try again.")
            
    except ValueError:
        print("Please enter a valid number.")

#function to search for a configuration item by name
def search_config_items():
    if not config_items:
        print("No configuration items to search.")
        return
    
    search_term = input("Enter the name to search: ").lower()
    results = []
    
    for item in config_items:
        if search_term in item.name.lower():
            results.append(item)
            
    if results:
        print("\nSearch Results:")
        for idx, item in enumerate(results, 1):
            print(f"{idx}. Name: {item.name}, version: {item.version}, Env: {item.environment}, Status: {item.status}")
                
    else:
        print("No configuration items matched your search.")
        
#Main function loop
def main():
    load_from_file()
    while True:
        display_menu()
        choice = input("Choose an option from 1 to 6: ")
        
        if choice == '1':
            add_config_item()
                    
        elif choice == '2': 
            view_config_items()
            
        elif choice == '3':
            update_config_status()
        
        elif choice == '4':    
            delete_config_item()
            
        elif choice == '5':
            search_config_items()
            
        elif choice == '6':
            save_to_file()
            print("Exiting... Goodbye!")
            break
    
        else:
            print("Invalid choice entered. Please try again.")
        
if __name__ == "__main__":
    main()
    
