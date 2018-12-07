#!/usr/bin/python
## Above is required as the first line of all python files
 
##
## Testing Jinja Templates Python Script
## Created 12/1/2016 by NSC (Derived from Network Automation script published in
## Network Programmability and Automation by Jason Edelman, Scott Lowe, and Matt Oswalt)
## This script creates (renders) a template using the template file "l2_baseline.j2" and
## replaces the hostname variable
##
 
## Import YAML so that the baseline YAML file containing all the data can be loaded
import yaml
 
## Load the jinja2 environment, so Python knows how to interact with the template
from jinja2 import Environment, FileSystemLoader
 
## Set the environment to '.'
## This means that any file names used are in the current directory the script is located in
ENV = Environment(loader=FileSystemLoader('.'))
 
## Load the basic-baseline.j2 jinja2 template file
baseline = ENV.get_template("basic-baseline.j2")
 
## Open the YAML file and render config
with open("baseline_data.yaml") as y:
 host_obj = yaml.load(y)
 f = open('config.conf', 'w')
 config = baseline.render(host=host_obj)
 f.write(config)
 f.close
 
## End of Script
