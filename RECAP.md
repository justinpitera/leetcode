# Week 1:
Failure loop problems:
Course schedule
number of islands

two sum 1 and 2  # to prepare for two sum 3

# day 1:
failure loop: 
1. best time to buy and sell stock 2 **(was new today) -- super simple overthought it
2. Container with most water **(was new today) -- almost got it on first attempt just remeber to use the correct area formula
3. Course schedule (review problem but struggled)

notes: i did two sum 3 in front of Gavin and I also most of course schedule myself but struggled on discerning which structures to traverse when just dont overthink it in the dfs you loop thru the defaultdict, for populating the dict you go thru the input list (obviously), and then for the main belt go thru the range of numCourses and make sure you if not dfs(course) return False. return True at end of dfs branch and set state properly.