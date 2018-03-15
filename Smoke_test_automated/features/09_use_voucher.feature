@skip
Feature: Student should be able to use voucher to automatically enroll to the course
  Scenario Outline:
  Given student login into Labster using their "<email>" & "<password>"
	When they arrived in dashboard and click on enter access code
	and input the voucher code "<voucherCode>"
  Then they should be enroll correctly into the right course

	Examples:

	| email			         		| password		| voucherCode	|
	| isaac+94@labster.com	| lab2ster		| NLNW94SHYH	|
