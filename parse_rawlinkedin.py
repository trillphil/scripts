#!/usr/bin/env python3
import argparse

def parse_names(contents):
    """ Parses names from contents of a file containing LinkedIn employee search results
    """
    names = []
    for line in contents.split('\n'):
        if "3rd degree connection3rd" in line or "2nd degree connection2nd" in line:
            name = line.split("  ")[0].lower()
            if name != "LinkedIn Member":
                names.append(name)
    return names


def generate_email_addresses(names, domain, email_format):
    """ Generates email addresses based on parsed names, target domain, and format """
    emails = []
    for name in names:
        name_list = name.split(' ')
        
        # if just first last, we gucci
        if len(name_list) == 2:
            name_list = name_list

        elif len(name_list) >= 3:
            # get rid of anything after a comma
            if name_list[1][-1] == ",":
                name_list = [name_list[0], name_list[1][:-1]]
            else:
                name_list = [name_list[0], name_list[1]]

        # if last name is hypenated, assume its the second one
        if '-' in name_list[1]:
            name_list = [name_list[0], name_list[1].split('-')[1]]

        # create email addresses based on assumed format
        if email_format == "flast":
            email = f"{name_list[0][0]}{name_list[1]}@{domain}"
            emails.append(email)
        elif email_format == "lastf":
            email = f"{name_list[1]}{name_list[0][0]}@{domain}"
            emails.append(email)
        elif email_format == "first.last":
            email = f"{name_list[0]}.{name_list[1]}@{domain}"
            emails.append(email)
        elif email_format == "last.first":
            email = f"{name_list[1]}.{name_list[0]}@{domain}"
            emails.append(email)
    return emails


def print_string_list(string_list):
    """ Print every string in a list """
    for item in string_list:
        print(item)


def write_string_list_to_file(string_list, filepath):
    """ Writes every string in a list to a newline separated file"""
    with open(filepath, 'w') as outfile:
        outfile.writelines(f"{string}\n" for string in string_list)

    print(f"[+] Results written to {filepath}")


def count_email_addresses(email_addresses):
    """ Displays the number of email addresses found """
    print(f"\n[+] {len(email_addresses)} email addresses generated")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        "-p",
                        help = "path to file containing copied LinkedIn search data",
                        default = "/root/temp.txt")
    parser.add_argument("--email_domain",
                        "-d",
                        help = "domain for email",
                        default = "example.com")
    parser.add_argument("--email_format",
                        "-f",
                        help = "format for email addresses",
                        type = str,
                        choices = {"flast", "lastf", "first.last", "last.first"},
                        default = "flast")
    parser.add_argument("--outfile",
                        "-o",
                        help = "file to output results to")
    parser.add_argument("--verbose",
                        "-v",
                        help = "prints additional output",
                        action="store_true")

    args = parser.parse_args()
    

    with open(args.path, 'r') as tempfile:
        file_contents = tempfile.read()

    names = parse_names(file_contents)
    emails = generate_email_addresses(names, args.email_domain, args.email_format)
    
    count_email_addresses(emails)

    if args.outfile != None:
        write_string_list_to_file(emails, args.outfile)
        if args.verbose:
            print_string_list(emails)  
    else:
        print_string_list(emails)
    

if __name__ == '__main__':
    main()

