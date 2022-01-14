#fltering log files with regular expression
import re
pattern= r"(\(\w+)\)"
line="(v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]"

result=re.search(pattern, line)
print(result)


def show_time_of_pid(line):
  pattern = r"Jul \d \d\d:\d\d:\d\d"
  result = re.search(pattern, line)
  
  pattern2 = r"\[(\d+)\]"
  result2 = re.search(pattern2, line)  
  results=f"{result[0]} pid:{result2[1]}"
  
  
  return(results)

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

#print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

#print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

#print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

#print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

#print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

#print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

#def checklog(address):
  #newline=[]
  #with open("Downloads//"+address)as fil:
    #for line in fil:
      #if "TRACE"not in line:
       # continue
      #patterns=r""
      #match=re.search(patterns,line)
      #print(f"{match[2]} : {match[1]}")
   # else:
      #match=re.search(patterns,line)
      #print(f"{match[1]}>>>>{match[3]}")

#checklog("sample.log")
    