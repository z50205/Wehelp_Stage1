let userForm=document.getElementById("userform");
let confirmCheckBox=document.getElementById("confirmcheckbox");
userForm.addEventListener("submit",(ev)=>{
    if (!confirmCheckBox.checked){
        ev.preventDefault();
        alert("請勾選同意條款");
    }
})

let posInt=document.getElementById("posint");
let calculateButton=document.getElementById("calbut");
calculateButton.addEventListener("click",()=>{
    integer=parseInt(posInt.value);
    if (isNaN(integer) || integer<=0)
        alert("請輸入正整數");
    else{
        const url = "/square/"+integer;
        window.location.href = url;
}
})