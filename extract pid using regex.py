import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]\W .[A-Z]*"
    result = re.search(regex, log_line)
    return result
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))
    #if result is None:
        #return None
    #return "{} ({})".format(result[2],result[1])

#print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
#print(extract_pid("99 elephants in a [cage]")) # None
#print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
#print(extract_pid("cc")) # 67890 (RUNNING)

def transform_record(record):
    new_record = re.sub(r",[\d]",r",+1-",record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer