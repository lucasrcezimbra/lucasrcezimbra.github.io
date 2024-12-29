---
title: Creating a WhatsApp bot
date: 2024-12-15
lastmod: 2024-12-29
---

## Requirements
- You will need a phone number that is not linked to WhatApp yet. "Your number
  must be used either on the Business Platform or on the Business App."
  ([source](https://developers.facebook.com/docs/whatsapp/cloud-api/get-started/migrate-existing-whatsapp-number-to-a-business-account))


## Steps
1. Create a [Facebook](https://www.facebook.com/) account
    - I didn't have an Facebook account. I created a new one, but didn't manage
      to use it to create a Meta Developer account. So, I had to create
      multiple accounts for one to work.
1. Create a [Meta Developer](https://developers.facebook.com/) account
1. Create a [business portfolio](https://business.facebook.com/)
1. Create a Facebook app
    1. Go to https://developers.facebook.com/apps/creation/
    1. Follow the steps. "Type" must be "Business" (and "Use cases" must be "Other")
1. Set up WhatsApp in your app
    1. Open your app - https://developers.facebook.com/apps/
    1. Look for WhatsApp under "Add products to your app"
    1. Click "Set up"
    1. Click "Start using the API"
    1. Adding your phone number
        1. Go to "Step 1: Select phone numbers" > "From"
        1. Click in the dropdown
        1. Click "Add phone number"
        1. Fill the fields and click next until you finish
        1. Save the "Phone number ID" for next steps. Use when you see `<PHONE_NUMBER_ID>` in this tutorial.
    1. Click "Generate access token"
        1. An pop up will open
        1. Click "Continue"
        1. Select "Opt in to current WhatsApp accounts only"
        1. Select your phone number
        1. Click "Continue"
        1. Click "Save"
        1. Save this token to the next steps. Use when you see `<ACCESS_TOKEN>` in this tutorial.
1. Add Payment method
    1. Open https://business.facebook.com/billing_hub/accounts/details/
    1. Select your Business portfolio
    1. Go to "Payment methods"
    1. Add business payment method
    1. Set as payment method as default
        1. Repeat steps 1, 2, and 3
        1. Go to the "Payment methods" you added, settings (three dots) and click "Set as default"
1. Set up Two-Step Verification (it will be required in the next step) ([docs](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/two-step-verification#updating-verification-code))
    1. Generate a 6-digit PIN (keep it safe). Use when you see `<PIN>` in this tutorial.
    ```shell
    curl -X  POST \
         'https://graph.facebook.com/v21.0/<PHONE_NUMBER_ID>' \
         -H 'Authorization: Bearer <ACCESS_TOKEN>' \
         -H 'Content-Type: application/json' \
         -d '{"pin" : "<PIN>"}'
    ```


### Optionals
- Adding WhatsApp profile info
    - Some info (like Profile photo) requires setting up the Two-Step Verification
    1. Go to https://business.facebook.com/latest/whatsapp_manager/phone_numbers/
    1. Select your WhatsApp account in the dropdown at the top right
    1. Click in your phone number
    1. Go to "Profile" and edit it.
