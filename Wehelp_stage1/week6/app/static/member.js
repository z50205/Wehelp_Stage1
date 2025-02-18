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
