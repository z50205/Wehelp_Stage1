let signupform=document.getElementById("signupform");
signupform.addEventListener("submit",(ev)=>{
    let signupname=document.getElementById("signupname").value;
    let username=document.getElementById("signupusername").value;
    let password=document.getElementById("signuppassword").value;
    if (signupname==""||username==""||password==""){
        ev.preventDefault();
        alert("請輸入完整註冊資訊");
    }
})

let loginform=document.getElementById("loginform");
loginform.addEventListener("submit",(ev)=>{
    let username=document.getElementById("signinusername").value;
    let password=document.getElementById("signinpassword").value;
    if (username==""||password==""){
        ev.preventDefault();
        alert("請輸入完整登入資訊");
    }
})
