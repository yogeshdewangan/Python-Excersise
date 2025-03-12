'''We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string that denotes a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Input Format

The first line contains a single integer, , the number of operations to perform.
Each line  of the  subsequent lines contains an operation in one of the two forms defined above.

Constraints

It is guaranteed that  and  contain lowercase English letters only.
The input does not have any duplicate  for the  operation.
Output Format

For each find partial operation, print the number of contact names starting with  on a new line.

Sample Input

4
add hack
add hackerrank
find hac
find hak
Sample Output

2
0'''


def operation(op, contact):
    if op == "add":
        contact_list.append(contact)
    else:  # find
        count = 0
        for contact_item in contact_list:
            if contact in contact_item:
                count += 1
        print (count)


if __name__ == '__main__':
    n = int(input().strip())
    contact_list = []

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        op = first_multiple_input[0]

        contact = first_multiple_input[1]
        operation(op, contact)
