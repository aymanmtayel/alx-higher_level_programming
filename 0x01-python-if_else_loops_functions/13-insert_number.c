#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the pointer of list head
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *after = malloc(sizeof(listint_t));

	if (!after)
		return (NULL);
	after->n = number;
	after->next = NULL;

	if (!current || after->n < current->n)
	{
		after->next = current;
		return (*head = after);
	}
	while (current)
	{
		if (!current->next || after->n < current->next->n)
		{
			after->next = current->next;
			current->next = after;
			return (current);
		}
		current = current->next;
	}
	return (NULL);
}
