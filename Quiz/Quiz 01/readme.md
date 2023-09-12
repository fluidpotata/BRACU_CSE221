01. (3 marks) Explain the time complexity of the following code snippet in regards of the Big-O notation:
```
def loopity_loop (arr: List[int]):
	  n = len(arr)
	  for i in range (0, n):
		  for j in range (i, n):
			  if (arr[i] == arr[j]):
				  break
```

<b>Ans:</b> Here, as j always starts traversing from i, arr[j] will always be equal to arr[i], hence the inner loop will never run more than once. So, the complexity will be O(n), as the outer loop will run n times and the inner will run only once.
<br>
<br>
02. (3 marks) Explain the time complexity of the following code snippet in regards of the Big-O notation:
```
def whatchudoin (arr: List[int]):
	n = len(arr)
		for i in range (0, n):
			for j in range (0, i):
				for k in range(i, j):
					print(“Bazinga!”)
```

<b>Ans:</b> Simulate it a bit. Look at the values of i, j, k.
i = 0, j = 0, k = 0 to 0
i = 1, j = 0, k = 1 to 0 (so, this will not run)
i = 1, j = 1, k = 1 to 1
i = 2, j = 0, k = 2 to 0 (so, this will not run)
i = 2, j = 1, k = 2 to 1 (so, this will not run)
i = 2, j = 2, k = 2 to 2

So, the innermost loop with k will only run once each time, because j only goes from 0 to i, and k is supposed to go from i to j, so k will only run when i equals j.
And if you look at j, then it will go from 0 to 0 in the first round, then 0 to 1, then 0 to 2 and so on. And in the last round, it will go from 0 to n-1.
So, in total, 
j goes from 0 to 0 = 1
j goes from 0 to 1 = 2
j goes from 0 to 2 = 3
……………………..
j goes from 0 to n-1 = n

Summing it all, 1 + 2 + … + n = n * (n+1)/2 = (n2 + n)/2
Hence, O(n2).<br>
<br>
03. 1 mark) Just mention the time complexity of the following code snippet in regards of the Big-O notation:
```
def dont_think_too_much (n: int):
	for i in range (0, n):
		for j in range (n-1, -1, -1):
			print(“But you still did, right?”)
```
<b>Ans:</b> Here, both loops will run n times. So it’s simply O(n2).<br>
<br>
04. (1 mark) Just mention the time complexity of the following code snippet in regards of the Big-O notation:
```
def being_weak_is_foine (n: int):
	i, j = (0, 1)
	while (i < n):
		i += 1
		while (j < n):
			j *= 5
			print(“JK. Weakness disgusts me.”)
```

<b>Ans:</b> Here, the outer loop will run n times and the inner loop will run log5n times as j is multiplied with 5 each time. Hence, the complexity will be O(n * log5n).<br>
<br>
05. (1 mark) Just mention the time complexity of the following code snippet in regards of the Big-O notation:
```
def the_statement_below_is_true (n: int):
	for i in range (0, n/2):
		for j in range (n, n/2, -1):
			print(“The statement above is false.”)
```
<b>Ans:</b> Here, both loops will run n/2 times. So it’s simply O(n/2 * n/2) = O(n2).<br>
<br>
06. (1 mark) Just mention the time complexity of the following code snippet in regards of the Big-O notation:
```
def it’s_done_it’s_over (n: int):
	for i in range (0, n/2):
		print(“Done with Iterative Complexity Horror!”)
	j = 1
	while (j < n):
		j *= 2
		print(“Or are you? ¯\_(ツ)_/¯”)
```
<b>Ans:</b> The first loop will run n/2 times and the second one will run log2n times as j is multiplied with 2 each time. Hence, the complexity will be O(n/2 + log2n) = O(n), as n easily dominates logn.
