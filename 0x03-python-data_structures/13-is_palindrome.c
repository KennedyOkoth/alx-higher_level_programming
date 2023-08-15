#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: The start of the list
 *
 * Return: 1 if it's a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *tmp = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast && fast->next)
    {
        fast = fast->next->next;
        tmp = slow;
        slow = slow->next;
        tmp->next = prev;
        prev = tmp;
    }

    if (fast)
        slow = slow->next;

    while (prev && slow)
    {
        if (prev->n != slow->n)
            return (0);
        prev = prev->next;
        slow = slow->next;
    }

    return (1);
}