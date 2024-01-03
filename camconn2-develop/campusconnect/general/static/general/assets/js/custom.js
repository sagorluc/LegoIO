import { fileValidationFileType3 }  from "./myFunc/FileValidation.js";
import { fetch_comparison_body2 }   from "./myFunc/productComparison.js";
import { checkForEmptySearchInput } from "./myFunc/searchBar.js";
import { hideForm, showForm }       from "./myFunc/buttonOps.js";


"use strict";
console.log(" reading from custom.js");


// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// 100% functional code below
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************


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



// *****************************************************************************
// guest resume upload validation
// tested
// 100% functional
const guestResumeForm1 = document.getElementById("guestResumeForm1");
if (guestResumeForm1 !== undefined && guestResumeForm1 !== null) {
    console.log("value of guestResumeForm1 from line#70"+guestResumeForm1.value);
    console.log("element exists>>>guestResumeForm1");

    // select tile field from the form
    var fileUploadField0 = document.getElementById("id_file1");

    var emailField = document.getElementById("id_email");
    console.log(emailField.value);

    // invoke the function to check file type
    fileUploadField0.addEventListener("change", function() {
        var fileName226 = fileUploadField0.files[0].name;
        fileValidationFileType3(fileName226, guestResumeForm1);
    });
    

    // Show Modal on form Submit
    guestResumeForm1.addEventListener("submit", function(event) {
        event.preventDefault();

        // Send form data to the server using Fetch API
        fetch('', {
            method: 'POST',
            body: new FormData(guestResumeForm1)
        })
        .then(function(response) {
            if (response.ok) {
                $("#guestResumeSuccessMsg").append("You have been sent an email to " + emailField.value);
                $('#successModal-guestForm').modal('show');
                $("#guestResumeSuccessMsg").remove();
                guestResumeForm1.reset();
            } else {
                $('#failedModal-guestForm').modal('show');
                console.log('Form submission failed');
            }
        })
        .catch(function(error) {
            console.log(error);
        });
    
    });

    // Clear modal email message
    const closeButton = document.getElementById("successModalClose");
    closeButton.addEventListener("click", function()
    {
        const successMsg = document.getElementById("guestResumeSuccessMsg")
        successMsg.innerHTML = "";
    })

}
else {
    console.log("guestResumeForm1 is undefined or null");
}



// SHOPCART 
// file upload validation
// tested, 100% functional
// *****************************************************************************
const cartFileUploadForm = document.getElementById("form_cart_file_upload72");
if (cartFileUploadForm !== undefined && cartFileUploadForm !== null) {
    console.log("value of cartFileUploadForm from line#70"+cartFileUploadForm.value);
    console.log("element exists>>>cartFileUploadForm");


    // select tile field from the form
    var fileUploadField12 = document.getElementById("id_document");

    // for testing purpose, print the filename
    fileUploadField12.addEventListener("change", function() {
        var fileName231 = fileUploadField12.files[0].name;
        console.log("line57>>>fileName231>>>"+fileName231);
    });

    // invoke the function to check file type
    fileUploadField12.addEventListener("change", function() {
        var fileName276 = fileUploadField12.files[0].name;
        fileValidationFileType3(fileName276, cartFileUploadForm);
    });


}


// product comparison 
// ajax call
// tested
// 100% functional
// ************************************************************************
var product_selected = document.getElementById("base_product_for_prod_comp");
if (typeof(product_selected) !== undefined && product_selected !== null) {
    var prod_name = product_selected.innerText;
    // product_selected = product_selected.toLowerCase();
    if (prod_name.length) {
        console.log("output from lin148"+prod_name);

        $.ajax({
            type: "GET",
            url: "/rw/service/" + prod_name + "/product-comparison",
            data: {
                "product": prod_name
            },

            success: function(response) {
                // console.log(response);
                // show corresponding prod-comparison body inside
                // this div >>> 'prod_fixed_section'
                fetch_comparison_body2(prod_name, "prod_fixed_section");

            },

            error: function(xhr, status, error) {
                alert(error);
            }


        });
    }
    else {
        console.log("prod_name.length not found");
    }

}


// product comparison
// tested
// 100% functional
// ************************************************************************
$(document).on("change", "#id_prod_other_code", function(){
    // console.log('(document).onchange: ==== START');
    var token = $("input[name=csrfmiddlewaretoken]").val();
    var prod  = $("select[name=prod_other_code]").val();
    // console.log('token: ' + token);
    // console.log('prod: ' + prod);

    if (prod.length) {
        console.log("prod selected from prod_other_code>>>" + prod);
        // show corresponding prod-comparison body inside
        // this div >>> 'prod_fixed_section'
        fetch_comparison_body2(prod, "prod_var_section")

    }
    // console.log('(document).onchange: ===== END');
});


// *****************************************************************************
// handle load img in purchase confirmation page
// tested
// 100% functional
window.onload = function() {
    //display loader on page load
    $(".loader").fadeOut("slow");
}



