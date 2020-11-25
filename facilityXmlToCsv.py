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

for facility in root.findall('T_Facility'):
  property_id = facility.find('Facility_ID').text
  account_number = facility.find('Facility_Account_Number').text
  name = facility.find('Facility_Name').text
  address1 = facility.find('Service_Address_Street_Name').text
  address2 = ''
  city = facility.find('Service_Address_City').text
  state_prov = facility.find('Service_Address_State').text
  country_code = 'US'
  postal_code = facility.find('Service_Address_Zip_Code').text
  primary_contact_id = facility.find('Facility_Contact_Mgr_ID').text
  notes = ''
  hazard_type = ''

  csv_writer.writerow([property_id, account_number, name, address1, address2, city, state_prov, country_code, postal_code, primary_contact_id, notes, hazard_type])

facility_data.close()




