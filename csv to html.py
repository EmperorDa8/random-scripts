from prettytable import PrettyTable

#with open("C:\\Users\\USER\\error_message.csv","r")as csvfile:
    #csvf=csvfile.readlines()
    #lines=csvf[0]
    #newline=lines.split(",")
    #s=PrettyTable([newline[0],newline[1]])
    #for r in range(1,len(csvf)):
        #rr=csvf[r].split(",")
        #s.add_row([rr[0],rr[1]])
    #html_code=s.get_html_string()
    #html_file=open("C:\\Users\\USER\\html_script.html","w")
    #html_file=html_file.write(html_code)


with open("C:\\Users\\USER\\user_statistics.csv","r") as usercsv:
    us=usercsv.readlines()
    line=us[0]
    lines=line.split(",")
    D=PrettyTable([lines[0] ,lines[1] ,lines[2]])
    for e in range(1,len(us)):
        new=us[e].split(",")
        D.add_row([new[0],new[1],new[2]])
    stats_html_code=D.get_html_string()
    stats_file=open("C:\\Users\\USER\\user_statistics.html","w")
    stats_file=stats_file.write(stats_html_code)