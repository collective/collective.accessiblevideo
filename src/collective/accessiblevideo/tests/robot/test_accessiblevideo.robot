# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.accessiblevideo -t test_accessiblevideo.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.accessiblevideo.testing.COLLECTIVE_ACCESSIBLEVIDEO_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_accessiblevideo.robot
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

Scenario: As a site administrator I can add a AccessibleVideo
  Given a logged-in site administrator
    and an add accessiblevideo form
   When I type 'My AccessibleVideo' into the title field
    and I submit the form
   Then a accessiblevideo with the title 'My AccessibleVideo' has been created

Scenario: As a site administrator I can view a AccessibleVideo
  Given a logged-in site administrator
    and a accessiblevideo 'My AccessibleVideo'
   When I go to the accessiblevideo view
   Then I can see the accessiblevideo title 'My AccessibleVideo'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add accessiblevideo form
  Go To  ${PLONE_URL}/++add++AccessibleVideo

a accessiblevideo 'My AccessibleVideo'
  Create content  type=AccessibleVideo  id=my-accessiblevideo  title=My AccessibleVideo


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the accessiblevideo view
  Go To  ${PLONE_URL}/my-accessiblevideo
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a accessiblevideo with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the accessiblevideo title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
