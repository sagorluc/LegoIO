
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// *****************************************************************************
// not sure the use of this block
var value49 = document.getElementById("final_cost_26220");
if (value49 !== undefined && value49 !== null) {
    console.log(value49);
    console.log(typeof(value49));

}




// *****************************************************************************
//// handle global search form
//// remove global search form when screen size is less than 992px
//// need to change this logic as it has many limitations
var current_screen_size = get_current_screen_size();
if (current_screen_size <= 992) {
    // const gsearchform = document.getElementById('global-search-form91');
    // gsearchform.style.display = 'none !important';
    $("#global-search-form91").attr("style", "display:none !important")
}





// *****************************************************************************
// not sure if i need this block
$(document).ready(function() {
    console.log("im from custom.js line67");
});


// *****************************************************************************
function get_current_screen_size() {
    return $(window).width();
}



