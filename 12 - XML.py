import xml.etree.ElementTree as ET
data = '''
<person>
    <users>
        <user x="1">
        <name>"Chuck"</name>
        <phone type = "intl"> +628116060 </phone>
        <email hide = "yes">aavellino@gmail.com</email>
        </user>
        <user x="2">
        <name>"Andrew"</name>
        <phone type = "intl"> +628116060 </phone>
        <email hide = "yes">chuck@gmail.com</email>
        </user>    
    </users>
</person>
'''
tree = ET.fromstring(data)
lst = tree.findall('users/user')

print("usercount = ",len(lst))

for item in lst:
    print('Name = ', item.find('name').text)
    print('Phone = ', item.find('phone').text)

# print dibawah dipake ketika hanya ada satu data
# print(tree.find('email').text)

# print(tree.find('email').get('hide'))