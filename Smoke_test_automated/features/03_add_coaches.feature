@skip
Feature: Admin can add CCX coach
  Scenario Outline: Admin should be able to add an active account as a CCX coach
  Given we have login into Labster as an admin using "<email>" and "<password>"
	When we add new CCX coach "<instructorUsername>"
	Then a new coach should be registered

	Examples:

	| email        			| password		| instructorUsername|
	| isaac@labster.com	| lab2ster		| isaac030     			|
