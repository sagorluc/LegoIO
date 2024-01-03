"use strict";
console.log("reading from myFunc/FileValidation.js");


// *****************************************************************************
function resetGuestResumeForm0(form) {
    form.reset();
}


// *****************************************************************************
function fileValidationFileType3(fileName226, form) {
    console.log("line8>>fileName225>>>"+fileName226);

    const fileName1 = fileName226 //fileUploadField0.files[0].name;
    console.log("line16>>>fileName1>>>"+fileName1);
    var file_ext = fileName1.split(".").pop();

    if (file_ext === "doc" || file_ext === "docx") {
        console.log("thanks for uploading your resume");

    } else {
        console.log("else statement was hit. line#25 FileValidation.js");
      
        // open modal to show error msg
        $("#guestResumeModal_wrongfiletype").click();
        $('#cartModal2299').modal('show');
        // reset the corresponding form
        resetGuestResumeForm0(form);      
    }
    
}

// *****************************************************************************
// if (fileUploadField0.files.length > 0) {}
// *****************************************************************************
function checkFileSize3(fileUploadField0) {
    for (let i = 0; i <= fileUploadField0.files.length - 1; i++) {
        const fsize = fileUploadField0.files.item(i).size;
        const file = Math.round((fsize / 1024));

        if (file >= 4096) {
            $("#modal_resume_largefile").click();
            resetGuestResumeForm0();
        }
        else {
            console.log("thanks for uploading your resume");
        }

    }

}




export { fileValidationFileType3 };
