import { checkFileType, checkFileSize, FileuploadSuccess }  from "./myFunc/FileValidation.js";


"use strict";
console.log(" reading from shopcart2.js");


// file upload validation
// tested, 100% functional
// *****************************************************************************
const cartFileUploadForm = document.getElementById("form_cart_file_upload72");
if (cartFileUploadForm !== undefined && cartFileUploadForm !== null) {
    console.log("value of cartFileUploadForm >>>"+cartFileUploadForm.value);
    console.log("element exists>>>cartFileUploadForm");

    // select file field from the form
    var fileUploadField12 = document.getElementById("id_document");
    // check file type
    fileUploadField12.addEventListener("change", function() {
        var filename = fileUploadField12.files[0].name;
        console.log(filename);
        checkFileType(filename, cartFileUploadForm);
    });
    // check file size
    fileUploadField12.addEventListener("change", function() {
        if (fileUploadField12.files.length > 0) {
            const selectedFile = fileUploadField12.files[0];
            const fileSize = selectedFile.size;
            console.log(fileSize);
            checkFileSize(fileSize, cartFileUploadForm);            
            
        } else {
            console.log('No file selected');
        }
    });

}
