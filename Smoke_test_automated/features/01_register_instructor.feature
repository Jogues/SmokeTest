@skip
Feature: Register new Instructor account
  Scenario Outline:
  Given user in register user page
	When he register new user with "<email>" "<fullname>" "<username>" and "<password>"
	Then a new account should be created and user redirected to dashboard page

	Examples:

	| email				| fullname	| username		| password		|
	| isaac+0011@labster.com	| isaac		| isaac0011		| lab2ster		|
