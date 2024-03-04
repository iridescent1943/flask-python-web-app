function checkPassword() {
    var oldPassword = document.getElementById("old_password").value;
    var newPassword = document.getElementById("new_password").value;
    var confirmPassword = document.getElementById("confirm_password").value;
    var submit = document.getElementById("to_be_activated");
    var msg = document.getElementById("msg");

    // Regular expression for checking password complexity
    var pwdRegex = /^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[^a-zA-Z0-9]).{8,30}$/;

    // Check if the new password is different from the old password
    if (newPassword !== oldPassword) {
        // Check if the passwords match
        if (newPassword === confirmPassword) {
            // Check if the password meets the strength criteria
            if (pwdRegex.test(newPassword)) {
                msg.innerHTML = "<br><font color='green'>Passwords match and meet complexity requirements.</font>";
                submit.disabled = false;
            } else {
                msg.innerHTML = "<br><font color='red'>Passwords match but do not meet complexity requirements.</font>";
                submit.disabled = true;
            }
        } else {
            msg.innerHTML = "<br><font color='red'>Passwords do not match!</font>";
            submit.disabled = true;
        }
    } else {
        msg.innerHTML = "<br><font color='red'>New password must be different from the old password.</font>";
        submit.disabled = true;
    }
}


document.addEventListener("DOMContentLoaded", function() {
    // Get the element with id="defaultOpen" and click on it
    document.getElementById("defaultOpen").click();
});


function openPage(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("guidecontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("guidelink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;
  }

   
document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('inactivateStaffModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var staff_id = event.relatedTarget.getAttribute('data-inactivate-id');
        document.getElementById('inactivateStaff').action = "/admin/staff/inactivate/" + staff_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('reactivateStaffModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var staff_id = event.relatedTarget.getAttribute('data-reactivate-id');
        document.getElementById('reactivateStaff').action = "/admin/staff/reactivate/" + staff_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('deleteStaffModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var user_id = event.relatedTarget.getAttribute('data-delete-id');
        document.getElementById('deleteStaff').action = "/admin/staff/delete/" + user_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('inactivateMarinerModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var mariner_id = event.relatedTarget.getAttribute('data-inactivate-id');
        document.getElementById('inactivateMariner').action = "/admin/mariner/inactivate/" + mariner_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('inactivateMarinerModal1'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var mariner_id = event.relatedTarget.getAttribute('data-inactivate-id');
        document.getElementById('inactivateMariner1').action = "/staff/mariner/inactivate/" + mariner_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('reactivateMarinerModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var mariner_id = event.relatedTarget.getAttribute('data-reactivate-id');
        document.getElementById('reactivateMariner').action = "/admin/mariner/reactivate/" + mariner_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('reactivateMarinerModal1'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var mariner_id = event.relatedTarget.getAttribute('data-reactivate-id');
        document.getElementById('reactivateMariner1').action = "/staff/mariner/reactivate/" + mariner_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('deleteMarinerModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var user_id = event.relatedTarget.getAttribute('data-delete-id');
        document.getElementById('deleteMariner').action = "/admin/mariner/delete/" + user_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('deleteMarinerModal1'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var user_id = event.relatedTarget.getAttribute('data-delete-id');
        document.getElementById('deleteMariner1').action = "/staff/mariner/delete/" + user_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('deleteGuideModal'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var ocean_id = event.relatedTarget.getAttribute('data-delete-id');
        document.getElementById('deleteGuide').action = "/admin/guide/delete/" + ocean_id;
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var myModal = new bootstrap.Modal(document.getElementById('deleteGuideModal1'));
    myModal._element.addEventListener('show.bs.modal', function (event) {
        var ocean_id = event.relatedTarget.getAttribute('data-delete-id');
        document.getElementById('deleteGuide1').action = "/admin/guide/delete/" + ocean_id;
    });
});