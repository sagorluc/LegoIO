"use strict";
console.log("reading from myFunc/buttonOps.js");

// *****************************************************************************
// not functional
// not sure if want to use this func
function searchButtonState(button) {
    if (button.value === "") {
        document.getElementById("globalsearchbut").disabled = true;
    } else {
        document.getElementById("globalsearchbut").disabled = false;
    }
}



function hideForm(form) {
    console.log("trying to hide>>>"+form);
    form.style.display = "none";

}

function showForm(form) {
    console.log("trying to show>>>"+form);
    form.show();

}

export { searchButtonState, hideForm, showForm };

