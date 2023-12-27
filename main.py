# ---------------------------- Contact Pro ------------------------------- #

# ---------------------------- By Mustafa Abdullah ------------------------------- #

# ---------------------------- Constants ------------------------------- #
import codecs
check_two = 0
# ---------------------------- Convert Encoding from 'UTF-8' To 'windows-1256' ------------------------------- #
with codecs.open('input.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    with codecs.open('output_contacts.txt', 'w', encoding='windows-1256', errors="ignore") as file:
        file.write(content)
# ---------------------------- Processing Text file to VCF file ------------------------------- #
with open(file='output_contacts.txt') as contact:
    for _ in range(20):
        contact.readline(_)
    for item in contact:
        if '?' in item or '2022' in item or '2023' in item or '2021' in item or '?' in item or ':' in item :
            pass
        else:
            print(item.strip())
            if '+' not in item:
                if check_two >= 1:
                    with open(file='All_Contacts.vcf', mode='a', encoding='windows-1256') as name_to_add:
                        name_to_add.write(f"END:VCARD\n")
                check_two = 0
                with open(file='All_Contacts.vcf', mode='a') as name_to_add:
                    name_to_add.write('BEGIN:VCARD\nVERSION:2.1\n')
                    name_to_add.write(f"FN;CHARSET=windows-1256;ENCODING=QUOTED-PRINTABLE:{item.strip()}\n")
            elif '+' in item:
                check_two += 1
                with open(file='All_Contacts.vcf', mode='a') as name_to_add:
                    name_to_add.write(f"TEL;:{item.strip()}\n")
    with open(file='All_Contacts.vcf', mode='a') as name_to_add:
        name_to_add.write(f"END:VCARD\n")
# ---------------------------- END ------------------------------- #

# ---------------------------- By Mustafa Abdullah ------------------------------- #
