# Can You LLM?

Compare LLM API prices of different vendors.


## Notes

### Architecture

- fastapi server + sqlite DB
- script to scrape websites and update DB via cron job
- htmx / astro webpage
- caddy / caprover


### Datamodel

Models 
- id
- name 
- size
- price_factor
- bench scores?


Vendors
- id
- url 
- name


Prices
- date 
- vendor_id
- model_id
- model_size
- price


