#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

size_t print_dlistint(const dlistint_t *h)
{
  int num;
  num = 0;
  if (!h)
    {
      return (0);
    }

  while (h != NULL)
    {
      printf("%d\n", h->n);
      h = h->next;
      num++;
    }
  return (num);
}
