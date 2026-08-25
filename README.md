#include <stdio.h>
#include <string.h>

void character_count()
{
    char data[100];
    int count;

    printf("\nEnter data: ");
    scanf("%s", data);

    count = strlen(data) + 1;

    printf("Framed data: %d%s\n", count, data);
}

void character_stuffing()
{
    char data[100], framed[200];
    char flag = 'F', esc = 'E';
    int i, j = 0;

    printf("\nEnter data: ");
    scanf("%s", data);

    framed[j++] = flag;

    for (i = 0; data[i] != '\0'; i++)
    {
        if (data[i] == flag || data[i] == esc)
            framed[j++] = esc;

        framed[j++] = data[i];
    }

    framed[j++] = flag;
    framed[j] = '\0';

    printf("Framed data: %s\n", framed);
}

void bit_stuffing()
{
    char data[200], stuffed[400];
    int i, j = 0, count = 0;

    printf("\nEnter bit string: ");
    scanf("%s", data);

    for (i = 0; data[i] != '\0'; i++)
    {
        stuffed[j++] = data[i];

        if (data[i] == '1')
            count++;
        else
            count = 0;

        if (count == 5)
        {
            stuffed[j++] = '0';
            count = 0;
        }
    }

    stuffed[j] = '\0';

    printf("After bit stuffing: %s\n", stuffed);
}

int main()
{
    int choice;

    printf("DATA LINK LAYER FRAMING METHODS\n");
    printf("1. Character Count\n");
    printf("2. Character Stuffing\n");
    printf("3. Bit Stuffing\n");

    printf("\nEnter your choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
        case 1:
            character_count();
            break;

        case 2:
            character_stuffing();
            break;

        case 3:
            bit_stuffing();
            break;

        default:
            printf("Invalid choice!\n");
    }

    return 0;
}
https://chatgpt.com/share/6a8d302b-2f50-83ee-8ec5-73db5a68b85a?ogimg=plain
