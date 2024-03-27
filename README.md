# comment_remover_python
Removes both single-line, multi-line comments or both + ignores print statements with tripple single and double - quotes.

In Python, there's no built-in support for multi-line comments. However, a common convention is to use triple quotes (''' or """) to create multi-line strings, which are then effectively treated as comments by the interpreter. But with a script like this that finds matches with regular expressions it could easily also remove more or less whole print statements using tripple single and double - quotes or remove the content within the print(). 

Well i wrote this script because i did not actually find any solution that involved simplicity so created this script to remove comments from python files in actually sonic speed.

Benchmark it does atleast 1 000 lines of python codes in under 0.9 seconds. It's pretty good if you ask me =)! 

Hope someone will have use for this script and put it to work =D 
