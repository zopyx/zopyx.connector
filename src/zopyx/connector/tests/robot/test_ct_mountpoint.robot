# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s zopyx.connector -t test_mountpoint.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src zopyx.connector.testing.ZOPYX_CONNECTOR_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/zopyx/connector/tests/robot/test_mountpoint.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Mountpoint
  Given a logged-in site administrator
    and an add Mountpoint form
   When I type 'My Mountpoint' into the title field
    and I submit the form
   Then a Mountpoint with the title 'My Mountpoint' has been created

Scenario: As a site administrator I can view a Mountpoint
  Given a logged-in site administrator
    and a Mountpoint 'My Mountpoint'
   When I go to the Mountpoint view
   Then I can see the Mountpoint title 'My Mountpoint'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Mountpoint form
  Go To  ${PLONE_URL}/++add++Mountpoint

a Mountpoint 'My Mountpoint'
  Create content  type=Mountpoint  id=my-mountpoint  title=My Mountpoint

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Mountpoint view
  Go To  ${PLONE_URL}/my-mountpoint
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Mountpoint with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Mountpoint title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
