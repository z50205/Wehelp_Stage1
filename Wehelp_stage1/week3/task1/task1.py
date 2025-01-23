import json
import os
import csv

# Step1.1：讀取各景點資料為json
spot_info_fp=os.path.join(os.path.dirname(__file__),"..","taipei-attractions-assignment-1")
spot_info_f=open(spot_info_fp,"r",encoding="utf-8")
spot_info_json=json.load(spot_info_f)

# Step1.2：讀取各捷運站資料為json
mrt_info_fp=os.path.join(os.path.dirname(__file__),"..","taipei-attractions-assignment-2")
mrt_info_f=open(mrt_info_fp,"r",encoding="utf-8")
mrt_info_json=json.load(mrt_info_f)

# Step2.1：初始化景點字典，以流水號為Key(兩資料應以SERIAL_NO為外鍵，故以SERIAL_NO為Key，不然會要嵌套兩個for去比SERIAL_NO)
spot_dict={}
for i in range(len(spot_info_json['data']['results'])):
    url_end=spot_info_json['data']['results'][i]["filelist"][1:].index("http")+1
    url=spot_info_json['data']['results'][i]["filelist"][0:url_end]
    spot_dict[spot_info_json['data']['results'][i]["SERIAL_NO"]]=\
        {"stitle":spot_info_json['data']['results'][i]["stitle"],\
         "longitude":spot_info_json['data']['results'][i]["longitude"],\
         "latitude":spot_info_json['data']['results'][i]["latitude"],\
         "url":url}

# Step2.2：初始化位址字典，仍以流水號為Key
mrt_dict={}
for i in range(len(mrt_info_json['data'])):
    district_end=mrt_info_json['data'][i]["address"].index("區")
    district=mrt_info_json['data'][i]["address"][district_end-2:district_end+1]
    mrt_dict[mrt_info_json['data'][i]["SERIAL_NO"]]=\
        {"MRT":mrt_info_json['data'][i]["MRT"],\
         "district":district}
    
# Step3：以流水號為Key，互相關聯相關資料並存入各results_dict
spot_results={}
mrt_results={}
for key in spot_dict:
    spot_results[key]={"stitle":spot_dict[key]["stitle"],\
         "district": mrt_dict[key]["district"],\
         "longitude":spot_dict[key]["longitude"],\
         "latitude":spot_dict[key]["latitude"],\
         "url":spot_dict[key]["url"]}
    if mrt_dict[key]["MRT"] in mrt_results.keys():
        mrt_results[mrt_dict[key]["MRT"]].append(spot_dict[key]["stitle"])
    else:
        mrt_results[mrt_dict[key]["MRT"]]=[spot_dict[key]["stitle"]]

#Step4：調用csv存入資料
spot_result_fp=os.path.join(os.path.dirname(__file__),"spot.csv")
fieldnames = ['results']
writer = csv.DictWriter(open(spot_result_fp, "w", newline=''),fieldnames)
for key in spot_results:
    writer.writerow({'results':spot_results[key]['stitle']+","+spot_results[key]["district"]+\
                     ","+spot_results[key]["longitude"]+","+spot_results[key]["latitude"]+\
                        ","+spot_results[key]["url"]})

mrt_result_fp=os.path.join(os.path.dirname(__file__),"mrt.csv")
fieldnames = ['results']
writer = csv.DictWriter(open(mrt_result_fp, "w", newline=''),fieldnames)
for key in mrt_results:
    writer.writerow({'results':str(key)+','+','.join(mrt_results[key])})