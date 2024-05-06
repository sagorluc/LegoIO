"use strict";
console.log("reading from myFunc/searchBar.js");



function checkForEmptySearchInput(e) {
    console.log("checkForEmptySearchInput");

    var x = document.forms["searchForm001"]["query"].value;
    // console.log(x.replace(/\s/g, '').length);

    if (!x.replace(/\s/g, '').length || x == null) {
        console.log("Product Search input is empty")
    
        // alert("Search input cannot be empty");

        // TODO: replace the alert window with a modal
        $('#error-modal-108').modal('show');

        e.preventDefault();
        // return false;
    }
    else {
        console.log(x)
    }
}



export { checkForEmptySearchInput };
