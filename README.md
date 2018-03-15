# SmokeTest

Dependancy: behave, python 2.7 and selenium

Steps to run the Script
1. Go to pages/generate_voucher_page.py and fill the usernamApi and passwordApi
2. Go to environment.py and modify the location of the Chromedriver
3. Create a new license in Salesforce and use the feature course creation as well to create the course directly
4. Update 08_generate_vouchers.feature with the newly created license code
5. Open your local directory via CMD and run this command behave --tags=~@skip 
6. Wait for the test to be finished
7. What left to be done are Play the simulation, check save data, check grades, ref link and check languages Ohh and license overlimit.
