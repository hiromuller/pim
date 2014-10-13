
function movePage(action){
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
    var input_invited_username = document.createElement("input");
    var input_action = document.createElement("input");

    input_invited_username.setAttribute("name", "invited_username");
    input_invited_username.setAttribute("type", "hidden");
    input_invited_username.setAttribute("value", invited_username);
    form.appendChild(input_invited_username);

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

function setSubContentForm(userProgressId) {
	$('#id_select_target').val($('#target_' + userProgressId).text());
	$('#id_user_progress_id').val($('#id_user_progress_id_' + userProgressId).text());
	$('#id_progress').val($('#progress_' + userProgressId).text());
	$('#id_relationship').val($('#relationship_' + userProgressId).text());
	$('#id_remarks').val($('#remarks_' + userProgressId).text());
	$('#id_submit_progress').val("譖ｴ譁ｰ");
	$('#id_progress_action').val("progress_update");
//	alert ($("#id_progress_action").val());

}

function deleteObject(object_id, delete_from_id, action) {
	if(window.confirm('蜑企勁縺励■繧�＞縺ｾ縺�')){
        var form = document.getElementById("list_form");
        var input_object_id = document.createElement("input");
	    var input_delete_from_id = document.createElement("input");
	    var input_action = document.createElement("input");

	    input_object_id.setAttribute("name", "object_id");
	    input_object_id.setAttribute("type", "hidden");
	    input_object_id.setAttribute("value", object_id);
	    form.appendChild(input_object_id);

	    input_delete_from_id.setAttribute("name", "delete_from_id");
	    input_delete_from_id.setAttribute("type", "hidden");
	    input_delete_from_id.setAttribute("value", delete_from_id);
	    form.appendChild(input_delete_from_id);

	    input_action.setAttribute("name", "action");
	    input_action.setAttribute("type", "hidden");
	    input_action.setAttribute("value", action);
	    form.appendChild(input_action);

	    form.submit();
    }
}

function test() {
	window.alert("TEST!!");
}


$(document).ready(function() {
    $('#id_met_date').datepicker({ dateFormat: "yy-mm-dd" });
    // $('#id_birthday').datepicker({ dateFormat: "yy-mm-dd" });
    // 2驥肴款縺鈴亟豁｢
    //$('#id_target_register_submit').attr('disabled',true);
    //$('#id_submit_progress').attr('disabled',true);
    //$('#id_team_add_submit').attr('disabled',true);
    //$('#id_team_invite_submit').attr('disabled',true);
   });

