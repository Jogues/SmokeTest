Feature: Enroll and unenroll student to the customer course
  Scenario Outline:
  Given user login as instructor account with "<email>" & "<password>"
	When accessing the right course
	And the instructor add a valid email/username "<username>"
	Then the student "<username>" should be enroll into the course

	Examples:

	| email			| password	| username		|
	| isaac+0@labster.com  	| lab2ster	| isaac998		|

  Scenario Outline:
  Given user already in CCX coach page
	When the instructor unenroll a valid email/username "<username>"
	Then the student should be no longer appear in the list

	Examples:
	| username		|
	| isaac998		|

  Scenario Outline:
	Given user already in CCX coach pages
	When the instructor enroll a second valid email/username "<username>"
	Then the student "<username>" should be enroll into the right course

	Examples:

	| username		|
	| isaac998		|
