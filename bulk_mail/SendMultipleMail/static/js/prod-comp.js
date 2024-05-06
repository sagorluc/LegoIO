import { checkFileType, checkFileSize, FileuploadSuccess }  from "./myFunc/FileValidation.js";
import { fetch_comparison_body2 }   from "./myFunc/productComparison.js";
import { checkForEmptySearchInput } from "./myFunc/searchBar.js";
import { hideForm, showForm }       from "./myFunc/buttonOps.js";


"use strict";
console.log(" reading from prod-comp.js");


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
            url: "/rw/service/" + prod_name + "/service-comparison",
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
        console.log("prod_name.length not found>>>265568");
    }

}


$(document).on("change", "#id_prod_other_code", function(){
    // console.log('(document).onchange: ==== START');
    var token = $("input[name=csrfmiddlewaretoken]").val();
    var prod  = $("select[name=prod_other_code]").val();
    // console.log('token: ' + token);
    console.log('prod: ' + prod);

    if (prod.length) {
        console.log("prod selected from prod_other_code>>>" + prod);
        // show corresponding prod-comparison body inside
        // this div >>> 'prod_fixed_section'
        fetch_comparison_body2(prod, "prod_var_section")

    }
    // console.log('(document).onchange: ===== END');
});

