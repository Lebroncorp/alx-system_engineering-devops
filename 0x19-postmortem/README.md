Postmortem
This following incident report for an isolated Ubuntu 14.04 container running an Apache Web Server on November 23, 2022. GET requests on the server led to 500 Internal Server Error when an HTML page was expected.

Issue Summary
From 2:14 PM to 4:36 PM CAT, requests to the Apache Web server resulted in 500 error response messages. All services that relied on this server also returned errors. At its peak, the issue affected 100% of traffic to this Server. The root cause of this error was an incorrectly typed file name(class-wp-locale.phpp) which was meant to be class-wp-locale.php.

Timeline (all times Central African Time)
2:14PM: Server Configuration
2:20PM: Error on request, noticed by engineer (I thought I would loose my job)
2:25PM: Engineer first checked running processes with ps aux
2:30PM: Confirmed that web server was serving content from /var/www/html/ folder
2:40PM: Ran strace on the PID of root Apache process while curling server on another instance
3:01PM: Ran starce on the PID of www-data process which showed where error origin
3:22PM: Looked through all files in /var/www/html/ to locate file containing error
3:44PM: Successful error debugging and application of changes by removing trailing p
3:55PM: Tested server by curling in another instance (My dream car is still secured :)
4:07PM: Server restarts begin
4:25PM: Wrote Puppet manifest to automate fixing the error.
4:36PM: 100% of traffic back online

Root Cause
At 2:14PM CAT, a configuration change was inadvertently released to our production environment without first being released to the testing environment. The change contained a typo with an incorrectly typed file name. The WordPress app was encountering a critical error in wp-settings.php when trying to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php. This lead to the 500 Internal Server Error received on request to the page.

Resolution and recovery
At 2:20 PM WAT, an engineer noticed the problem and quickly began debugging. By 3:44 PM, the bug was found and fixed. The processes running on the server was first checked. The strace (a very effective debugging tool) was used to trace out bugs in the process. At 3:22 PM, all files served by the web server was searched by matching pattern to try and locate the erroneous .phpp file extension. By 4:00 PM, server was confirmed to be serving the correct content

Corrective and Preventative Measures
In the last two days, we’ve conducted an internal review and analysis of the outage. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times: Test the application before deploying. The bug could have been fixed if the entire process had been tested. Improve process for auditing all high-risk configuration options. Add a faster rollback mechanism and improve the traffic ramp-up process, so any future problems of this type can be corrected quickly. Develop better mechanism for quickly delivering status notifications during incidents. A Puppet manifest was written to automate fixing of the error should it occur in the future.
