#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
  int i, x;
  listint_t *end, *start;

  i = 0;
  end = *head;
  start = *head;
  
  if (*head != NULL)
    {
      while (end != NULL)
	{
	  end = end->next;
	  i++;
	}
      
      if (i <= 1)
	{
	  return (1);
	}

      end = *head;
      while (i > 0)
	{
	  for (x = 0; x < (i - 1); x++)
	    {
	      end = end->next;
	    }
	  
	  if (start->n != end->n)
	    {
	      return (0);
	    }
	  start = start->next;
	  end = *head;
	  i--;
	}
      return (1);
    }
  return (1);
}
