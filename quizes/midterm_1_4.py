def convert_m_to_hm(minutes):
    remainder = minutes % 60
    hours = (minutes - remainder) / 60
    list = [int(hours), remainder]
    return list


minutes = int(input('Enter minutes: '))
print(convert_m_to_hm(minutes))