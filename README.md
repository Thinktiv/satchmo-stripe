# Satchmo Stripe
This is a django app to help with stripe integration and satchmo.

## To get working:

  * install using pip: pip install git+https://github.com/Thinktiv/satchmo-stripe.git
  * add `satchmo_stripe` to installed apps
  * mv stripe.js to root /template/js/stripe.js
  * call set_stripe_publish_key(<stripe_publish_key>) in the template where you include stripe.js

