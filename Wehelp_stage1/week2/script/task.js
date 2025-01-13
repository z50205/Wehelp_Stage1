// ---------------------task1分隔線---------------------
function findAndPrint(messages, currentStation) {
    //資料區域
    //stops將兩路線區分
  const stops = [
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
    ["Qizhang","Xiaobitan"],
  ];
  //connect_node提供轉乘站資訊(如果一條線路轉乘站較多，此資料須更改為二維arr或dict)
  const connect_node = [16,0];
  //friend_pos各朋友所在車站資訊
  let friends_pos = {};
  //friend_pos各朋友所在車站資訊
  let friends_dis = {};
  //getID方法提供該訊息中所在車站
  function getID(stops, message) {
    for (let route_id in stops) {
      for (let stop_id in stops[route_id]) {
        if (message.includes(stops[route_id][stop_id])) {
          return [route_id, stop_id]
        }
      }
    }
  }

  //主程式
  let ele1=document.getElementById("task1");
  //step1:取得所有朋友所在位置
  for (let key in messages) {
    friends_pos[key] = getID(stops,messages[key]);
  }
  //step2:取得自己所在位置
  pos=getID(stops,currentStation)

  //step3.1:如於相同路線上即可直接計算差值
  //step3.2:如於不同路線上分別計算至七張之差值，再相加(如果一條線路轉乘站較多，尋路機制可能要再想更細，)
  for (let key in friends_pos){
    if (friends_pos[key][0]==pos[0]){
        friends_dis[key]=Math.abs(friends_pos[key][1]-pos[1]);
    }
    else{
        friends_dis1=Math.abs(friends_pos[key][1]-connect_node[friends_pos[key][0]]);
        friends_dis2=Math.abs(pos[1]-connect_node[pos[0]]);
        friends_dis[key]=friends_dis1+friends_dis2;
    }
  }
    //step4:決定何者最短，並輸出
  let least_dis=100;
  let least_dis_friend=[];
  for (let key in friends_dis){
    if (friends_dis[key]<least_dis){
        least_dis=friends_dis[key];
        least_dis_friend=[key];
    }else if(friends_dis[key]==least_dis){
        least_dis_friend.push(key);
    }
  }
  for(let i in least_dis_friend){
    console.log(least_dis_friend[i]);
    ele1.innerHTML =ele1.innerHTML +"<p class='answer_node'>"+least_dis_friend[i]+"</p>";
  }
}

const messages = {
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Leslie: "I'm at home near Xiaobitan station.",
  Vivian: "I'm at Xindian station waiting for you.",
};
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian


// ---------------------task2分隔線---------------------
let schedule={};
function book(consultants, hour, duration, criteria){
  // Step0:第一次設定(如果schedule為空字典，依照此請求各顧問名稱設定時程表)
  consultants_dict={}
  for (let consultant in consultants){
    consultants_dict[consultants[consultant]["name"]]=consultants[consultant];
  }
  if (Object.keys(schedule)==0){
    for(let key in consultants_dict){
          schedule[key]={"scheduled":[]}
        }
      }
  // Step1:找出有空預約(將請求時程與各顧問時程表時程比較，如請求時程都大於或小於顧問時程則可擺進可選擇顧問陣列中)
  let ele2=document.getElementById("task2");
  let available=[]
  let chosen_consultant=[]
  for (let key in consultants_dict){
    if (schedule[key]["scheduled"].length==0){
      available.push(key);
    }else{
      let conflict=true;
      for(let id in schedule[key]["scheduled"]){
        time_slice=schedule[key]["scheduled"][id];
        if (!((time_slice[0]>hour & time_slice[0]>hour+duration) || (time_slice[1]<hour & time_slice[1]<hour+duration))){
          conflict=false;
          break;
        }
      }
      if (conflict)available.push(key);
      }
  }
  if (available.length==0){
    console.log("No Service");
    return;
  }
  // Step2:依不同策略找出建議顧問
  if (criteria=="price"){
    price =5000;
    for (let i in available){
      if (price>consultants_dict[available[i]][criteria]){
        price=consultants_dict[available[i]][criteria];
        chosen_consultant=available[i];
      }
    }
  }else if(criteria=="rate"){
    rate =0;
    for (let i in available){
      if (rate<consultants_dict[available[i]][criteria]){
        rate=consultants_dict[available[i]][criteria];
        chosen_consultant=available[i];
      }
    }
  }
  // Step3:更新時間表內容
  schedule[chosen_consultant]["scheduled"].push([hour,hour+duration]);
  console.log(chosen_consultant);
  ele2.innerHTML =ele2.innerHTML +"<p class='answer_node'>"+chosen_consultant+"</p>";
}

  const consultants=[
  {"name":"John", "rate":4.5, "price":1000},
  {"name":"Bob", "rate":3, "price":1200},
  {"name":"Jenny", "rate":3.8, "price":800}
  ];
  book(consultants, 15, 1, "price"); // Jenny
  book(consultants, 11, 2, "price"); // Jenny
  book(consultants, 10, 2, "price"); // John
  book(consultants, 20, 2, "rate"); // John
  book(consultants, 11, 1, "rate"); // Bob
  book(consultants, 11, 2, "rate"); // No Service
  book(consultants, 14, 3, "price"); // John


// ---------------------task3分隔線---------------------
function func(...data){
  let ele3=document.getElementById("task3");
  //com_dict中間字頻率
  let com_dict={};
  //result僅出現一次的中間字
  let result=[];
  //getIndex中間字資料表
  const getIndex=[-1,-1,1,1,2,2];
  //Step1:紀錄中間字出現次數
  for (let id in data){
    key=data[id][getIndex[data[id].length]];
    if (key in com_dict){
      com_dict[key]={times:com_dict[key]["times"]+1,names:[com_dict[key]["names"],data[id]]};
    }else{
      com_dict[key]={times:1,names:data[id]};
    }
  }
  //Step2:挑出中間字僅一次者，如未有則「沒有」
  for (let key in com_dict){
    if (com_dict[key]["times"]==1){
      result.push(com_dict[key]["names"]);
    }
  }
  if (result.length==0){
    result=["沒有"]
  }

  for (res in result){
    console.log(result[res]);
    ele3.innerHTML =ele3.innerHTML +"<p class='answer_node  chinese_text'>"+result[res]+"</p>";
  }
  }

  func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
  func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
  func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
  func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安


// ---------------------task4分隔線---------------------
function getNumber(index){
  let ele4=document.getElementById("task4");
  // residual取得尾數
  let residual=index%3;
  // result設定初值
  let result=0;
  // Step1:經觀察，依尾數分開輸出各數列值
  if (residual==1){
    result=4+Math.floor(index/3)*7;
  }else if(residual==2){
    result=8+Math.floor(index/3)*7;
  }else{
    result=Math.floor(index/3)*7;
  }
  console.log(result);
  ele4.innerHTML =ele4.innerHTML +"<p class='answer_node'>"+result+"</p>";
  }

  getNumber(1); // print 4
  getNumber(5); // print 15
  getNumber(10); // print 25
  getNumber(30); // print 70


// ---------------------task5分隔線---------------------
function find(spaces, stat, n){
  let ele5=document.getElementById("task5");
  // result,min 設定初值
  let result =-1;
  let min=100;
  // Step1:於遮罩為1,數值較min小,且比n大才計入，並取得最後更新值
  for (let i in stat){
    if ((stat[i] == 1)&(spaces[i] <min)&(spaces[i] >=n)){
      min =spaces[i];
      result=i;
    }
  }
  console.log(result);
  ele5.innerHTML =ele5.innerHTML +"<p class='answer_node'>"+result+"</p>";
  }

  find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
  find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
  find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2

