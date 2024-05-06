"use strict";
console.log("reading from myFunc/FileValidation.js");


// *****************************************************************************
function resetGuestResumeForm0(form) {
    form.reset();
}


// *****************************************************************************
function checkFileType(file, form) {    
    console.log("line8>>fileName225>>>"+file);

    console.log("filevalidation>>line17>>>fileName1>>>"+file);
    var file_ext = file.split(".").pop();

    if (file_ext === "doc" || file_ext === "docx") {
        console.log("thanks for uploading your resume");

    } else {
        console.log("checkFileType failed");
        $("#modal_1771").click();
        // reset form
        resetGuestResumeForm0(form);      
    }
    
}


// *****************************************************************************
function checkFileSize(fileSize, form) {
    const maxSize = 2 * 1024 * 1024 ;

    if (fileSize > maxSize) {
        console.log("checkFileSize failed");        
        $("#modal_1772").click();
        // reset form
        resetGuestResumeForm0(form);        
    } else {
        console.log("thank you for uploading");
    }

}


// *****************************************************************************
function FileuploadSuccess(form) {

    $("#modal_1773").click();
    // reset form
    resetGuestResumeForm0(form);        
    console.log("file upload success");

}

export { checkFileType, checkFileSize, FileuploadSuccess };
