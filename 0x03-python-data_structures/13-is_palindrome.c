#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */

int checkPalindrome(listint_t **left, listint_t *right)
{
	int res;
	
	if (right == NULL)
		return 1;

	res = checkPalindrome(left, right->next) && ((*left)->n == right->n);
	(*left) = (*left)->next;

	return res;
}

int is_palindrome(listint_t **head)
{
	return checkPalindrome(&(*head), *head);
}

