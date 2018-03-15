@skip
Feature: Instructor can create new course and apply license
  Scenario Outline: Instructor should be able to create new course
  Given Instructor already login to Labster using "<email>" and "<password>"
	When they go to ccx coach menu and add "<course>" as a new course
	Then a new course should be created

	Examples:

	| email					        | password 		| course		  	|
	| isaac+030@labster.com	| lab2ster		| AT 050318			|


  Scenario Outline: Instructor should be able to apply the license
  Given Instructor open the license tab
	When Instructor input the correct CK "<consumerKey>", SK "<secretKey>", and license code "<licCode>"
	Then the license should applied correctly

	Examples:

	| consumerKey							               	| secretKey									              | licCode			|
	| Ck3084af98-9e4d-8e27-7dca-050f3262cb37	| Skc8a5cb12-49cf-0c81-009e-2961639fa1c3	| XUECRC			|
