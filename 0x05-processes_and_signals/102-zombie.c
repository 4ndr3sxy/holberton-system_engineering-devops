#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - function called in main
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 * Return: 0
 */
int main(void)
{
	pid_t new_child;
	int count = 1;

	while (count <= 5)
	{
		new_child = fork();

		if (new_child == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", new_child);
		count++;
	}
	infinite_while();
	return (0);
}
