#include "lists.h"

/**
 * check_cycle - check if list is cycle
 * @list: list to check
 *
 * Return: 0 for no, 1 for yes
 */

int check_cycle(listint_t *list)
{
listint_t *curr, *tmp;

if (list == NULL || list->next == NULL)
{
  return (0);
}
 
curr = list;
tmp = list;

while (curr != NULL && tmp != NULL && tmp->next != NULL)
{
  curr = curr->next;
  tmp = tmp->next->next;

  if (curr == tmp)
    {
      return (1);
    }
}
 return (0);
}
