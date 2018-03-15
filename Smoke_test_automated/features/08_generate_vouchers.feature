Feature: Admin should be able to generate voucher
  Scenario Outline:
  Given Admin already inside API and access voucher menu
	When he select the right license "<license>" and generated voucher
	Then the voucher for that specific license should be created

	Examples:

	| license		|
	| NYISUA		|
