import xml.etree.ElementTree as ET

root = ET.Element("Ganshyam_Das_Goyal")
First_Family_Element = ET.SubElement(root, "Family_One")
ET.SubElement(First_Family_Element, "name_one").text = "Tau"
ET.SubElement(First_Family_Element, "name_two").text = "Tai"
ET.SubElement(First_Family_Element, "name_three").text = "Nisha"
ET.SubElement(First_Family_Element, "name_four").text = "Bunty"
ET.SubElement(First_Family_Element, "name_five").text = "Golu"

Second_Family_Element = ET.SubElement(root, "Family_Two")
ET.SubElement(Second_Family_Element, "name_one").text = "Papa"
ET.SubElement(Second_Family_Element, "name_two").text = "Mummy"
ET.SubElement(Second_Family_Element, "name_three").text = "Chiki"
ET.SubElement(Second_Family_Element, "name_four").text = "Shipra"
ET.SubElement(Second_Family_Element, "name_five").text = "Rocky"
tree = ET.ElementTree(root)
tree.write("Goyal.xml")

# Read XML file

tree = ET.parse("Goyal.xml")
root = tree.getroot()
print(type(root))

for family in root:
    print(family.find("name_one").text)
