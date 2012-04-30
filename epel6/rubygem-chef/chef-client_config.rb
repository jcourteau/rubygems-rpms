# This is a basic default chef client configuration.  Please see
# http://wiki.opscode.com/display/chef/Installing+Chef+Client+on+CentOS#InstallingChefClientonCentOS-Configurechefclient
# for more info on configuring your system, or
# http://wiki.opscode.com/display/chef/Chef+Configuration+Settings
# for a full list of configuration settings.
#
# In all the following examples, for Hosted Chef users, ORGNAME is the
# Organization Short Name from your Hosted Chef Management Console.

log_level        :info
log_location     STDOUT

# If you use your own Chef server, put the URL here.  If you use Hosted Chef
# the URL should look like
# chef_server_url 'https://api.opscode.com/organizations/ORGNAME'
chef_server_url  'http://yourchefserver.com:4000'

# The validation key can be downloaded from your Chef server in /etc/chef,
# retrieved by knife with "knife configure client" if you have a Chef
# workstation with knife configured, or downloaded from your Hosted Chef
# management console.  Note that Hosted chef keys are named
# ORGNAME-validator.pem
validation_key   "/etc/chef/validation.pem"

# If you use Hosted Chef, this should be ORGNAME-validator
validation_client_name 'chef-validator'
