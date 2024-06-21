 0x0C. Web server
DevOpsSysAdmin

Resources

Read or watch:

    How the web works
    Nginx
    How to Configure Nginx
    Child process concept page
    Root and sub domain
    HTTP requests
    HTTP redirection
    Not found HTTP response code
    Logs files on Linux

For reference:

    RFC 7231 (HTTP/1.1)
    RFC 7540 (HTTP/2)

General

    What is the main role of a web server
    What is a child process
    Why web servers usually have a parent process and child processes
    What are the main HTTP requests

DNS

    What DNS stands for
    What is DNS main role

DNS Record Types

    A
    CNAME
    TXT
    MX

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 16.04 LTS
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    All your Bash script files must be executable
    Your Bash script must pass Shellcheck (version 0.3.7) without any error
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing
    You can’t use systemctl for restarting a process

Tasks
0. Transfer a file to your server
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that transfers a file from our client to a server:

Requirements:

    Accepts 4 parameters
        The path to the file to be transferred
        The IP of the server we want to transfer the file to
        The username scp connects with
        The path to the SSH private key that scp uses
    Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
    scp must transfer the file to the user home directory ~/
    Strict host key checking must be disabled when using scp


1. Install nginx web server
mandatory
Score: 0.0% (Checks completed: 0.0%)

Readme:

    -y on apt-get command

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

    Install nginx on your web-01
    server
    Nginx should be listening on port 80
    When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
    As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
    You can’t use systemctl for restarting nginx

Server terminal:

root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 

Local terminal:

sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$

In this example 34.198.248.145 is the IP of my web-01 server. If you want to query the Nginx that is locally installed on your server, you can use curl 127.0.0.1.

If things are not going as expected, make sure to check out Nginx logs, they can be found in /var/log/.

Maarten’s PRO-tip: When you use sudo su on your web-01 you can become root like this to test your file:


2. Setup a domain name
mandatory
Score: 0.0% (Checks completed: 0.0%)

.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

YOU can have a free .tech domain for 1 year by following these steps:

    Access the tools space
    Unlock the GitHub student pack: WARNING - this invitation link is unique to you and can’t be reclaimed! If you have any issue, please contact GitHub education support

    When registered, access your benefits:

    And scroll to .Tech domain:

    Start to register your domain and checkout
    At the Checkout step, please click on “Login with GitHub”:

    The cost of the domain should be now at $0
    You can finalize it by creating an account in .Tech domains
    And manage your domain there!

Provide the domain name in your answer file.

Requirement:

    provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
    configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
    go to your profile and enter your domain in the Project website url field


3. Redirection
mandatory
Score: 0.0% (Checks completed: 0.0%)

Readme:

    Replace a line with multiple lines with sed

Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

    The redirection must be a “301 Moved Permanently”
    You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
    Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task


4. Not found page 404
mandatory
Score: 0.0% (Checks completed: 0.0%)

Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

    The page must return an HTTP 404 error code
    The page must contain the string Ceci n'est pas une page
    Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task


5. Install Nginx web server (w/ Puppet)
#advanced
Score: 0.0% (Checks completed: 0.0%)

Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

    Nginx should be listening on port 80
    When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
    The redirection must be a “301 Moved Permanently”
    Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements


