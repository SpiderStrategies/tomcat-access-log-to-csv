import sys
import re

f_name = sys.argv[1]
expression = r'(?P<ip>.*) \[(?P<date>.*) (?P<timezone>.*?)\] "(?P<request_method>.*) (?P<path>.*) (?P<request_version>HTTP/.*)" (?P<status_code>.*\d) (?P<size>.*) (?P<duration>.*) "(?P<user_agent>.*)" (?P<userid>.*) (?P<sessionid>.*)'
error_expression = r'(?P<ip>.*) \[(?P<date>.*) (?P<timezone>.*?)\] "(?P<path>.*)" (?P<status_code>.*\d) (?P<size>.*) (?P<duration>.*) "(?P<user_agent>.*)" (?P<userid>.*) (?P<sessionid>.*)'
compiled_regex = re.compile(expression)
error_compiled_regex = re.compile(error_expression)

newfile = open(f_name + ".csv","w")

fields = "ip,date,timezone,request_method,path,request_version,status_code,size,duration,user_agent,userid,sessionid"
newfile.write(fields + "\n")

def handleLine(regex, line):
    match = regex.match(l.strip())
    dict = match.groupdict()
    for field in fields.split(","):
        if(dict.has_key(field)):
            newfile.write("\"" + dict[field] + "\",")
        else:
            newfile.write("\" \",")
    newfile.write("\n")

with open(f_name) as f:
    for l in f:
        l = l.strip()
        try:
            handleLine(compiled_regex, l)
        except:
            print "Error processing line: " + l.strip()
            handleLine(error_compiled_regex, l)

newfile.close()