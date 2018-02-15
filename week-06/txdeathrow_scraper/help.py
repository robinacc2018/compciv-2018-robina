from scraper import get_inmate_data
from format_helper import calc_years_diff
from format_helper import txdate_to_iso

### This is more or less an integration test to
### spot-check the expected values given the specified DATA_SRC_URL
### (i.e. this is a very brittle test)
INMATE_DATA = get_inmate_data()

print (calc_years_diff(txdate_to_iso('11/30/1977'), txdate_to_iso('07/15/2015')))

