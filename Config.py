import logging

# Logging Settings
APPNAME = "myapp"
LOGFILE = "myapp.log"
LOGLEVEL = logging.DEBUG

# global constants used to create a server
HOSTNAME="10.57.126.171"
PORT="8585"

# No of maximum connections that will be queued / served parallely
MAXCONN = 5
BIGENDIAN = False # only python constants. so no 'true'

# type of Message this simulator should listen to
MSGTYPE = "ISO8583"

#forcing error/corrupt value when forcing vendor response code (field 39)
FORCE_CORRUPT_VALUE_ON_SETTING_FIELD39 = True
