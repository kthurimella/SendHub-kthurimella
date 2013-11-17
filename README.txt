=== SendHub Coding Test Web Service ===
Author: Kumar Thurimella

=== Complexity Analysis ===
i. Provide an analysis of the computational complexity of the algorithm you used to solve
the problem.
Answer: Figuring out the number of requests takes constant time (the for loop in count_senders function). Most time is spent in the json.dumps and json.loads functions.

ii. What is its complexity?
Answer: JSON functions need to traverse the dictionaries and transform them into Python data structures and vice versa. These operations are proportional to the size of the input/output. This is linear in the size of the input, i.e. O(n). The greedy algorithm used will be constant time, i.e. O(1) because there only 4 categories of message relays. 

iii. Can you categorize this problem into the same category of other well  known problems?
Answer: Yes, the solution to the problem falls into the category of greedy algorithms. 

iv. Is it possible to optimally solve this problem in polynomial time? What about with other throughput values?
Answer: Yes, as described above this program runs in linear time, which is polynomial time. However, this solution does not work if the throughput of 1 msgs/request does not exist.

As an example consider if you had only 3 throughputs, namely 1 msgs/request, 6 msgs/request and 7 msgs/request. If we would like to route 18 requests the greedy solution would be to use [2, 0, 4] corresponding to [7 msgs/request, 6 msgs/request, 1 msgs/request] which would produce a total of 6 requests. However, the smallest number of requests would be [0, 3, 0] or 3 requests with 6 msgs/requsts. 

=== Usage ===
This web service is hosted on Heroku under, http://sendhub-kthurimella.herokuapp.com/. 

