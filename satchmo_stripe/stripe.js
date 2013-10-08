$(document).ready(function(){

    function stripeResponseHandler(status, response){
        if(status === 200){
            // Success
            form = $("#stripe-payment-form").get(0);
            if(form){
                // Reset the form so that we don't send credit card info to our server
                // Set the token input and submit
                form.reset();
                $("#id_stripe_token").val(response['id']);
                $("#id_display_cc").val(response['card']['last4']);
                form.submit();
            }

        } else {
            // Stripe Error
            $("#stripe_error").append(response.error.message);
            $('input[type=submit]').attr('disabled', false);
        }
    }

    $("#stripe-payment-form").submit(function(event){
        $('input[type=submit]').attr("disabled", true);
        $("#stripe_error").html('');

        if($("#id_credit_number").length){
            Stripe.createToken({
                name: $('#id_name').val(),
                number: $('#id_credit_number').val(),
                cvc: $('#id_ccv').val(),
                exp_month: $('#id_month_expires').val(),
                exp_year: $('#id_year_expires').val()
            }, stripeResponseHandler);
            return false;
        } else {
            return false;
        }
    });
});

function set_stripe_publish_key(stripe_publish_key){
    // Call this Method to set stripe_publish_key from context
    Stripe.setPublishableKey(stripe_publish_key);
}