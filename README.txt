=== SendHub Coding Test Web Service ===
Author: Kumar Thurimella

=== Complexity Analysis ===
i. Provide an analysis of the computational complexity of the algorithm you used to solve
the problem.
Answer: Figuring out the number of requests takes constant time (the for loop in count_senders function). Most time is spent in the json.dumps and json.loads functions.

ii. What is its complexity?
Answer: JSON functions need to traverse the dictionaries and transform them into Python data structures and vice versa. These operations are proportional to the size of the input/output. This is linear in the size of the input, i.e. O(n). The greedy algorithm used will be constant time, i.e. O(1) because there only 4 categories of message relays. 

iii. Can you categorize this problem into the same category of other well  known problems?
Answer: Yes, the solution to the problem falls into the category of greedy algorithms. [See 1]

iv. Is it possible to optimally solve this problem in polynomial time? What about with other throughput values?
Answer: Yes, as described above this program runs in linear time, which is polynomial time. However, this solution does not work if the throughput of 1 msgs/request does not exist.

As an example consider if you had only 3 throughputs, namely 1 msgs/request, 6 msgs/request and 7 msgs/request. If we would like to route 18 requests the greedy solution would be to use [2, 0, 4] corresponding to [7 msgs/request, 6 msgs/request, 1 msgs/request] which would produce a total of 6 requests. However, the smallest number of requests would be [0, 3, 0] or 3 requests with 6 msgs/requsts. 

=== Usage ===
This web service is hosted on Heroku under, http://sendhub-kthurimella.herokuapp.com/. 

To generate a random phone number input, please refer to the function generate_phone_numbers.py. Here is an example use case:

$ python generate_phone_numbers.py 15 'Hello World'

This will generate an input file named input_15_phone_numbers.txt with the message Hello World inside of it, in the proper input format. Please note that this is assuming that you do not use an apostrophe in the message argument. 

Once an input file is generated to generate the output please use the following curl command:

$ curl -i -F input=@input_15_phone_numbers.txt http://sendhub-kthurimella.herokuapp.com

This will send the output to stdout. If you prefer to have the output saved to a file invoke the command as follows:

$ curl -i -F input=@input_15_phone_numbers.txt http://sendhub-kthurimella.herokuapp.com -o output.txt

The application is written in SendHubCodingTest.py.

=== use_cases Directory ===

Under this directory, you will find the following files. All input was generated using 
generate_phone_numbers.py. To generate input files with different argumets, see the usage section above.

input_3_non_unique.txt       //three phone numbers where two are the same
output_3_non_unique.txt

input_6_phone_numbers.txt     //normal 6 phone number input 
output_6_phone_numbers.txt

input_12_phone_numbers.txt   //normal 12 phone number input 
output_12_phone_numbers.txt    

output_6_not_10_digits.txt  //input with incorrect phone numbers
input_6_not_10_digits.txt     

input_5089_phone_numbers.txt    //input with a large number phone numbers
output_5089_phone_numbers.txt

=== Error Handling & Assumptions ===
It's also assumed that the phone numbers do not have any leading zeros. If the phone number list exceeds 10414, or there are no phone numbers in the input file an error is generated. The number 10414 comes from the fact that using 8 bits the number of available hosts is 2^8 - 2, namely 254 [See 2]. If the phone number is not in the format 3104532345 then there is an error raised, and the bad numbers are listed. If there are non-unique numbers generated then another exception is raised as well. When handling duplicates, every number appearing n times will be printed (n-1) times, for ease to correct each duplicate. 

=== Improvements ===
1) Extensive testing and error handling
2) Exception handling 
3) Make the code conform to best practices
4) Documentation, and
5) Performance stress testing


References:
[1] Rosen, Kenneth H. Discrete mathematics and its applications. New York: McGraw-Hill, 1999.
[2] http://en.wikipedia.org/wiki/Subnetwork#Subnet_and_host_counts
