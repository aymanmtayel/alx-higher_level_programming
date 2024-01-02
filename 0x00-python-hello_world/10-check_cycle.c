#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the head of the list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *after;

	if (!list || !list->next)
		return (0);
	current = list;
	after = list->next;

	while (after && after->next)
	{
		if (current == after)
			return (1);
		current = current->next;
		after = after->next->next;
	}
	return (0);
}
