#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
  int i;
  listint_t *new, *curr, *prev;

 i = 5;
 
 if (*head == NULL)
   return (NULL);

 curr = *head;
 prev = *head;
 
 new = malloc(sizeof(listint_t));
 if (new == NULL)
   {
     return (NULL);
   }

 for (i = 5; i != 0; i--)
   {
     prev = curr;
     curr = curr->next;
   }
 prev->next = new;
 new->next = curr;
 new->n = number;

 return (new);
}
