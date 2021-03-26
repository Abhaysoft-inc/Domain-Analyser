import pyfiglet
import whois

banner = pyfiglet.print_figlet(text="Domain Name Information", font='big')
# banner = pyfiglet.print_figlet(text="----", font='big')

domain = input("[*] Enter the Domain: ")
print("[*] Searching for Domain Informations ")
print("")
print("=============== INFORMATION =============")
print("")
w = whois.query(domain)
print(" [#] Name : " + w.name)
print(" [#] Registrar : " + str(w.registrar))
print(" [#] Nameservers : " , w.name_servers)
print(" [#] Creation Date : " , w.creation_date)
print(" [#] Expiry Date : " , w.expiration_date)
print(" [#] Last Updated : " , w.last_updated)

print("")
print("Thanks For Using")
print("")
print("Made with Love By Abhay Vishwakarma")
# changing the banner doesn't makes you programmer
print("")
