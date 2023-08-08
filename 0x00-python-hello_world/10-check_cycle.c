#include "lists.h"

/**
 * check_cycle - Checks if the list has a loop
 * @list: The list to check
 * 
 * Return: either 0 or 1
*/
int check_c9ylcle(listint_t *list)
{
    listint *fast = list;
    listint *slow = list;

    while (fast != NULL && slow != NULL)
    {
        slow = slow->next;
        if (fast->next == NULL)
            return (0);
        fast = fast->next;
        fast = fast->next;

        if (fast == slow)
            return (1);
    }
    return (0);
}
