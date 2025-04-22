str = 'CPE-CPE009A-2025: 0.8475'

colon_pos = str.find(':')
extracted_str = str[colon_pos + 2:]
float_value = float(extracted_str)

print(float_value)
