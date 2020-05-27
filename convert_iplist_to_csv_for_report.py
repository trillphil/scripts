#!/usr/bin/env python3


def convert_to_csv(iplist):
    numips = len(iplist)
    csv = ""
    line = ""
    for i in range(1, numips + 1):
        if i % 4 == 0:
            # add a newline character, add the line to the csv, and reset the current line
            line += iplist[i-1] + "\n"
            csv += line
            line = ""

        else:
            line += iplist[i-1] + ','
            
            # if this is the last line, pad with '---' cells
            if i == numips:
                commas = line.count(',')
                if commas == 1:
                    line += "---,---,---" 
                elif commas == 2:
                    line += "---,---"
                elif commas == 3:
                    line += "---"

                csv += line

    print(csv)
        

def main():
    ip_list = []

    with open('/tmp/ip.txt', 'r') as iplist:
        for ip in iplist:
            ip_list.append(ip.strip('\n'))
    
    #print(ip_list)
    convert_to_csv(ip_list)



if __name__ == '__main__':
    main()
