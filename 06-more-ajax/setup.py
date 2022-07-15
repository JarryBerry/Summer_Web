from mongita import MongitaClientDisk
client = MongitaClientDisk(host="./.mongita")

#---
shopping_db = client.shopping_db
shopping_list = shopping_db.shopping_list
shopping_list.delete_many({})

shopping_list.insert_one({"description":"apple"})
shopping_list.insert_one({"description":"milk"})
shopping_list.insert_one({"description":"cheese"})
shopping_list.insert_one({"description":"cookies"})
shopping_list.insert_one({"description":"hot dogs"})
shopping_list.insert_one({"description":"mustard"})


items = list(shopping_list.find({}))
items = [item['desc'] for item in items]
print(items)
