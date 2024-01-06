#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (recur_pal(head, *head));
}

/**
 * recur_pal - recursive function to check first against last
 * @head: start of the list
 * @tail: end of the list
 * Return: 1 if palindrome, 0 if not
 */
int recur_pal(listint_t **head, listint_t *tail)
{
	if (tail == NULL)
		return (1);
	if (recur_pal(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
