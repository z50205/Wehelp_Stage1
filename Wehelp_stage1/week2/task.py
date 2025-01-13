# ---------------------task1分隔線---------------------
def find_and_print(messages, current_station):
    # 資料區域
    # stops將兩路線區分
    stops = [
    [
      "Songshan",
      "Nanjing Sanmin",
      "Taipei Arena",
      "Nanjing Fuxing",
      "Songjiang Nanjing",
      "Zhongshan",
      "Beimen",
      "Ximen",
      "Xiaonanmen",
      "Chiang Kai-Shek Memorial Hall",
      "Guting",
      "Taipower Building",
      "Gongguan",
      "Wanlong",
      "Jingmei",
      "Dapinglin",
      "Qizhang",
      "Xindian City Hall",
      "Xindian",
    ],
    ["Qizhang","Xiaobitan"],]
    # connect_node提供轉乘站資訊(如果一條線路轉乘站較多，此資料須更改為二維arr或dict)
    connect_node = [16,0]
    # friend_pos各朋友所在車站資訊
    friends_pos = {}
    # friend_pos各朋友所在車站資訊
    friends_dis = {}
    # getID方法提供該訊息中所在車站
    def getID(stops, message):
        for route_id in range(len(stops)):
            for stop_id in range(len(stops[route_id])):
                if stops[route_id][stop_id] in message:
                     return [route_id, stop_id]
    # 主程式
    # step1:取得所有朋友所在位置
    for key in messages:
        friends_pos[key] = getID(stops,messages[key])
    # step2:取得自己所在位置
    pos=getID(stops,current_station)
    # step3.1:如於相同路線上即可直接計算差值
    # step3.2:如於不同路線上分別計算至七張之差值，再相加(如果一條線路轉乘站較多，尋路機制可能要再想更細，)
    for key in friends_pos:
        if (friends_pos[key][0]==pos[0]):
            friends_dis[key]=abs(friends_pos[key][1]-pos[1])
        else:
            friends_dis1=abs(friends_pos[key][1]-connect_node[friends_pos[key][0]])
            friends_dis2=abs(pos[1]-connect_node[pos[0]])
            friends_dis[key]=friends_dis1+friends_dis2
    # step4:決定何者最短，並輸出
    least_dis=100
    least_dis_friend=[]
    for key in friends_dis:
        if (friends_dis[key]<least_dis):
            least_dis=friends_dis[key]
            least_dis_friend=[key]
        elif(friends_dis[key]==least_dis):
            least_dis_friend.append(key)
    for fri in least_dis_friend:
        print(fri)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian


# ---------------------task2分隔線---------------------
schedule={}
def book(consultants, hour, duration, criteria):
    # Step0:第一次設定(如果schedule為空字典，依照此請求各顧問名稱設定時程表)
    consultants_dict={consultant["name"]:consultant for consultant in consultants}
    if schedule=={}:
        for key in consultants_dict:
            schedule[key]={"scheduled":[]}
    # Step1:找出有空預約(將請求時程與各顧問時程表時程比較，如請求時程都大於或小於顧問時程則可擺進可選擇顧問陣列中)
    available=[]
    chosen_consultant=[]
    # schedule["John"]["scheduled"]=[[15,16]]
    for key in consultants_dict:
        if schedule[key]["scheduled"]==[]:
            available.append(key)
        else:
            for time_slice in schedule[key]["scheduled"]:
                if not ((time_slice[0]>hour and time_slice[0]>hour+duration) or (time_slice[1]<hour and time_slice[1]<hour+duration)):
                    break
            else:
                available.append(key)
    if len(available)==0:
        print("No Service")
        return
    # Step2:依不同策略找出建議顧問
    if criteria=="price":
        price =5000
        for i in range(len(available)):
            if price>consultants_dict[available[i]][criteria]:
                price=consultants_dict[available[i]][criteria]
                chosen_consultant=available[i]
    elif criteria=="rate":
        rate =0
        for i in range(len(available)):
            if rate<consultants_dict[available[i]][criteria]:
                rate=consultants_dict[available[i]][criteria]
                chosen_consultant=available[i]
    # Step3:更新時間表內容
    schedule[chosen_consultant]["scheduled"].append([hour,hour+duration])
    print (chosen_consultant)

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


# ---------------------task3分隔線---------------------
def func(*data):
# com_dict中間字頻率
    com_dict={}
# result僅出現一次的中間字
    result=[]
# getIndex中間字資料表
    getIndex=[-1,-1,1,1,2,2]
# Step1:紀錄中間字出現次數
    for name in data:
        key=name[getIndex[len(name)]]
        if (key in com_dict):
            com_dict[key]={"times":com_dict[key]["times"]+1,"names":[com_dict[key]["names"],name]}
        else:
            com_dict[key]={"times":1,"names":name}

# Step2:挑出中間字僅一次者，如未有則「沒有」
    for key in com_dict:
        if (com_dict[key]["times"]==1):
            result.append(com_dict[key]["names"])
    if len(result) == 0:
        result=["沒有"]
    for res in result:
        print(res)

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安


# ---------------------task4分隔線---------------------
def get_number(index):
    # residual取得尾數
    resudual=index%3
    # Step1:經觀察，依尾數分開輸出各數列值
    if resudual==1:
        result=4+(index//3)*7
    elif resudual==2:
        result=8+(index//3)*7
    else:
        result=(index//3)*7
    print(result)

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


# ---------------------task5分隔線---------------------
def find(spaces, stat, n):
    # result,min 設定初值
    result =-1
    min=100
    # Step1:於遮罩為1,數值較min小,且比n大才計入，並取得最後更新值
    for i in range(len(stat)):
        if ((stat[i] == 1) and (spaces[i] <min) and (spaces[i] >=n)):
            min =spaces[i]
            result=i
    print(result)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2

