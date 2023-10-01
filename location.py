import phonenumbers
import opencage
from numb import number

from phonenumbers import geocoder
cnum = phonenumbers.parse(number)
location = geocoder.description_for_number(number,'en')
print(location)
