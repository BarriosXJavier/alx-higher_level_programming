#include "lists.h"
#include <stdio.h>

/*main -  check if a linked list has a cycle */
/*check_cycle - check for a cycle */

int check_cycle(listint_t *list)
{
	/* Initialize two pointers, one slow and one fast */
	listint_t *slow = list;
	listint_t *fast = list;

	/* Traverse the list */
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		/* Move the slow pointer one step at a time */
		slow = slow->next;

		/* Move the fast pointer two steps at a time */
		fast = fast->next->next;

		/* If the pointers meet, there is a cycle */
		if (slow == fast)
			return (1); /* Cycle detected */
	}

	return (0); /* No cycle found */
}

int main(void)
{
	/* Check if the linked list has a cycle */
	if (check_cycle(head))
	{
		printf("The linked list has a cycle.\n");
	} else
		printf("The linked list does not have a cycle.\n");

	free(head);
	free(node1);
	free(node2);
	free(node3);

	return (0);
}
