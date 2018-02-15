from scraper import get_inmate_data

### This is more or less an integration test to
### spot-check the expected values given the specified DATA_SRC_URL
### (i.e. this is a very brittle test)
INMATE_DATA = get_inmate_data()