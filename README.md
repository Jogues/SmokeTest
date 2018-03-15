# SmokeTest

Dependancy:
*behave
*python 2.7
*selenium

Steps to run the Script
1. Go to environment.py and modify the location of the Chromedriver
2. Create a new license in Salesforce and use the feature course creation as well to create the course directly
3. Update 08_generate_vouchers.feature with the newly created license code
4. Open your local directory via CMD and run this command behave --tags=~@skip 
5. Wait for the test to be finished
6. What left to be done are Play the simulation, check save data, check grades, ref link and check languages Ohh and license overlimit.
