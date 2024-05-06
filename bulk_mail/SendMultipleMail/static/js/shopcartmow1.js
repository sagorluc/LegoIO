'use strict';
console.log("reading from shopcartmow1");

// Magic urlPath that point to specific Django Views.
// If the path to the view changes in the python url configuration these need to be changed as well.
const magicAjaxUrl_Exp180DetailView_ajax                    = "/rw/ajax_detail/";   // APPENDED BY model_name / PRODUCT_ID

const magicAjaxUrl_rwCartAjaxView_contents                  = "/cart_ajax/contents";
const magicAjaxUrl_rwCartAjaxView_carticon                  = "/cart_ajax/carticon";
const magicAjaxUrl_rwCartAjaxView_emptycart                 = "/cart_ajax/emptycart";
const magicAjaxUrl_rwCartAjaxView_removebymodelnameandid    = "/cart_ajax/removebymodelnameandid";
const magicAjaxUrl_rwCartAjaxView_addproductver2            = "/cart_ajax/addproductver2";
const magicAjaxUrl_rwCartAjaxView_removeproductver2         = "/cart_ajax/removeproductver2";
// const magicAjaxUrl_rwCartAjaxView_applycoupontocart         = "/cart_ajax/applycoupontocart/";    // APPENDED BY coupon_32_string_value
// const magicAjaxUrl_rwCartAjaxView_unapplycoupontocart       = "/cart_ajax/unapplycoupontocart/";  // APPENDED BY coupon_32_string_value
// const magicAjaxUrl_rwCartAjaxView_applycoupon               = "/cart_ajax/applycoupon";

const productDOM = document.querySelector('.product');

// // -----------------------------------------------------------------------------
// // For testing only
// console.log("mmh: MANUALLY DELETING mmh_uniqid FROM LOCAL STORAGE");
// localStorage.removeItem('mmh_uniqid');   // clear item from local storage

// make completly uniqu userid for possible uses in the future.
// *****************************************************************************
function mmh_genUniqueID() {
  // console.log("mmh: mmh_genUniqueID()");
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}


// mmh: get users unique id from localStorage
// mmh: if not there generate and store it.
// *****************************************************************************
function mmh_getUsersUniqueId() {
  var temp_uniqueid = localStorage.getItem('mmh_uniqid');
  if (temp_uniqueid === null) {
    temp_uniqueid = mmh_genUniqueID();
    localStorage.setItem('mmh_uniqid', temp_uniqueid);
    console.log("mmh: generated new temp_uniqueid = " + temp_uniqueid);
  }
  // console.log("mmh: mmh_getUsersUniqueId(): " + temp_uniqueid);
  return temp_uniqueid
}


// Method duplicated in mmh_paypal.js
// *****************************************************************************
function get_cookie_value(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// *****************************************************************************
function mmh_setUsersUniqueCookie() {
  var mmh_cook = get_cookie_value('mmh_uniqid_cookie');
  // Only set new cookie if old cookie doesn't exist
  // console.log("mmh_cook = " + mmh_cook);
  if (mmh_cook === null) {
    var mmh_uniqid_cookie_value = mmh_getUsersUniqueId();
    document.cookie = "mmh_uniqid_cookie=" + mmh_uniqid_cookie_value + "; SameSite=Strict; expires=Fri, 31 Dec 9999 23:59:59 GMT";
    console.log("mmh_setUsersUniqueCookie(): " + mmh_uniqid_cookie_value)
  }
}

mmh_setUsersUniqueCookie();

// *****************************************************************************
// mmh: EventListener that will wait until HTML/DOM elements are ready and then
// call mmh_updateMyCartIconItemCount()
document.addEventListener('readystatechange', event => {
    if (event.target.readyState === "interactive") {
        mmh_updateMyCartIconItemCount();
    }
});

// *****************************************************************************
function mmh_updateMyCartIconItemCount() {
  // console.log("mmh: mmh_updateMyCartIconItemCount()");
  mmh_replaceElementWithIdWithHtmlFromUrl("mmh_cart_icon_id", magicAjaxUrl_rwCartAjaxView_carticon);
}

// *****************************************************************************
function mmh_updateProductDetailsDom(product_id, model_name) {
  var product_id = productDOM.querySelector('.product__id').innerText;
  var model_name = productDOM.querySelector('.product__model_name').innerText;
  // console.log("mmh: mmh_updateProductDetailsDom(): product_id = " + product_id + ", model_name = " + model_name);

  // final url = magic url + model_name \ PRODUCT_ID
  var final_url = magicAjaxUrl_Exp180DetailView_ajax + model_name + "/" + product_id
  console.log("mmh: mmh_updateProductDetailsDom(): final_url = " + final_url);
  mmh_replaceElementWithIdWithHtmlFromUrl("mmh_product_details_id", final_url);
}

// *****************************************************************************
// Find element with given id.
// Replace innerHTML of that element with data retrieved from url via AJAX call.
// mmh_uniqid passed to url as it is required for this use and the document cookie with this data wasn't being retrieved correctly in ajax call. FIX PROBABLE
function mmh_replaceElementWithIdWithHtmlFromUrl(id, url) {
  console.log("mmh: mmh_replaceElementWithIdWithHtmlFromUrl(): id = " + id + ", url = " + url);
  // console.log("value of id from line114>>>"+id);
  var element = document.getElementById(id);
  // console.log("value of element from line115>>>"+element)
  var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
  $.ajax({
      type: "GET",
      url: url,
      dataType: "html",
      data: {
        mmh_guest_user_unique_id: mmh_guest_user_unique_id,
        csrfmiddlewaretoken: '{{ csrf_token }}',
      },
      success: function(data) {
          var data_dict = JSON.parse(data);
          element.innerHTML = data_dict.html;
      },
      error: function(e) {
          alert('Error: ' + e);
      },
      async: false   // make this request syncronous
  });
}


// // *****************************************************************************
// // Find element with given id.
// // Replace innerHTML of that element with data retrieved from url via AJAX call.
// // THIS IS THE POST VERSION WHICH MUST DO SOME MAGIC TO PRESERVE csrfTokens
// // MMH: NOT FINISHED, NOT NEEDED, NOT TESTED, NOT GUARANTEED TO WORK
// // MMH: NOT FINISHED, NOT NEEDED, NOT TESTED, NOT GUARANTEED TO WORK
// // MMH: NOT FINISHED, NOT NEEDED, NOT TESTED, NOT GUARANTEED TO WORK
// // MMH: NOT FINISHED, NOT NEEDED, NOT TESTED, NOT GUARANTEED TO WORK
// function mmh_replaceElementWithIdWithHtmlFromUrl_POST_VERSION(id, url) {
//   console.log("mmh: mmh_replaceElementWithIdWithHtmlFromUrl_POST_VERSION(): id = " + id + ", url = " + url);
//   var element = document.getElementById(id);
//   var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
//
//   // Get and preserve existing csrfToken
//
//   // var token = $('input[name="csrfToken"]').attr('value')
//   // $.ajaxSetup({
//   //   beforeSend: function(xhr) {
//   //     xhr.setRequestHeader('Csrf-Token', token);
//   //   }
//   // });
//
//   // var token = document.getElementsByName("csrfToken").value;
//   var token = document.getElementsByName("X-CSRFToken").value;
//   console.log("token = " + token);
//
//
//   $.ajax({
//       type: "POST",
//       url: url,
//       dataType: "html",
//       headers: {'X-CSRFToken': token},
//       data: {
//         mmh_guest_user_unique_id: mmh_guest_user_unique_id,
//         // csrfmiddlewaretoken: '{{ csrf_token }}',
//       },
//       success: function(data) {
//           var data_dict = JSON.parse(data);
//           element.innerHTML = data_dict.html;
//       },
//       error: function(e) {
//           alert('Error: ' + e);
//       },
//       async: false   // make this request syncronous
//   });
// }

// *****************************************************************************
function mmh_refreshCartHomeDom() {
  console.log("mmh: mmh_refreshCartHomeDom():");
  mmh_replaceElementWithIdWithHtmlFromUrl("mmh_shopping_cart_contents", magicAjaxUrl_rwCartAjaxView_contents);
  mmh_updateMyCartIconItemCount();
}

// // *****************************************************************************
// function mmh_refreshCartHomeDom_POST_METHOD() {
//   console.log("mmh: mmh_refreshCartHomeDom_POST_METHOD():");
//   mmh_replaceElementWithIdWithHtmlFromUrl_POST_VERSION("mmh_shopping_cart_contents", magicAjaxUrl_rwCartAjaxView_contents);
//   mmh_updateMyCartIconItemCount();
// }

// *****************************************************************************
function mmh_removeItemFromCartByModelNameAndId(model_name, id) {
  console.log("mmh: mmh_removeItemFromCartByModelNameAndId(): model_name = " + model_name);
  console.log("mmh: mmh_removeItemFromCartByModelNameAndId(): id = " + id);

  var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
  //  SYNCRONOUS AJAX CALL TO REMOVE THIS FROM MCART
  // Calls rw_cart_views.rwCartAjaxView_removebymodelnameandid()
  $.ajax({
    type: "POST",
    url: magicAjaxUrl_rwCartAjaxView_removebymodelnameandid,
    data: {
      mmh_guest_user_unique_id: mmh_guest_user_unique_id,
      model_name: model_name,
      id: id,
      csrfmiddlewaretoken: '{{ csrf_token }}',
    },
    success:function(response) {
      console.log("mmh: mmh_removeItemFromCartByModelNameAndId ajax completed()");
    },
    async: false   // make this request syncronous
  });
}

// *****************************************************************************
function mmh_removeItemFromCartByModelNameAndId_andRefreshCartHomeDom(model_name, id) {
  console.log("mmh: mmh_removeItemFromCartByModelNameAndId_andRefreshCartHomeDom(): model_name = " + model_name);
  console.log("mmh: mmh_removeItemFromCartByModelNameAndId_andRefreshCartHomeDom(): id = " + id);
  mmh_removeItemFromCartByModelNameAndId(model_name, id)
  mmh_refreshCartHomeDom()
}

// *****************************************************************************
function mmh_removeAllItemsFromCart() {
  var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
  //  SYNCRONOUS AJAX CALL TO REMOVE ALL ITEMS FROM CART
  // Calls rw_cart_views.rwCartAjaxView_emptycart()
  $.ajax({
    type: "POST",
    url: magicAjaxUrl_rwCartAjaxView_emptycart,
    data: {
      mmh_guest_user_unique_id: mmh_guest_user_unique_id,
      csrfmiddlewaretoken: '{{ csrf_token }}',
    },
    success:function(response) {
      console.log("mmh: mmh_removeAllItemsFromCart ajax completed()");
    },
    async: false   // make this request syncronous
  });
}

// *****************************************************************************
function mmh_removeAllItemsFromCart_andRefreshCartHomeDom() {
  console.log("mmh: mmh_removeAllItemsFromCart_andRefreshCartHomeDom():");
  mmh_removeAllItemsFromCart()
  mmh_refreshCartHomeDom()
}

// *****************************************************************************
function getProductFromDOM_newVersion(){
  // console.log("mmh: getProductFromDOM_newVersion()");

  const product = {
    id:               productDOM.querySelector('.product__id').innerText,
    model_name:       productDOM.querySelector('.product__model_name').innerText,
    serviceoptions:   mmh_getCheckedOptionsIdArray_byInputName('option'),
    deliveryoption:   mmh_getCheckedOptionsIdArray_byInputName('delivery_option'),
    quantity:         1,
  };

  if (product["model_name"] === "") {
    alert("MMH: product[model_name] is null. Must supply a model_name in DOM")
  }
  return product;
}

// *****************************************************************************
function mmh_getCheckedOptionsIdArray_byInputName(name) {
  // console.log("mmh: mmh_getCheckedOptionsIdArray_byInputName(" + name  + ")");
  var returnArray = [];
  const checkedItems_array = document.querySelectorAll(`input[name="${name}"]:checked`);
  for (var i = 0; i<(checkedItems_array.length); i++){
      var checkedItemId = checkedItems_array[i].id
      // console.log("mmh: checkedItem for " + name + ": id = " + checkedItemId );
      returnArray.push(checkedItemId)
  }
  return returnArray;
}

// *****************************************************************************
function mmh_removeProductFromCart_andUpdateDom() {
  var product_id = productDOM.querySelector('.product__id').innerText;
  var model_name = productDOM.querySelector('.product__model_name').innerText;
  console.log("mmh: *********************************************************");
  console.log("mmh: mmh_removeProductFromCart_andUpdateDom(): product_id = " + product_id + ", model_name = " + model_name);

  var product_ver2 = getProductFromDOM_newVersion();
  mmh_removeProductVer2FromMcart(product_ver2);
  mmh_updateProductDetailsDom(product_id, model_name);
  mmh_updateMyCartIconItemCount();
}

// *****************************************************************************
function mmh_addProductToCart_andUpdateDom() {
  var product_id = productDOM.querySelector('.product__id').innerText;
  var model_name = productDOM.querySelector('.product__model_name').innerText;
  console.log("mmh: *********************************************************");
  console.log("mmh: mmh_addProductToCart_andUpdateDom(): product_id = " + product_id + ", model_name = " + model_name);

  var product_ver2 = getProductFromDOM_newVersion();
  mmh_addProductVer2ToMcart(product_ver2);
  mmh_updateProductDetailsDom(product_id, model_name);
  mmh_updateMyCartIconItemCount();
}

// *****************************************************************************
function mmh_addProductVer2ToMcart(product_ver2) {
  var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
  $.ajax({
    type: "POST",
    url: magicAjaxUrl_rwCartAjaxView_addproductver2,
    data: {
      mmh_guest_user_unique_id: mmh_guest_user_unique_id,
      product_ver2: [JSON.stringify(product_ver2)],
      csrfmiddlewaretoken: '{{ csrf_token }}',
    },
    success:function(response) {
      console.log("mmh: mmh_addProductVer2ToMcart ajax completed()");
    },
    async: false   // make this request syncronous
  });
}

// *****************************************************************************
function mmh_removeProductVer2FromMcart(product_ver2) {
  var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
  $.ajax({
    type: "POST",
    url: magicAjaxUrl_rwCartAjaxView_removeproductver2,
    data: {
      mmh_guest_user_unique_id: mmh_guest_user_unique_id,
      product_ver2: [JSON.stringify(product_ver2)],
      csrfmiddlewaretoken: '{{ csrf_token }}',
    },
    success:function(response) {
      console.log("mmh: mmh_removeProductVer2FromMcart ajax completed()");
    },
    async: false   // make this request syncronous
  });
}

// *****************************************************************************
// MMH CONSIDER MOVING THIS TO mmh_paypal.js
// MMH CONSIDER MOVING THIS TO mmh_paypal.js
// MMH CONSIDER MOVING THIS TO mmh_paypal.js
function mmh_transactionCompletePerformHouskeeping(){
  console.log("mmh: mmh_transactionCompletePerformHouskeeping()");

  // // Below not needed any more as it is now done with vpaypal_markItemsInCartAsPurchased
  // // mmh_fromLocalStorageUpdateDbTable_mcart_purchasedItems()
  //
  // console.log("mmh: clear cart of p urchased items.");
  // localStorage.removeItem('cart')
  // // mmh_enableOrDisableProductDetailHtmlElementsBasedOnCartLocalStorageContents();

  // mmh_removeProductVer2FromMcart(product_ver2);
  // mmh_updateProductDetailsDom(product_id, model_name);
  mmh_updateMyCartIconItemCount();

  // MMH: REVIEW WHAT CLEANUP HAS TO BE DONE HERE.
  // MMH: THIS METHOD ONLY CALLED BY mmh_paypal WHEN TRANSACTION APPROVED.
  // MMH: SO THIS IS IN CART PAYMENT SCREEN
  // MMH: ALSO ALL THE ITEMS HAVE ALREADY BEEN MARKED AS PURCHASED.
}



// // *****************************************************************************
// function mmh_applyCouponToCart(coupon_random_string_32) {
//   var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
//   // SYNCRONOUS AJAX CALL TO APPLY COUPON TO CART
//   // Calls rw_cart_views.rwCartAjaxView_applycoupontocart()
//
//   var final_url = magicAjaxUrl_rwCartAjaxView_applycoupontocart + coupon_random_string_32
//   $.ajax({
//     type: "POST",
//     url: final_url,
//     data: {
//       mmh_guest_user_unique_id: mmh_guest_user_unique_id,
//       csrfmiddlewaretoken: '{{ csrf_token }}',
//     },
//     success:function(response) {
//       console.log("mmh: mmh_applyCouponToCart ajax completed()");
//     },
//     async: false   // make this request syncronous
//   });
// }
//
// // *****************************************************************************
// function mmh_applyCouponToCart_andUpdateDom(coupon_random_string_32) {
//   console.log("mmh: mmh_applyCouponToCart_andUpdateDom(): "+coupon_random_string_32);
//   mmh_applyCouponToCart(coupon_random_string_32)
//   mmh_refreshCartHomeDom()
// }
//
//
// // *****************************************************************************
// function mmh_unApplyCouponToCart(coupon_random_string_32) {
//   var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
//   // SYNCRONOUS AJAX CALL TO UN APPLY COUPON TO CART
//   // Calls rw_cart_views.rwCartAjaxView_unapplycoupontocart()
//
//   var final_url = magicAjaxUrl_rwCartAjaxView_unapplycoupontocart + coupon_random_string_32
//   $.ajax({
//     type: "POST",
//     url: final_url,
//     data: {
//       mmh_guest_user_unique_id: mmh_guest_user_unique_id,
//       csrfmiddlewaretoken: '{{ csrf_token }}',
//     },
//     success:function(response) {
//       console.log("mmh: mmh_unApplyCouponToCart ajax completed()");
//     },
//     async: false   // make this request syncronous
//   });
// }
//
// // *****************************************************************************
// function mmh_unapplyCouponToCart_andUpdateDom(coupon_random_string_32) {
//   console.log("mmh: mmh_unapplyCouponToCart_andUpdateDom(): "+coupon_random_string_32);
//   mmh_unApplyCouponToCart(coupon_random_string_32)
//   mmh_refreshCartHomeDom()
// }


// // *****************************************************************************
// function mmh_applyCoupon() {
//   var mmh_guest_user_unique_id = mmh_getUsersUniqueId();
//   // SYNCRONOUS AJAX CALL TO APPLY COUPON TO CART
//   // Calls rw_cart_views.rwCartAjaxView_applycoupon()
//
//   $.ajax({
//     type: "POST",
//     // url: magicAjaxUrl_rwCartAjaxView_applycoupon,
//     url: magicAjaxUrl_rwCartAjaxView_contents,
//     data: {
//       mmh_guest_user_unique_id: mmh_guest_user_unique_id,
//       csrfmiddlewaretoken: '{{ csrf_token }}',
//     },
//     success:function(response) {
//       console.log("mmh: mmh_applyCoupon ajax completed()");
//     },
//     async: false   // make this request syncronous
//   });
// }

// // *****************************************************************************
// function mmh_applyCoupon_andUpdateDom() {
//   console.log("mmh: mmh_applyCoupon_andUpdateDom()");
//   // mmh_applyCoupon()
//   mmh_refreshCartHomeDom_POST_METHOD()
// }




