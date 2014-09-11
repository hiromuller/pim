
function moveTo(action){
    var form = document.getElementById("navigation_form");
    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);
    form.submit();
}

function moveToDetail(action, key){

    var form = document.getElementById("list_form");

    var elm = document.createElement("input");
    elm.setAttribute("name", "action");
    elm.setAttribute("type", "hidden");
    elm.setAttribute("value", action);
    form.appendChild(elm);

    var elm2 = document.createElement("input");
    elm2.setAttribute("name", "key");
    elm2.setAttribute("type", "hidden");
    elm2.setAttribute("value", key);
    form.appendChild(elm2);

    form.submit();
}

function display(target) {
    var obj=document.all && document.all(target) || document.getElementById && document.getElementById(target);
    if(obj && obj.style) obj.style.display=
    "none" == obj.style.display ?"" : "none"
}

function acceptMember(invited_username, action) {
    var form = document.getElementById("admin_approval_form");
    var invited_username = document.createElement("input");
    var input_action = document.createElement("input");

    invited_username.setAttribute("name", "invited_username");
    invited_username.setAttribute("type", "hidden");
    invited_username.setAttribute("value", invited_username);
    form.appendChild(invited_username);

    input_action.setAttribute("name", "action");
    input_action.setAttribute("type", "hidden");
    input_action.setAttribute("value", action);
    form.appendChild(input_action);

    form.submit();
}

function acceptTeam(team_id, action) {
    var form = document.getElementById("invited_user_approval_form");
    var input_team = document.createElement("input");
    var input_action = document.createElement("input");

    input_team.setAttribute("name", "team_id");
    input_team.setAttribute("type", "hidden");
    input_team.setAttribute("value", team_id);
    form.appendChild(input_team);

    input_action.setAttribute("name", "action");
    input_action.setAttribute("type", "hidden");
    input_action.setAttribute("value", action);
    form.appendChild(input_action);

    form.submit();
}

function test() {
	window.alert("TEST!!");
}

$(document).ready(function() {
    $('#id_met_date').datepicker({ dateFormat: "yy-mm-dd" });
    $('#id_birthday').datepicker({ dateFormat: "yy-mm-dd" });
});
