
function moveTo(action){
    var form = document.getElementById("navigation_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);
    form.submit();
}

function display(target) {
    var obj=document.all && document.all(target) || document.getElementById && document.getElementById(target);
    if(obj && obj.style) obj.style.display=
    "none" == obj.style.display ?"" : "none"
}

function test() {
	window.alert("TEST!!");
}

$(document).ready(function() {
    $('#id_met_date').datepicker({ dateFormat: "yy-mm-dd" });
    $('#id_birthday').datepicker({ dateFormat: "yy-mm-dd" });
});
