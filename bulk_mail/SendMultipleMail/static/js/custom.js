import { checkFileType, checkFileSize }  from "./myFunc/FileValidation.js";
import { fetch_comparison_body2 }   from "./myFunc/productComparison.js";
import { checkForEmptySearchInput } from "./myFunc/searchBar.js";
import { hideForm, showForm }       from "./myFunc/buttonOps.js";


"use strict";
console.log(" reading from custom.js");


// handle dynamic state of global search button
// tested
// working 100%
// *****************************************************************************
const searchForm001 = document.getElementById("searchForm001");
// console.log(searchForm001);
if (searchForm001 !== undefined && searchForm001 !== null) {
    searchForm001.addEventListener("submit", checkForEmptySearchInput)
    console.log("yes")
   
}




// guest resume upload validation
// *****************************************************************************
// 100% functional
const guestResumeForm1 = document.getElementById("guestResumeForm1");
if (guestResumeForm1 !== undefined && guestResumeForm1 !== null) {
    console.log("value of guestResumeForm >>>"+guestResumeForm1.value);
    console.log("element exists>>>guestResumeForm1");

    // select file field from the form
    var fileUploadField0 = document.getElementById("id_file1");
    // check file type
    fileUploadField0.addEventListener("change", function() {
        var filename = fileUploadField0.files[0].name;
        console.log(filename);
        checkFileType(filename, guestResumeForm1);
    });
    // check file size
    fileUploadField0.addEventListener("change", function() {
        if (fileUploadField0.files.length > 0) {
            const selectedFile = fileUploadField0.files[0];
            const fileSize = selectedFile.size;
            console.log(fileSize);
            checkFileSize(fileSize, guestResumeForm1);            
            
        } else {
            console.log('No file selected');
        }
    });


    var emailField = document.getElementById("id_email");
    console.log(emailField.value);

    // Show Modal on form Submit
    // guestResumeForm1.addEventListener("submit", function(event) {
    //     event.preventDefault();

    //     // Send form data to the server using Fetch API
    //     fetch('', {
    //         method: 'POST',
    //         body: new FormData(guestResumeForm1)
    //     })
    //     .then(function(response) {
    //         if (response.ok) {
    //             FileuploadSuccess(guestResumeForm1);
    //         } else {
    //             console.log('Form submission failed');
    //         }
    //     })
    //     .catch(function(error) {
    //         console.log(error);
    //     });
    
    // });

    // // Clear modal email message
    // const closeButton = document.getElementById("successModalClose");
    // closeButton.addEventListener("click", function()
    // {
    //     const successMsg = document.getElementById("guestResumeSuccessMsg")
    //     successMsg.innerHTML = "";
    // })

}
else {
    console.log("guestResumeForm1 is undefined or null");
}



// // Using fetch API
// document.getElementById('invokeButton').addEventListener('click', function() {
//     fetch('/my-function/')
//         .then(response => response.json())
//         .then(data => {
//             console.log(data.message);
//             // Handle the response data as needed
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             // Handle errors
//         });
// });

document.getElementById('invokeButton').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    fetch('/my-function/', {
        method: 'POST',
        body: new FormData(document.getElementById('guestResumeForm1'))
    })
    .then(response => response.text())
    .then(data => {
        console.log(data); // Display the response from the server
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


// handle load img in purchase confirmation page
// tested
// 100% functional
// *****************************************************************************
window.onload = function() {
    //display loader on page load
    $(".loader").fadeOut("slow");
}
