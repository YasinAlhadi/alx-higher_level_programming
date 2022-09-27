#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject
 *
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t index = 0;
	PyListObject list;

	PyObject = *item;
	size = Py_SIZE(p);
	list = (PyListObject *) p;
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, index);
		printf("Element %zd: %s\n", index, item->ob_type->tp_name);
	}
}
