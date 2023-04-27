import os
import csv
import json

json_data = {}

path = "C://Users//91963//Desktop//LeetCode//files"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
for item in dir_list:
    if "alltime" in item:
        arr = []
        with open("files//"+item, mode ='r')as file:
            csvFile = csv.reader(file)
            cnt = 0
            for lines in csvFile:
                cnt = cnt + 1
                if cnt == 1:
                    continue
                arr.append({
                    "id": lines[0],
                    "title": lines[1],
                    "slug": lines[5].split("/")[4],
                    "acceptance": lines[2],
                    "difficulty": lines[3]
                })
            comp_name = item.split("_")[0]
            json_data[comp_name] = arr
            with open(f"company//{comp_name}.json", "w") as outfile:
                outfile.write(json.dumps({"questions": arr}, indent=4))
            print(item.split("_")[0])
    
# json_object = json.dumps(json_data, indent=4)

# with open("data.json", "w") as outfile:
#     outfile.write(json_object)