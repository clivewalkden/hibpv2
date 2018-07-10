# hibp
 
A command line interface for batch checking emails against HaveIBeenPwned or just checking a singular email.
This is a python script to verify multiple email addresses for pwnage. My version actually works, the original had a syntax error that wouldn't allow it to run.

Usage:  
  -h, --help   Shows this help message and exits  
  -a ADDRESS   Singular email address to be checked for pwnage  
  -f FILENAME  File to be checked with one email addresses per line  

 
Example output:  
[✓]info@example.com has not been breached.  
[X]example@example.com has been breached.  
  
#end of check it runs the breach info report  
  
Breach info for: example@example.com  
!------ Ticketfly ------!  
Breached data types:  
        Email addresses  
        Names  
        Phone numbers  
        Physical addresses  

  
[!] Rate limit exceeded, server instructed us to retry after 2 seconds  
    Refer to acceptable use of API: https://haveibeenpwned.com/API/v2#AcceptableUse  

[i] example@example.com has not been breached.  

This has been updated for the "HaveIBeenPwned?" API 2. This is a modified/working version of houbbit's python program that checks emails for pwnage using the HaveIBeenPwned? API.  

This is another updated version that fixed up JeffreyMustard's repor, included the ability to report on basic breach data information   
