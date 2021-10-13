Advanced Test Driven Development (TDD) -- Robert Martin

2021-10-11 - Uncle Bob gave a presentation on Test Driven Development. He started with motivational examples showing that if we don't have more disipline as developers-- we will get regulated and constrained.


The Three Laws of Test Driven Development (disipline) 

1) Your are not allowed to write any production code until you have first writtne a unit test that fails due to its absense.
2) You are not allowed to write more of a unit test than is sufficent to fail.  Failing to compile is failing.
3) You are not allowed to write more production code than is sufficient to cause the currently failing test to pass.


RESULTS
---------------------
"Reduce Debug time by N "
"Tests are the low level documentation for the programmers to read"
"Tests tell you how something works in the system"
"You can make decisions on your test suite"
"Your design will be better -- (decoupled more)"

WHY DO TDD?
----------------
A:  To make improvements easy.

You can make code get better with time instead of degrading.
If your afraid of code -- it controls you, you can't clean.  It will rot.
Everyone afraid to do what is needed ( clean the code).

Like accounting -- "double entry bookkeeping is TDD"


pattern for a test.
------------------
Arrange
Action  -- should only have single action.
Assert


Unit-test :   Tests written by programmers for programmers;

Tests need to be maintained the same level of quality as production code.

QA may hit only 50% of the code,only programmers can reach the other 50% .

"We write comments when the code does not explain itself.  Tests can sometimes be better than comments. We will still write comments."  

composed test result..


F.I.R.S.T
Fast                 - (may only run tests for component as you are working on it to make test cycle faster)
Isolated&Independent -  tests don't depend on eachother. careful with static variables
Repeatable           -  should be able to run on laptop, production, test (minimize enviromental dependencies)
Self Verifying       -  binary (Pass, or Fail)
Timely               -  Treat as more important than production code:  write tests before code, refactored first, 










