# CECS328 Pytest Files

## Overview

This repo contains pytest files that can be used for CECS328, spring semester 2025. Each of the pytest files follows the naming convention
that is asked for by the programming assignments and pytest. Therefore, each file has the word `test_*` in front of the file name that is requested
from the programming assignment.

**All of these pytest files have tests that I have thought of prior to submission of the programming assignment. I have no way of knowing what tests
will be used to check programming assignments.**

This repo is also something for myself to get more practice with using GitHub and the features that it has.

> [!WARNING]
> The lifetime for this repo at the moment will only be for this semester of CECS328. After the semester, I plan on no longer having this repo public.

## Installation

> [!NOTE]
> To run pytest you need pip and Python 3.8+.
> Pip comes installed with Python 3.4+.

Install pytest:

```
pip install -U pytest
```

> [!TIP]
> I recommend going to the [pytest](https://docs.pytest.org/en/stable/) and reading through their documentation.

## How to Use

To use one of the testing files you need to have the file on your local machine. You can download the repo as a zip file, copy and paste the code into your
editor of choice, or clone this repo. Whichever way you choose to get the file on your local machine is up to you.

Once the file is on your local machine **MOVE** the file to be in the same folder as the programming assignment you are trying to test.
Then, run the following command in the same folder that both the test file and programming assignment:

```
pytest
```

Pytest should run all of the test and provide you with an output displaying if the tests have passed or failed.

## Useful Pytest Flags

You can simply run the pytest command and get your output, but there are some useful commands that I have came across.

Verbose output - each flag provides a different verbose output

```
pytest -v
```

```
pytest -vv
```

```
pytest -vvv
```

Durations - will provide which of your tests are running the slowest:

```
pytest --durations=3
```

> [!NOTE]
> The number after `--durations=` will display slowest running test equal to that number.
> You can use `--durations=0` to display the duration of all the tests, but you must use the `-vv` verbose flag to get that information.

My current command:

```
pytest -vv --durations=0
```

> [!TIP]
> Less is more! If you are using a `unix` based system, I completely recommend to pipe the output to the `less` command.

```
pytest -vv --durations=0 | less
```

This allows me to display how long it took for all the tests to run with a more verbose output.

These are not necessary, but they are helpful.

## FAQs

**Q: Why is Pytest running all of my test files?**

A: If you simply run the pytest command, pytest will run all test files in the current directory and any sub-directories. If you want to only run the pytest file for the
programming assignment that you are working on, make sure that you have both the test file and assignment file in a separate directory. Then run pytest in that directory
to only test for that file.

**Q: Pytest is not recognizing my function, what is the issue?**

A: I am following the naming convention that is listed in the programming assignment instructions. If it does not work, then make sure your function is following the naming
convention that was given.

**Q: Why can I not run the pytest file from a different folder instead?**

A: While it is possible, the way that I wrote these pytest files with the thought that both would be inside the same folder. I wrote them this way to keep it as simple as possible
since I am not sure how others would be structuring their folders for the programming assignments. If you do decide to change where the tests are going, make sure you edit the pytest
file to import your programming assigment file correctly **on your local machine**. I will be keeping these files as intended, again with the most simple set up as possible.

**Q: The rubric for the PA got posted, will you be updating the testing files?**

A: No.
I intend to keep these test files with student thought test cases.

**Q: What do I do if I notice an issue with the pytest file?**

A: Let me know!
I am still learning how to navigate with GitHub and as well as pull requests. So if you want to use that feature or use the Issues feature to submit an issue, then please go for it!
You can also message me on discord as well. **I will be slow on responding as I have other priorities with my job, but I will get to those pull requests, issues, or messages as soon
as I can!**

**Q: Can I provide some test ideas?**

A: Of course! I also intended to make this collaborative as possible. But please, do not feel that you need to help out. I simply just wanted to be helpful for everyone and create something
that I felt we could all use.
