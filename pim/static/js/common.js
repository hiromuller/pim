
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

function setSubContentForm(userProgressId) {
	$('#id_select_target').val($('#target_' + userProgressId).text());
	$('#id_user_progress_id').val($('#id_user_progress_id_' + userProgressId).text());
	$('#id_progress').val($('#progress_' + userProgressId).text());
	$('#id_relationship').val($('#relationship_' + userProgressId).text());
	$('#id_remarks').val($('#remarks_' + userProgressId).text());
	$('#id_submit_progress').val("更新");
	$('#id_progress_action').val("progress_update");
//	alert ($("#id_progress_action").val());

}

function test() {
	window.alert("TEST!!");
}

$(document).ready(function() {
    $('#id_met_date').datepicker({ dateFormat: "yy-mm-dd" });
    $('#id_birthday').datepicker({ dateFormat: "yy-mm-dd" });
});
