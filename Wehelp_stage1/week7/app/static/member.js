function deleteMessage(id) {
  let ans = confirm("Caution! Do you really want to delete the message?");
  if (ans) {
    const form = document.createElement("form");
    form.action = "/deleteMessage";
    form.method = "post";
    const input = document.createElement("input");
    input.type = "text";
    input.name = "id";
    input.value = id;
    const submitButton = document.createElement("button");
    submitButton.type = "submit";
    form.appendChild(input);
    form.appendChild(submitButton);
    document.body.appendChild(form);
    form.submit();
  }
}

async function getMemberInfo(){
  const username = document.getElementById("searchname").value;
  const encodeUserName=encodeURIComponent(username);
  const response = await fetch(`/api/member?username=${encodeUserName}`);
  const jsonData=await response.json();
  let result=document.getElementById("searchresult");
  if (jsonData.data!=null){
    result.textContent=jsonData.data['name']+"("+jsonData.data['username']+")";
  }else{
    result.textContent="";
  }
}

async function updateMemberInfo(){
  const updateName= document.getElementById("updatename").value;
  const response = await fetch("/api/member", {
    method: "PATCH",
    headers: new Headers({'content-type': 'application/json'}),
    body:JSON.stringify({"name":updateName}) ,
  });
  updateMemberName(updateName);
}
function updateMemberName(updateName){
  const memberNames= document.getElementsByClassName("membername-self");
  for (i in memberNames){
    memberNames[i].textContent=updateName;
  }
}