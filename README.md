Test Environment Control
=========================

## EPIC

This project is going to do a simple toolkit to help you control your test environment. The final version of this project should contain a UI in it, no matter it is CLI or GUI. Therefore, the project will not just be a script. The version control will based on git. We just use the code to control it. The idea is simple. It just creates a bunch of folder with git and use branch and tag to do the switch.

## Feature

1. The version control. Being a tester, you will need to do the version control. The reasons are following:

    - During deveploping period, you will get a lot of code from developer. (Developer's Code)

    - You will have your own test script to manage. (Test Plan)

    - During test, the sample file may be polluted. (The data that may be used by program.)

    - During test, you may need to output the profile at different steps. (Report)

2. An environment initializer. Sometimes, it is pretty tedious to create your test environment layout. However, the different users may have other habits. Therefore, we may give users some freedom to define their layout by themselves.

    - A default config to initiate your environment.

    - Let user to define his own environment.

3. Test runner. If we can do the test by only click one button, the thing will be easier.

    - Let tester can execute all the test under the project folder, feature folder, test folder or just one test file. 

    - Let user can define which tests they want to use in the program.

4. A report collector. How to generate a report is a big problem for a QA engineer. A report with figures may be difficult to manage. However, the information generated by the test scripts may be collected much easier.

    - This one should support the tester to collect their reports into a specific folder.

    - The other kind of report should be supported in the future.
