 0x0A. Configuration management
DevOpsSysAdminScriptingCI/CD

Resources

Read or watch:

    Intro to Configuration Management
    Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
    Puppet’s Declarative Language: Modeling Instead of Scripting
    Puppet lint
    Puppet emacs mode

Requirements
General

    All your files will be interpreted on Ubuntu 20.04 LTS
    All your files should end with a new line
    A README.md file at the root of the folder of the project is mandatory
    Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
    Your Puppet manifests must run without error
    Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
    Your Puppet manifests files must end with the extension .pp

Note on Versioning

Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled. 

Tasks
0. Create a file
mandatory
Score: 0.0% (Checks completed: 0.0%)

Using Puppet, create a file in /tmp.

Requirements:

    File path is /tmp/school
    File permission is 0744
    File owner is www-data
    File group is www-data
    File contains I love Puppet


1. Install a package
mandatory
Score: 0.0% (Checks completed: 0.0%)

Using Puppet, install flask from pip3.

Requirements:

    Install flask
    Version must be 2.1.0

Example:



1. Install a package
mandatory
Score: 0.0% (Checks completed: 0.0%)

Using Puppet, install flask from pip3.

Requirements:

    Install flask
    Version must be 2.1.0

Example:
