#!/usr/bin/python3

# Create a directory (i.e. folder)
run("mkdir /data/")
run("mkdir /data/web_static/")
run("mkdir /data/web_static/releases/")
run("mkdir /data/web_static/shared/")
run("mkdir /data/web_static/releases/test/")
run("touch /data/web_static/releases/test/index.html")
run("ln /data/web_static/current /data/web_static/releases/test/")







# Hostname
run("hostname")

# Capture the output of "ls" command
result = run("ls -l /var/www")

# Check if command failed
result.failed
