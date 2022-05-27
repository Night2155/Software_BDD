var form = document.getElementById("function-container");
var btn = document.getElementById("btn");
var result = document.getElementById("result-label");
var input_item = document.getElementById("key");

function btn_click(event) {
  event.preventDefault();
  fetch("/calculate", {
    body: input_item.value /*傳入值給伺服器*/,
    method: "POST",
  })
    .then((Value_from_server) =>
      Value_from_server.text()
    ) /*將伺服器回傳的值轉換成text */
    .then((Get_value) => {
      result.innerHTML = Get_value;
    });
  /*result.innerHTML = input_item.value;*/
}
btn.onclick = btn_click;
