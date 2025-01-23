async function getData() {
    const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      return json
    } catch (error) {
      console.error(error.message);
    }
  }
function insertSpotData(spotInfo) {
    // //取得相較week1需要調整的title及圖片節點以修改屬性
    // //取得promotion相關子節點調整title為景點名稱；圖片src為fetch的網址
    // let promotions=document.getElementsByClassName('Sbox_items');
    // for (let i=0;i< promotions.length;i++){
    //     promotionChilds=promotions[i].childNodes;
    //     promotionChilds[0].src=spotInfo[i][1];
    //     promotionChilds[1].textContent=spotInfo[i][0];
    // }
    // //取得大圖片相關子節點調整title為景點名稱；圖片src為fetch的網址
    // let contents=document.getElementsByClassName('Bbox_items_2');
    // for (let i=0;i< 10;i++){
    //     contentChilds=contents[i].childNodes;
    //     contentChilds[3].src=spotInfo[i+3][1];
    //     contentChilds[5].children[0].textContent=spotInfo[i+3][0];
    // }
    let promotionParent=document.getElementsByClassName("Sbox_div")[0];
    for (let i=0;i< 3;i++){
            let newPromotion=document.createElement("div");
            newPromotion.className="Sbox_items";
            let newPromotionImg=document.createElement("img");
            newPromotionImg.src=spotInfo[i][1];
            newPromotionImg.height="50";
            newPromotionImg.weight="80";
            let newPromotionText=document.createElement("p");
            newPromotionText.className="Sbox_texts";
            newPromotionText.textContent=spotInfo[i][0];
            newPromotion.appendChild(newPromotionImg);
            newPromotion.appendChild(newPromotionText);
            promotionParent.appendChild(newPromotion);
        }
    let BboxParent=document.getElementsByClassName("Bbox_div")[0];
    for (let i=0;i< 10;i++){
            let newBbox_items=document.createElement("div");
            newBbox_items.className="Bbox_items";
            let newBbox_items_2=document.createElement("div");
            newBbox_items_2.className="Bbox_items_2";
            let newBboxStar=document.createElement("img");
            newBboxStar.className="star_svg";
            newBboxStar.src="static/star.svg";
            let newBboxImg=document.createElement("img");
            newBboxImg.className="pic";
            newBboxImg.src=spotInfo[i+3][1];
            let newBboxTitle=document.createElement("div");
            newBboxTitle.className="title_div";
            let newBboxText=document.createElement("p");
            newBboxText.className="title_text";
            newBboxText.textContent=spotInfo[i+3][0];
            newBboxTitle.appendChild(newBboxText);
            newBbox_items_2.appendChild(newBboxStar);
            newBbox_items_2.appendChild(newBboxImg);
            newBbox_items_2.appendChild(newBboxTitle);
            newBbox_items.appendChild(newBbox_items_2);
            BboxParent.appendChild(newBbox_items);
        }
  }

  function clickInsert() {
    let BboxParent=document.getElementsByClassName("Bbox_div")[0];
    let spotCountLimit=spotCount+10
    for (;spotCount< spotCountLimit;){
      if (spotCount>=spotInfo.length-3){
        return;
      }
            let newBbox_items=document.createElement("div");
            newBbox_items.className="Bbox_items";
            let newBbox_items_2=document.createElement("div");
            newBbox_items_2.className="Bbox_items_2";
            let newBboxStar=document.createElement("img");
            newBboxStar.className="star_svg";
            newBboxStar.src="static/star.svg";
            let newBboxImg=document.createElement("img");
            newBboxImg.className="pic";
            newBboxImg.src=spotInfo[spotCount+3][1];
            let newBboxTitle=document.createElement("div");
            newBboxTitle.className="title_div";
            let newBboxText=document.createElement("p");
            newBboxText.className="title_text";
            newBboxText.textContent=spotInfo[spotCount+3][0];
            newBboxTitle.appendChild(newBboxText);
            newBbox_items_2.appendChild(newBboxStar);
            newBbox_items_2.appendChild(newBboxImg);
            newBbox_items_2.appendChild(newBboxTitle);
            newBbox_items.appendChild(newBbox_items_2);
            BboxParent.appendChild(newBbox_items);
            spotCount=spotCount+1;
        }
  }

async function init(spotInfo){
    let spotData=await getData();
    let spotDict=spotData['data']['results'];
    for(let i in spotDict){
        let urlPart=spotDict[i]["filelist"].substring(1);
        let urlEnd=urlPart.indexOf("http")+1;
        let urlFirst=spotDict[i]["filelist"].substring(0,urlEnd);
        spotInfo.push([spotDict[i]['stitle'],urlFirst]);
    }
    insertSpotData(spotInfo);
    spotCount=10;
}
let spotInfo=[];
let spotCount;
init(spotInfo);
