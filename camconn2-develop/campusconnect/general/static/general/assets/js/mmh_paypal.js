console.log("mmh_paypal.js");

// Magic urlPath that point to specific Django Views.
// If the path to the view changes in the python url configuration these need to be changed as well.
const magicUrl_vpaypal_create           = "/rw/vpaypal/vcreate";
const magicUrl_vpaypal_capture          = "/rw/vpaypal/vcapture/";
const magicUrl_mmh_cartpurchasesuccess  = "/rw/cart/checkout/success/";


// Method duplicated in shopcartmow1.js
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

const csrftoken = get_cookie_value('csrftoken');


// status >>> "Payment Gateway loading failed" 
// *****************************************************************************
function showPaymentGatewayLoadingErrorMsg() {
    let ptst = document.getElementById("payment_gateway_loading_error_msg");
    ptst.removeAttribute("hidden");    
}


// status >>> "Payment Processing successful" 
// *****************************************************************************
function showPaymentProcessingSuccessMsg() {
    let ptst = document.getElementById("successful_payment_processing_status_msg");
    ptst.removeAttribute("hidden");    
}


// status >>> "Payment Processing Failed"
// *****************************************************************************
function showFailedPaymentProcessingStatus() {
    let ptst = document.getElementById("failed_payment_processing_status_msg");
    ptst.removeAttribute("hidden");    
}


// Check if PayPal exists
// *****************************************************************************
console.log('typeof(paypal) ->>>' + typeof(paypal));


// Initiate PayPal button is Payment gateway connection is successful
// *****************************************************************************
const isPaypalDefined = typeof paypal !== 'undefined';

if (isPaypalDefined) {
    console.log('PayPal loaded successfully');

    paypal.Buttons({

        // creates a paypal order
        createOrder: function(data, actions) {
          var orderID_new = data.orderID;
          return actions.order
            .create({
                purchase_units: [{
                    amount: {
                       value: document.getElementById('final_cost_26220').innerText,
                    },
                },],
                // applicaiton_context is added because we donot need shipping address
                application_context: {
                    shipping_preference: "NO_SHIPPING",
                },
            })
            .then((orderID_new) => {
              return orderID_new;
            });
        },

        
        // call to server to finalize the transaction
        onApprove: function(data, actions) {
            return fetch(magicUrl_vpaypal_capture+data.orderID, {
                method: 'post',
                headers: {"X-CSRFToken": csrftoken}
            }).then(function(res) {
                // console.log(res);
                return res.json();
            }).then(function(orderData) {

                console.log("Output of orderData >>>");
                console.log(orderData);

                // Three cases to handle:
                // CASE (1) Recoverable INSTRUMENT_DECLINED -> call actions.restart()
                // CASE (2) Other non-recoverable errors -> Show a failure message
                
                // console.log("mmh: orderData.icompletedpurchase_id: "+orderData.icompletedpurchase_id);
                // console.log("mmh: orderData.paypaltransaction_id: "+orderData.paypaltransaction_id);

                // CASE (3) Successful transaction -> Show a success / thank you message                
                // Show status >> payment processing successful
                showPaymentProcessingSuccessMsg();
                // Successful post purchase actions
                mmh_transactionCompletePerformHouskeeping();
                // redirect to magicUrl_mmh_cartpurchasesuccess
                window.location.replace(magicUrl_mmh_cartpurchasesuccess+orderData.paypaltransaction_id);


            });
        },


        onError: function(err) {
            console.log(err);
        }

    }).render('#mmh_paypal_button_container');
} else {
    console.log('Error with PayPal button');
    showPaymentGatewayLoadingErrorMsg();
}

