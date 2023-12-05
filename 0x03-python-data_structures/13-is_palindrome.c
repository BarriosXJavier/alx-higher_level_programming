#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int main() 
{
	/* example */
	listint_t *head = NULL;
	/* palindrome list */
	for (int i = 1; i <= 3; ++i)
	{
		listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
		new_node->data = i;
		new_node->next = head;
		head = new_node;
	}
	for (int i = 3; i >= 1; --i)
	{
		listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
		new_node->data = i;
		new_node->next = head;
		head = new_node;
	}

	int result = is_palindrome(&head);

	printf("Is the list a palindrome? %s\n", result ? "Yes" : "No");

	/* Free mem*/
	while (head)
	{
		listint_t *temp = head;
		head = head->next;
		free(temp);
	}

	return 0;
	}

	int is_palindrome(listint_t **head) 
	{
		listint_t *fast = *head;
		listint_t *slow = *head;
		listint_t *prev_slow = NULL;
		listint_t *mid = NULL;
 
		int is_palindrome = 1;

	/*Find the middle of the linked list*/
		while (fast && fast->next) 
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

	/* If the list has odd number of elements, skip the middle*/
		if (fast != NULL) 
		{
			mid = slow;
			slow = slow->next;
		}

	/*Reverse the second half of the linked list*/
		listint_t *second_half = slow;
		prev_slow->next = NULL;
		listint_t *prev = NULL;
		listint_t *current = second_half;
		listint_t *next = NULL;

		while (current != NULL) 
		{
			next = current->next;
			current->next = prev;
			prev = current;
			current = next;
		}

		second_half = prev; /*Head of the reversed second half*/

	/*Compare the first and reversed second halves*/
		listint_t *first_half = *head;
		while (first_half && second_half) 
		{
			if (first_half->data != second_half->data) 
			{
				is_palindrome = 0;
				break;
			}
			first_half = first_half->next;
			second_half = second_half->next;
		}

	/*Restore the original linked list*/
		prev = NULL;
		current = mid;
		next = NULL;
		while (current != NULL) 
		{
			next = current->next;
			current->next = prev;
			prev = current;
			current = next;
		}
		if (mid != NULL) 
		{
			prev_slow->next = mid;
			mid->next = second_half;
		} else {
			prev_slow->next = second_half;
		}

		return is_palindrome;
}
