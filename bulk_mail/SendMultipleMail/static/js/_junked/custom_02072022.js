// $(window).load(function() {
//     $(".loader").fadeOut("slow");
// })

window.onload = function() 
{
    //display loader on page load 
    $('.loader').fadeOut("slow");
}


//////////// function to handle dynamic state of global search button
function searchButtonState() {
    if(document.getElementById("id_globalsearchquery").value==="") { 
        document.getElementById('globalsearchbut').disabled = true; 
    } else { 
        document.getElementById('globalsearchbut').disabled = false;
    }
}






function guestResumeFileValidation3(){
    // console.log("guestResumeFileValidation2 is invoked"+resumeUploadField0);

    let resumeUploadField1 = document.getElementById("id_file1");
    if (resumeUploadField1.files.length > 0) {
       const fileName1 = resumeUploadField1.files[0].name
       console.log(fileName1);
       let file_ext = fileName1.split(".").pop();

        if (file_ext === 'doc' || file_ext === 'docx') {
            console.log('thanks for uploading your resume');
            
        } else {
          // console.log('else st was hit. line#29');
          $('#modal_resume_wrongfiletype').click();
          resetGuestResumeForm0();
        }  


        for (let i = 0; i <= resumeUploadField1.files.length - 1; i++) {
            const fsize = resumeUploadField1.files.item(i).size;
            const file = Math.round((fsize / 1024));

            if (file >= 4096) {
                $('#modal_resume_largefile').click();
                resetGuestResumeForm0();
            } 
            else {
                console.log('thanks for uploading your resume');
            }                    

        }        

    }
}



//////////// function to handle general resume upload file extension behavior
$(document).ready(function(){
    console.log("im from custom.js line67");

    let x11 = document.getElementById("resumeform1");
    console.log("value of x1 from line#70"+x11.value)

    if (typeof(x11) != 'undefined' && x11 != null){

        console.log('element exists>>>document.getElementById("resumeform1")');
        let resumeUploadField0 = document.getElementById("id_file1");
        resumeUploadField0.addEventListener('change', guestResumeFileValidation3)

    }
    else{
        alert("document.getElementById resumeform1 does not exists")
    }



});


