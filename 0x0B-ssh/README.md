 0x0B. SSH
DevOpsSSHNetworkSysAdminSecurity

Resources

Read or watch:

    What is a (physical) server - text
    What is a (physical) server - video
    SSH essentials
    SSH Config File
    Public Key Authentication for SSH
    How Secure Shell Works
    SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

For reference:

    Understanding the SSH Encryption and Connection Process
    Secure Shell Wiki
    IETF RFC 4251 (Description of the SSH Protocol)
    Internet Engineering Task Force
    Request for Comments

man or help:

    ssh
    ssh-keygen
    env

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What is a server
    Where servers usually live
    What is SSH
    How to create an SSH RSA key pair
    How to connect to a remote host using an SSH RSA key pair
    The advantage of using #!/usr/bin/env bash instead of /bin/bash

Copyright - Plagiarism

    You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
    You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
    You are not allowed to publish any content of this project.
    Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

    Allowed editors: vi, vim, emacs
    All your files will be interpreted on Ubuntu 20.04 LTS
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    All your Bash script files must be executable
    The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing


Tasks
0. Use a private key
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

    Only use ssh single-character flags
    You cannot use -l
    You do not need to handle the case of a private key protected by a passphrase



1. Create an SSH key pair
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that creates an RSA key pair.

Requirements:

    Name of the created private key must be school
    Number of bits in the created key to be created 4096
    The created key must be protected by the passphrase betty

Example:



2. Client configuration file
mandatory
Score: 0.0% (Checks completed: 0.0%)

Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password

Example:



3. Let me in!
mandatory
Score: 0.0% (Checks completed: 0.0%)

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.



4. Client configuration file (w/ Puppet)
#advanced
Score: 0.0% (Checks completed: 0.0%)

Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

    Your SSH client configuration must be configured to use the private key ~/.ssh/school
    Your SSH client configuration must be configured to refuse to authenticate using a password

Example:


