Feature: Student should be able to unenroll from his course
  Scenario Outline:
  Given student login into labster using "<email>" & "<password>"
	When he arrive in dashboard and check that the courses that he want to unenroll is present
	and click setting button and unenroll from course
	Then he should be successfully unenroll from that course

	Examples:

	| email			| password	|
	| isaac+998@labster.com	| lab2ster	|
