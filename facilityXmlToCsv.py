import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse("Facility.xml")
root = tree.getroot()

# Create the CSV file for transformed data
facility_data = open('facility_properties.csv', 'w',newline='', encoding='utf-8')
csv_writer = csv.writer(facility_data)

# Create the header row
csv_writer.writerow(['property_id', 'account_number', 'name', 'address1', 'address2', 'city', 'state_prov', 'country_code', 'postal_code', 'primary_contact_id', 'notes', 'addl:Hazard Type'])

# Helper function to check whether property is nil
def getPropertyText(facility, property_name):
  prop = facility.find(property_name)
  if prop != None:
    return prop.text
  return ''

# Iterate over facilities and create rows in new CSV file
for facility in root.findall('T_Facility'):
  property_id = getPropertyText(facility, 'Facility_ID')
  account_number = getPropertyText(facility, 'Facility_Account_Number')
  name = getPropertyText(facility, 'Facility_Name')
  address1 = getPropertyText(facility, 'Service_Address_Street_Name')
  address2 = ''
  city = getPropertyText(facility, 'Service_Address_City')
  state_prov = getPropertyText(facility, 'Service_Address_State')
  country_code = 'US'
  postal_code = getPropertyText(facility, 'Service_Address_Zip_Code')
  primary_contact_id = getPropertyText(facility, 'Facility_Contact_Mgr_ID')
  notes = ''
  hazard_type = ''

  csv_writer.writerow([property_id, account_number, name, address1, address2, city, state_prov, country_code, postal_code, primary_contact_id, notes, hazard_type])

facility_data.close()
