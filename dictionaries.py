monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
month=input("Input the first 3 letters of a month: ")
# print(monthConversions[month])
print(monthConversions.get(month,"Invalid Month"))