#include <python.h>

/**
 * print_python_list_info - function that prints some basic
 * info about Python lists.
 * @p: a python list to be evaluated
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	int length, size_alloc, counter;
	pyobject *object_t;

	length = PY_SIZE(p);
	size_alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python list = %d\n", length);
	printf("[*] Allocated = %d\n", size_alloc);

	for (counter = 0; counter < length; counter++)
	{
		printf("Element %d: ", counter);
		object_t = PyList_GetItem(p, counter);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
