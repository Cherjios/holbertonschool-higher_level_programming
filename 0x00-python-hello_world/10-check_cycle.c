#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cyclical
 * @list: pointer to list to check
 * Return: 0 no cycle, 1 cucle found
 */
int check_cycle(listint_t *list)
{
	listint_t  *slow_p = list, *fast_p = list;

	while (slow_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;

	/* If slow_p and fast_p meet at some point then there is a loop */
		if (slow_p == fast_p)
		{
			/* Return 1 to indicate that loop is found */
			return (1);
		}
	}

	/* Return 0 to indeciate that ther is no loop*/
	return (0);
}

