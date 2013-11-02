"""
Openclicker - an open source clicker game.
Copyright (C) 2013  Cheryl Yang and Ryan Lam
Contact: cheriexryan@hellokitty.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import os
import sys

# try:
    # os.chdir(os.path.dirname(__file__))
# except WindowsError:
    # pass

# print "*** Syncing The Fucking DB... ***"
# os.system('python manage.py syncdb')

print "\n*** Collecting static... please take off your wool sweaters for safety ***"
if '--clear' in sys.argv:
    # Run collectstatic to collect the static files to the static folder
    # The --clear arg will clear away the existing static files
    os.system('python manage.py collectstatic --clear --noinput')
else:
    # Run collectstatic without clearing
    os.system('python manage.py collectstatic --noinput')

print "\n*** Finally... running the server. Have fun! ***"
os.system('python manage.py runserver')
