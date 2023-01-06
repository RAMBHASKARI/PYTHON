#customer = {
#    "name" : 'SAIRAM BHASKARI',
#    "age": 18,
#    'is_verified': True
#}
#customer["birthdate"]="july 21st 2004"
#print(customer["birthdate"])


phone = (input('phone :'))
digits_mapping = {
    '1' : 'ONE',
    '2' : 'TOW',
    '3' : 'THREE',
    '4' : 'FOUR',
    '5' : 'FIVE',
    '6' : 'SIX',
    '7' : 'SEVEN',
    '8' : 'EIGHT',
    '9' : 'NINE'
}
output = ''
for ch in phone :
    output +=digits_mapping.get(ch,'!') + ''
    print(output)
