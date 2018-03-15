Feature: Student can see CCX course, courseware, course info and theory tabs
  Scenario Outline:
  Given student are in Labster website
	When they login into labster using their "<email>" & "<password>"
	Then they should be able to see the course that they enroll with

	Examples:

	| email							         		| password	|
	| isaac+999@labster.com					| lab2ster	|

  Scenario:
	Given student already in dashboard page
	When they click on the CCX course
	Then they should be able to access the courseware, course info and theory tabs
