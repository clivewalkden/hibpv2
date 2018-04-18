# hibp
 
A command line interface for batch checking emails against HaveIBeenPwned or just checking a singular email.
This is a python script to verify multiple email addresses for pwnage. My version actually works, the original had a syntax error that wouldn't allow it to run.

Usage:
  -h, --help   Shows this help message and exits
  -a ADDRESS   Singular email address to be checked for pwnage
  -f FILENAME  File to be checked with one email addresses per line

 
Example output:

[i] info@example.com has not been breached.

[!] lastfm@example.com has been breached!

[!] Rate limit exceeded, server instructed us to retry after 2 seconds
    Refer to acceptable use of API: https://haveibeenpwned.com/API/v2#AcceptableUse

[i] example@example.com has not been breached.

This has been updated for the "HaveIBeenPwned?" API 2. This is a modified/working version of houbbit's python program that checks emails for pwnage using the HaveIBeenPwned? API.
