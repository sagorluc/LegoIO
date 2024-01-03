"use strict";
console.log("reading from myFunc/FileValidation.js");


// *****************************************************************************
// Delete file_upload_failure_msg when user tries to upload a new doc again
function remove_msg_cart_file_upload_fail() {
    var ggtt55 = document.getElementById("cart_file_upload_fail_msg");
    console.log("remove_msg_cart_file_upload_fail is clicked");

    if (ggtt55 !== undefined && ggtt55 !== null) {
        if (ggtt55.innerText == "") {
            console.log("im happy");
        } else {
            // alert('today is tuesday');
            ggtt55.innerText = "";
        }

    }

}




export { fileValidationFileType3 };
