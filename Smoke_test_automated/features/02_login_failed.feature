Feature: login failed
  Scenario Outline:
  Given user is on login page
	When I login with "<email>" and "<password>"
	Then I will have an error

	Examples:

	| email		    | password		|
	| isaac@labster.com | isaac12 		|
