"use strict";
console.log("reading from myFunc/productComparison.js");


//// *****************************************************************************
//// Function to display corresponding product div
//// based on selection from dropdown menu
function fetch_comparison_body2(prod_name, search_div_id){
    console.log("fetch_comparison_body2() ----------------- start");
    console.log("product_selected: " + prod_name);
    console.log("search_div_id: " + search_div_id);

    var PRODUCT_SEARCH_DIV_NODE = document.getElementById(search_div_id);
    // console.log('PRODUCT_SEARCH_DIV_NODE: ' + PRODUCT_SEARCH_DIV_NODE);

    var PRODUCT_NODES = PRODUCT_SEARCH_DIV_NODE.getElementsByClassName("prod_comp_div")
    for (var loop1=0; loop1<PRODUCT_NODES.length; loop1++) {
      // console.log('loop1: ' + loop1);
      if (PRODUCT_NODES[loop1].id === prod_name) {
        PRODUCT_NODES[loop1].style.display = "block"
      }
      else {
        PRODUCT_NODES[loop1].style.display = "none"
      }
    }
    console.log("fetch_comparison_body2() ----------------- end");
}





export { fetch_comparison_body2 };
