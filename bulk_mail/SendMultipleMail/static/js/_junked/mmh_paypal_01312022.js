console.log("mmh_paypal.js");

// Magic urlPath that point to specific Django Views.
// If the path to the view changes in the python url configuration these need to be changed as well.
const magicUrl_vpaypal_create = "/rw/vpaypal/vcreate";
const magicUrl_vpaypal_capture = "/rw/vpaypal/vcapture/";
const magicUrl_mmh_cartpurchasesuccess = "/rw/cart/checkout/success/";


// *****************************************************************************
// Method duplicated in shopcartmow1.js
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

const csrftoken = get_cookie_value('csrftoken');

// *****************************************************************************
paypal.Buttons({
          // Call your server to set up the transaction
          createOrder: function(data, actions) {
              return fetch(magicUrl_vpaypal_create, {
                  method: 'post',
                  headers: {"X-CSRFToken": csrftoken}
              }).then(function(res) {
                  return res.json();
              }).then(function(orderData) {
                  return orderData.id;
              });
          },

          // Call your server to finalize the transaction
          onApprove: function(data, actions) {
              return fetch(magicUrl_vpaypal_capture+data.orderID, {
                  method: 'post',
                  headers: {"X-CSRFToken": csrftoken}
              }).then(function(res) {
                  return res.json();
              }).then(function(orderData) {

                  // Three cases to handle:
                  //   (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
                  //   (2) Other non-recoverable errors -> Show a failure message
                  //   (3) Successful transaction -> Show a success / thank you message

                  // Your server defines the structure of 'orderData', which may differ
                  var errorDetail = Array.isArray(orderData.details) && orderData.details[0];

                  if (errorDetail && errorDetail.issue === 'INSTRUMENT_DECLINED') {
                      // Recoverable state, see: "Handle Funding Failures"
                      // https://developer.paypal.com/docs/checkout/integration-features/funding-failure/
                      return actions.restart();
                  }

                  if (errorDetail) {
                      var msg = 'Sorry, your transaction could not be processed.';
                      if (errorDetail.description) msg += '\n\n' + errorDetail.description;
                      if (orderData.debug_id) msg += ' (' + orderData.debug_id + ')';
                      // Show a failure message
                      return alert(msg);
                  }

                  // console.log("mmh: orderData.icompletedpurchase_id: "+orderData.icompletedpurchase_id);
                  // console.log("mmh: orderData.paypaltransaction_id: "+orderData.paypaltransaction_id);

                  mmh_transactionCompletePerformHouskeeping();

                  // redirect to magicUrl_mmh_cartpurchasesuccess
                  window.location.replace(magicUrl_mmh_cartpurchasesuccess+orderData.paypaltransaction_id);
              });
          }


      }).render('#mmh_paypal_button_container');



